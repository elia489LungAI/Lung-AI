import streamlit as st

st.title("🌍 Global AI Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Write to me in any language... / اكتب لي بأي لغة..."):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Intelligent response logic
    with st.chat_message("assistant"):
        # هنا المساعد يرد حسب اللغة التي استخدمتها
        response = f"I understand you! You said: '{prompt}'. I am now able to process multiple languages."
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
