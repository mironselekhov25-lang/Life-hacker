import streamlit as st

st.set_page_config(page_title="My Chatbot", page_icon="🤖")

st.title("🤖 My First Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.c_
