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
for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
    output_row = list(output_empty)
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
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compilar y entrenar el modelo
sgd = SGD(learning_rate=0.001, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

model.fit(train_x, train_y, epochs=100, batch_size=5, verbose=1)

model.save('models/chatbot_model.h5')
