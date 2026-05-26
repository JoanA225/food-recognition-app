from flask import Flask, request
from PIL import Image
import google.generativeai as genai
import os

app = Flask(__name__)

# API KEY GEMINI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/food', methods=['POST'])
def detect_food():

    if 'image' not in request.files:
        return {"food": "No image"}

    image = Image.open(request.files['image'])

    response = model.generate_content([
        "Dime SOLO el nombre del alimento en español. Solo una palabra.",
        image
    ])

    return {"food": response.text.strip()}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)