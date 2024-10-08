from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from chatbot import predict_class, get_response
from fastapi.responses import JSONResponse
import ftfy
import nltk
from nltk.stem import WordNetLemmatizer

app = FastAPI()
nltk.data.find('tokenizers/punkt')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')

# Configurar CORS
origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "https://chat-py-pi.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de solicitud
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    intent = predict_class(request.message)
    if intent:
        response_text = get_response(intent)
        status_code = 200
    else:
        response_text = "Lo siento, no entiendo tu pregunta."
        status_code = 400
    response_text = ftfy.fix_text(response_text)
    
    return JSONResponse(content={"data": {"status": status_code, "chatBotText": response_text}}, status_code=status_code)
