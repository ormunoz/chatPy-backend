import json
import pickle
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# Cargar datos y modelos
intents = json.loads(open('app/intents.json').read())
words = pickle.load(open('app/models/words.pkl', 'rb'))
classes = pickle.load(open('app/models/classes.pkl', 'rb'))
