Instalacion para usarlo de manera local

Pasos

1_ En la raiz del proyecto ejecutar "python -m venv venv"
  nota: venv sera nuestro entorno virtual para hacer las instalaciones de dependencias

2_ Entraremos a dicho entorno  para windows es ".\venv\Scripts\Activate" para mac "source venv/bin/activate"

3_luego ejecutaremos los paquetes necesarios predefinidos en requirements 
"pip install -r requirements.txt "

4_luego ejecutaremos "python -m uvicorn app.main:app --host 127.0.0.1 --port 3000 --reload"
esto levantara el proyecto en [http://localhos:3000] 

5_En postman o tu aplicacion web llamareemos al servicio para hablar con el chat 
http://localhos:3000/chat

y se le debe enviar un json en el body, ejemplo : 
{
  "message": "quiero aprobar el curso"
}

6_ chat respondera segun sus limitaciones neuronales