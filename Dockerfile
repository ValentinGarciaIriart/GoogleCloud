# Usa una imagen de Python como base
FROM python:3.9-alpine3.20

# Establece el directorio de trabajo en /app
WORKDIR /app

# Instala las dependencias
RUN pip install flask 

# Copia la aplicación y los archivos HTML al contenedor
COPY app.py .
COPY templates/ templates/

# Expone el puerto 5000 para acceder a la aplicación Flask
EXPOSE 5000

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["python", "app.py"]
