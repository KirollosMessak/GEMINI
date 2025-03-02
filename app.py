from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
from PIL import Image
import google.generativeai as genai

genai.configure (api_key = os.getenv('google_api_key'))

def gemini_response (input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text