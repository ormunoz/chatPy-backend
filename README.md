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


<div id='id4' />

---

## 4. Levantamiento: 📝

## Pasos para el levantamiento del proyecto:

✳️ Levantar el servidor FastAPI utilizando Uvicorn::

➡️ Asegúrate de tener un archivo main.py dentro de una carpeta llamada app (es decir, app/main.py). Luego, ejecuta el siguiente comando para levantar el servidor:


  ```
        uvicorn app.main:app --host 127.0.0.1 --port 3000 --reload
  ```

Nota📝: Esto levantará el proyecto en http://localhost:3000.


<div id='id5' />

---

## 5. Postman: 📝

## Probar el endpoint del chat usando Postman:

✳️ Levantar el servidor FastAPI utilizando Uvicorn::

➡️ Realiza una solicitud POST al servicio de chat en la URL http://localhost:3000/chat con un JSON en el cuerpo de la solicitud. Ejemplo:

  ```
        {
          "message": "Hola"
        }
  ```

Nota📝: El chatbot responderá según su capacidad de procesamiento neuronal (basado en el modelo que hayas implementado).

