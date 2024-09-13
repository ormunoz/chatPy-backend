# Usa una imagen base ligera de Python
FROM python:3.12.1

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de dependencias
COPY requirements.txt . 

# Instala las dependencias
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación
COPY app /app

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Define el comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
