import streamlit as st
import google.generativeai as genai

# قراءة المفتاح من الـ Secrets
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=["AQ.Ab8RN6LzyCUukA9Mo5ImvQ0xXEHDhSqfL2MCDwpJ52wghlG09w"])
    model = genai.GenerativeModel('flash-lite 3.1')
    
    st.title("Lung AI")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask me anything..."):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
else:
    st.error("API Key not found! Please add GOOGLE_API_KEY to your Streamlit Secrets.")
