import nltk
from nltk.stem import WordNetLemmatizer
from unidecode import unidecode
from .models import words
import numpy as np

lemmatizer = WordNetLemmatizer()

#  limpiar y normalizar la oración
def clean_up_sentence(sentence):
    # elimina los acentos y otros caracteres diacríticos
    sentence = unidecode(sentence.lower())
    # tokenizamos la frase
    sentence_words = nltk.word_tokenize(sentence)
    # reducimos la palabra en su forma base
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        if w in words:
            bag[words.index(w)] = 1
    return np.array(bag)
