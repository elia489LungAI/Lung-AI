import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Lung AI", page_icon="🤖")

genai.configure(api_key=["AQ.Ab8RN6LzyCUukA9Mo5ImvQ0xXEHDhSqfL2MCDwpJ52wghlG09w"])

model = genai.GenerativeModel("gemini-1.5-flash-8b")

st.title("🤖 Lung AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

system_prompt = """
You are Lung AI, a smart and helpful AI assistant.

Rules:
- Answer naturally like ChatGPT or Gemini.
- Answer in the same language as the user.
- Do not repeat yourself.
- Keep the conversation context.
- Think carefully before answering.
- Give clear, useful, and accurate answers.
- If the user asks for code, provide complete working code.
- If you are not sure, say that honestly.
"""

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Write to me in any language..."):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    conversation = system_prompt + "\n\n"

    for msg in st.session_state.messages[-4:]:
        conversation += f"{msg['role']}: {msg['content']}\n"

    conversation += "assistant:"

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(conversation)

                if response and response.text:
                    answer = response.text
                else:
                    answer = "I could not generate a response. Please try again."

            except Exception as e:
                answer = f"Error: {e}"

            st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
