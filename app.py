import streamlit as st
import google.generativeai as genai

# 1. Setup API (Replace YOUR_API_KEY_HERE with your real key)
genai.configure(API_Key="AQ.Ab8RN6LtMOldqP5sA2-tCYRZjztXNaopnSLq43LstaFKGGZxDg")
model = genai.GenerativeModel('gemini-pro')

st.title("🌍 Global AI Assistant")

# 2. Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Display history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Chat logic
if prompt := st.chat_input("Write to me in any language..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        # This is where the AI responds with real intelligence
        response = model.generate_content(prompt)
        st.markdown(response.text)
    
    st.session_state.messages.append({"role": "assistant", "content": response.text})
