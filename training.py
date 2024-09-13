import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

# Para crear la red neuronal
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD

lemmatizer = WordNetLemmatizer()

# Cargar los datos de intenciones
with open('app/intents.json', encoding='utf-8') as file:
    intents = json.load(file)
    

# dividir el texto en oraciones o palabras (tokenización)
nltk.download('punkt')
# Convierte palabras a su forma base o raíz perros perro.
nltk.download('wordnet')
nltk.download('omw-1.4')

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '¿', '.', ',']

# Clasifica los patrones y las categorías
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # divide la lista en arrays en palabras separadas
        word_list = nltk.word_tokenize(pattern)
        # une todo el array en 1 soloa
        words.extend(word_list)
        # se guarda la tokenizacion y el tag 
        documents.append((word_list, intent["tag"]))
        if intent["tag"] not in classes:
            # en en el arreglo no existe el tag se le agrega en caso de existir se agrega solo el texto no el tag
            classes.append(intent["tag"])

# words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
# Convierte palabras a su forma base o raíz perros perro y eliminamos las repetidas
words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore_letters]
words = sorted(set(words))

pickle.dump(words, open('models/words.pkl', 'wb'))
pickle.dump(classes, open('models/classes.pkl', 'wb'))

# Prepara los datos para el entrenamiento
training = []
output_empty = [0] * len(classes)
# recorremos el guardado de tokenizacion
for document in documents:
    bag = []
    # tomamos todas las palabras de ese tag
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    # tomamos todas las palabtas y las comparamos con las primeras palabras si coinciden 
    # se cambia a 1 en caso contraro queda en 0
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
    # creamos una copia de outputempty para las modificaciones
    output_row = list(output_empty)
    # aqui dicha copia buscaremos todas los tags correpondientos y buscaremos
    # cual coincide con el tag de turno y cuando le encuentre en el espacio 
    # correspondiente del index le agrega un 1, se asegura de que solo el índice correspondiente al tag actual sea 1
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])
    
random.shuffle(training)

train_x = []
train_y = []
for i in training:
    train_x.append(i[0])
    train_y.append(i[1])

train_x = np.array(train_x)
train_y = np.array(train_y)

# Crear la red neuronal
# inicializamos las capas de entrada  salida
model = Sequential()
# aprende combinaciones de palabras , aprenderemos representaciones útiles y complejas
model.add(Dense(256, input_shape=(len(train_x[0]),), activation='relu'))
# evitamos sobrecarga con 50%
model.add(Dropout(0.5))
# la segunda capa es menos densa capta palabras mas robustas
model.add(Dense(64, activation='relu'))
# la segunda capa es menos densa capta palabras mas robustas
model.add(Dropout(0.5))
# proporcionar una predicción final en términos de probabilidades
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compilar y entrenar el modelo
# un valor más bajo hace que el aprendizaje sea más lento pero más estable.
# reducir gradualmente la tasa de aprendizaje durante el entrenamiento
# acelerar el entrenamiento y a suavizar el proceso de optimización.
# ajuste más preciso en las actualizaciones de los peso
sgd = SGD(learning_rate=0.001, decay=1e-6, momentum=0.9, nesterov=True)
#  Calcula la diferencia entre las probabilidades predichas y las verdaderas usando la entropía cruzada
# El optimizador ajusta los pesos de la red neuronal durante el entrenamiento
# porcentaje de predicciones correctas realizadas por el modelo
# evalua como fue el entrenamiento
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
# entrenamos con los datos 100 veces
# divide los lotes en 5 
model.fit(train_x, train_y, epochs=100, batch_size=5, verbose=1)

model.save('models/chatbot_model.h5')
