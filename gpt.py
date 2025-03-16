import google.generativeai as genai
import os

# Set up the Gemini API key
genai.configure(api_key="AIzaSyDZQlyK7T57T5SyGibY--uSL7XOUwI2paU")

def get_summarise(system, text):
    model = genai.GenerativeModel("gemini-2.0-flash")
    contents = [
        {"role": "user", "parts": [f"{system} Topic: {text}"]},
    ]
    response = model.generate_content(contents)
    return response.text

