import streamlit as st
from chatbot.chatbot_engine import get_response


# Page settings
st.set_page_config(
    page_title="Synora AI",
    page_icon="S",
    layout="wide"
)

# Custom Styling
st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
}

.stApp {
    background-color: #050816;
    color: white;
}

.block-container {
    max-width: 820px;
    padding-top: 2rem;
}

h1, h2, h3, h4 {
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

[data-testid="stChatMessage"] {
    background-color: #111827;
    border-radius: 18px;
    padding: 14px;
    margin-bottom: 15px;
    border: 1px solid rgba(255,255,255,0.05);
}

.stChatInput {
    padding-bottom: 20px;
    position: sticky;
    bottom: 15px;
    background-color: #050816;
    padding-top: 10px;
}

.stChatInput input {
    border-radius: 15px !important;
    background-color: #111827 !important;
    color: white !important;
    border: 1px solid #374151 !important;
}

</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:

    st.title("Synora AI")

    st.markdown("---")

    st.markdown("### Customer Support")

    st.markdown("""
Need help with your orders, refunds, payments, or shipping?

Our AI assistant is here to help you 24/7.
""")

    st.markdown("---")

    st.markdown("### Quick Help")

    st.markdown("""
- Track Orders
- Refund Status
- Cancel Orders
- Payment Issues
- Delivery Support
""")

# Hero Welcome Section
st.markdown("""
<div style='text-align: center; padding-top: 0px; padding-bottom: 25px;'>

<h1 style='font-size: 60px; margin-bottom: 5px; font-weight: 700;'>
Synora AI
</h1>

<h3 style='color: #cbd5e1; font-weight: 500;'>
Customer Support Assistant
</h3>

</div>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask your question...")

# If user sends message
if user_input:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Display current user message immediately
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get AI response
    response = get_response(user_input)

    bot_answer = response["answer"]

    final_response = f"""
{bot_answer}
"""

    # Display bot response
    with st.chat_message("assistant"):

        with st.spinner("Synora AI is typing..."):

            import time

            message_placeholder = st.empty()
            full_response = ""

            for word in final_response.split():
                full_response += word + " "
                time.sleep(0.03)
                message_placeholder.markdown(full_response)

    # Save bot response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": final_response
        }
    )