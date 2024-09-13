<div align='center'>
  <h1>Documentación para utilizar chat bot en Python</h1>
  <h2>ChatBot Python</h2>
</div>

## [ÍNDICE](#indice)
1. [Instalación](#id1)
2. [Entorno Desarrollo](#id2)
3. [Entorno virtual](#id3)
4. [Dependencias](#id4)
5. [Levantamiento](#id5)
6. [Postman](#id6)
7. [Entrenamiento](#id7)


<div id='id1' />

---
## 1. Recomendaciones de Instalación 📝

## Programas Necesarios

- **`Python Version`**: 3.12.0
- **`pip`**: 24.2
- **`Postman`**: Sirve Cualquier version.

✳️ En caso de no tener Python instalado:

  - **`https://python.org/downloads`**: Descarga e instala Python.
    - Haz clic en el botón de descarga para la última versión de Python. 

  - **Ejecutar el instalador**:
    - Una vez descargado, abre el instalador.
      Importante: Marca la casilla que dice "Add Python to PATH". Esto configurará automáticamente la variable de entorno PATH y facilitará el uso de Python desde la línea de comandos.

  - **Actualizar `pip`** (opcional pero recomendado):
  ```
        python -m pip install --upgrade pip
  ```

<div id='id2' />
---

## 2. Instalacion de Entorno Desarrollo 📝

## Pasos de Instalación para un Proyecto de Chat IA con Python y FastAPI

✳️Crear un entorno virtual en la raíz del proyecto:
  
  ➡️ Para Windows:

  ```
        python -m venv venv
  ```

  📝 Nota: venv será nuestro entorno virtual para manejar las dependencias.


<div id='id3' />
---

## 3. Activar el entorno virtual: 📝

## Pasos de Instalación la activación del entorno virtual

✳️Activando un entorno virtual:
  
➡️En la raíz del proyecto ejecutamos lo siguiente

➡️ Para Windows:

  ```
        .\venv\Scripts\Activate
  ```

➡️ Para macOS/Linux:

  ```
        source venv/bin/activate
  ```

<div id='id4' />

---

## 4. Instalacion de Dependencias: 📝

## Pasos de Instalación de dependencias:

✳️ Instalar las dependencias necesarias desde el archivo requirements.txt:

➡️ Asegúrate de tener un archivo requirements.txt en la raíz del proyecto con las dependencias necesarias. Luego ejecuta:


  ```
        pip install -r requirements.txt
  ```
Nota📝: Estas son dependencias solo para el uso de chatIa si quiere cambiar el codigo y
  dependencias se deberan instalar en su entorno.

<div id='id5' />

---

## 5. Levantamiento: 📝

## Pasos para el levantamiento del proyecto:

✳️ Levantar el servidor FastAPI utilizando Uvicorn::

➡️ Asegúrate de tener un archivo main.py dentro de una carpeta llamada app (es decir, app/main.py). Luego, ejecuta el siguiente comando para levantar el servidor:


  ```
        uvicorn app.main:app --host 127.0.0.1 --port 3000 --reload
  ```

Nota📝: Esto levantará el proyecto en http://localhost:3000.


<div id='id6' />

---

## 6. Postman: 📝

## Probar el endpoint del chat usando Postman:

✳️ Levantar el servidor FastAPI utilizando Uvicorn::

➡️ Realiza una solicitud POST al servicio de chat en la URL http://localhost:3000/chat con un JSON en el cuerpo de la solicitud. Ejemplo:

  ```
        {
          "message": "Hola"
        }
  ```

Nota📝: El chatbot responderá según su capacidad de procesamiento neuronal (basado en el modelo que hayas implementado).

<div id='id7' />

---

## 7. Entrenamiento: 📝

## Paso a Paso para Entrenar un Chatbot de IA:

✳️ Crear el Archivo intents.json: Este archivo es crucial para el entrenamiento de tu chatbot. En él, defines las diferentes intenciones que tu chatbot debe reconocer y las respuestas que debe proporcionar. Cada intención contiene:


- **`Tag (Etiqueta):`**: Un identificador único para la intención.
- **`Patterns (Patrones):`**: Ejemplos de frases o textos que los usuarios podrían escribir para expresar esa intención.
- **`Responses (Respuestas):`**: Las respuestas que el chatbot puede dar cuando detecta esa intención.
A continuación, se muestra un ejemplo de cómo podría verse una sección de tu archivo intents.json:

  ```
        {
          {
            "intents": [
              {
                "tag": "saludo",
                "patterns": [
                  "Hola",
                  "¿Qué tal?",
                  "Buenos días",
                  "Hola, ¿cómo estás?",
                  "Hey"
                ],
                "responses": [
                  "¡Hola! ¿En qué puedo ayudarte hoy?",
                  "¡Buenos días! ¿Cómo puedo asistirte?",
                  "¡Hola! ¿Qué tal?"
                ]
              }
            ]
          }
        }
  ```


✳️ Definir las Intenciones y Patrones:

➡️ Para cada intención (tag), debes definir diferentes patrones que representen las maneras en las que un usuario podría expresar esa intención. Por ejemplo, para la intención "saludo", los patrones pueden incluir variaciones como "Hola", "¿Qué tal?", "Buenos días", etc.

Nota📝: Asegúrate de cubrir varias formas en las que las personas pueden formular preguntas o solicitudes para cada intención. Cuantos más patrones tengas, más preciso será tu chatbot para identificar la intención del usuario.


✳️ Definir las Respuestas:

➡️ Para cada intención, debes proporcionar una lista de respuestas que el chatbot puede usar cuando detecta esa intención.
Estas respuestas deben ser variadas para que el chatbot no suene repetitivo. Por ejemplo, en el caso de la intención "saludo", puedes incluir respuestas como "¡Hola! ¿En qué puedo ayudarte hoy?", "¡Buenos días! ¿Cómo puedo asistirte?", etc.

Nota📝: Agregar Más Intenciones al Archivo intents.json: Puedes añadir tantas intenciones como desees. Aquí tienes algunos ejemplos adicionales:

  ```
        {
          "intents": [
            {
              "tag": "despedida",
              "patterns": [
                "Adiós",
                "Hasta luego",
                "Nos vemos",
                "Chao",
                "Que tengas un buen día"
              ],
              "responses": [
                "¡Adiós! Que tengas un buen día.",
                "Hasta luego. ¡Cuídate!",
                "Nos vemos pronto."
              ]
            },
            {
              "tag": "gracias",
              "patterns": [
                "Gracias",
                "Muchas gracias",
                "Te lo agradezco",
                "¡Gracias!"
              ],
              "responses": [
                "¡De nada! Estoy aquí para ayudar.",
                "No hay de qué. ¡Siempre dispuesto a ayudar!",
                "¡Gracias a ti!"
              ]
            }
          ]
        }
  ```

✳️ Ejecución del Entrenamiento:

➡️ Para entrenar el chatbot utilizando las intenciones definidas, solo necesitas ejecutar el archivo de entrenamiento desde la raíz del proyecto o desde el entorno virtual que hayas creado.
  ```
      python training.py 
  ```

➡️ Esto iniciará el proceso de entrenamiento del chatbot basado en los datos que has configurado en el archivo intents.json. Una vez finalizado, el modelo estará listo para reconocer las intenciones y proporcionar las respuestas correspondientes.