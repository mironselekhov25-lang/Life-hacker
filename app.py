import streamlit as st
import random

st.set_page_config(page_title="Life Hacker Bot", page_icon="🤖")

st.title("🤖 Life Hacker Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Simple response logic (no API)
def get_bot_response(user_input):
    user_input = user_input.lower()

    if "study" in user_input:
        return "📚 Try the Pomodoro technique: 25 minutes study, 5 minutes break!"
    elif "sleep" in user_input:
        return "😴 Avoid screens 1 hour before bed."
    elif "focus" in user_input:
        return "🎧 Use noise-cancelling headphones or white noise."
    elif "hello" in user_input:
        return "Hi! How can I help you improve your life today?"
    else:
        responses = [
            "That's interesting! Tell me more.",
            "Try setting small daily goals.",
            "Consistency is key!",
            "Break big tasks into smaller steps."
        ]
        return random.choice(responses)

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask me for life hacks...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate bot response
    bot_response = get_bot_response(user_input)

    # Show bot message
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)
