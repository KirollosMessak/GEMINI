from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
from PIL import Image
import google.generativeai as genai

genai.configure (api_key = os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input,image,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,image,prompt])
    return response.text


def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        return[ {
            'mime_type': uploaded_file.type,
            'data': bytes_data
        }
        ]
    else:
        raise FileNotFoundError('No file uploaded')

#initialize streamlit

input = st.text_input('Input Prompt', key = 'input')
uploaded_file = st.file_uploader('Upload Image', type = ['jpg', 'jpeg', 'png'])
image = ""
if uploaded_file is not None:
    image = Image.open (uploaded_file)
    st.image(image , caption ='uploaded_image', use_column_width = True)

submit = st.button ('Invoice here')

input_prompt = """ you are an expert in understanding invoices. You will recieve input images as invoices .. 
you will have to answer questions based on the input image."""

# if submit button clicked

if submit: 
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)

    st.subheader('The Response is')
    st.write(response)