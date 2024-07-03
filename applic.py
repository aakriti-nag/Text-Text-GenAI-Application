from dotenv import load_dotenv
load_dotenv()  # to load all environment variables

import streamlit as st
import os
import google.generativeai as genai

# Configure the generative AI model
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Load Gemini Pro model
model = genai.GenerativeModel('gemini-pro')

def get_response(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

# Initialize Streamlit app
st.set_page_config(page_title='Gemini LLM App', layout='wide')
st.title('Gemini LLM Application')

# Input section
input = st.text_input('Ask a question:', key='input')
submit = st.button('Submit')

if submit:
    if input:
        with st.spinner('Generating responses...'):
            response = get_response(input)
            st.subheader("The response is:")
            st.write(response)
    else:
        st.error('Please enter a question.')

# Sidebar
st.sidebar.header("About")
st.sidebar.info("This application uses Generative AI to answer questions. Enter your question in the input box and click 'Submit' to get a response.")