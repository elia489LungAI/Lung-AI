import streamlit as st
import google.generativeai as genai

genai.configure(api_key=["AQ.Ab8RN6LzyCUukA9Mo5ImvQ0xXEHDhSqfL2MCDwpJ52wghlG09w"])

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("Lung AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("اسال Lung Ai"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            answer = response.text
        except Exception as e:
            answer = "صار خطأ بالاتصال. تأكدي من API Key واسم الموديل داخل Streamlit Secrets."

        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
