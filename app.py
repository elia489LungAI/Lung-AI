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
            system_prompt = """
You are Lung AI, a highly intelligent AI assistant.

Your behavior:
- Answer naturally like ChatGPT.
- Think carefully before responding.
- Never repeat yourself unnecessarily.
- Give detailed, accurate, and helpful answers.
- Keep the conversation context.
- Answer in the same language as the user.
- Be friendly and professional.
- If asked to write code, always provide complete working code.
- If you don't know something, say so honestly instead of guessing.
"""

conversation = system_prompt + "\n\n"

for msg in st.session_state.messages[-10:]:
    conversation += f"{msg['role']}: {msg['content']}\n"

conversation += f"user: {prompt}\nassistant:"

response = model.generate_content(conversation)
answer = response.text
            answer = response.text
        except Exception as e:
            answer = "صار خطأ بالاتصال. تأكدي من API Key واسم الموديل داخل Streamlit Secrets."

        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
