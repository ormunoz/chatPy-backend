import random
import numpy as np
from keras.models import load_model
from .models import words, classes, intents, lemmatizer
from .utils import bag_of_words

# Cargar el modelo entrenado
try:
    model = load_model('models/chatbot_model.h5')
except Exception as e:
    print("Error al cargar el modelo:", e)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    # probabilidades
    res = model.predict(np.array([bow]))[0]
    if np.sum(res) != 0:
        res = res / np.sum(res)
    threshold = 0.1
    results = [(i, r) for i, r in enumerate(res) if r > threshold]
    results.sort(key=lambda x: x[1], reverse=True)
    if results:
        predicted_class = classes[results[0][0]]
        return predicted_class
    else:
        return "No hay una intención clara."


def get_response(tag):
    list_of_intents = intents['intents']
    for intent in list_of_intents:
        if intent["tag"] == tag:
            response = random.choice(intent['responses'])
            return response
    return "Lo siento, no entendí tu pregunta. ¿Podrías reformularla o contactarnos para más ayuda?"
