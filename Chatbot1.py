#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import google.generativeai as genai

# API key (hardcoded)
API_KEY = "AIzaSyBsq5Kd5nJgx2fejR77NT8v5Lk3PK4gbH8"

# Configure the generative model
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-flash')

# Initialize chat session
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Streamlit app title
st.title("🤖 Chatbot - Your AI Assistant")

# Initialize messages in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Say something..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get chatbot response
    response = st.session_state.chat.send_message(prompt)

    # Add chatbot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    with st.chat_message("assistant"):
        st.markdown(response.text)
