import streamlit as st
import google.generativeai as genai


st.title("Welcome to my AI Chatbot!")


genai.configure(api_key="AIzaSyDRqyPNqAkxCPISsNSuWqAgXK6MyvZKqLU")

text = st.text_input("Enter your question:")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Click Me"):
    response = chat.send_message(text)
    st.write(response.text)