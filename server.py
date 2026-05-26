from flask import Flask, request
from PIL import Image
import google.generativeai as genai
import os

app = Flask(__name__)

# Configurar Gemini usando la API Key de Render
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Modelo Gemini
model = genai.GenerativeModel("gemini-1.5-flash")


@app.route('/food', methods=['POST'])
def detect_food():

    # Comprobar si llegó algún archivo
    if len(request.files) == 0:
        return {"food": "No image"}

    # Coger el primer archivo recibido
    uploaded_file = list(request.files.values())[0]

    # Abrir imagen
    image = Image.open(uploaded_file)

    # Preguntar a Gemini
    response = model.generate_content([
        "Dime SOLO el nombre del alimento en español. Solo una palabra.",
        image
    ])

    # Limpiar respuesta
    food_name = response.text.strip()

    return {"food": food_name}


@app.route('/')
def home():
    return "Servidor Food IA funcionando"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)