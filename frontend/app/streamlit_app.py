import os
import requests
import streamlit as st


BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")


st.set_page_config(
    page_title="Ask Kinkini | Portfolio Assistant",
    page_icon="🤖",
    layout="centered"
)


st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 34px;
    font-weight: bold;
    color: #f8fafc;
}

.subtitle {
    text-align: center;
    font-size: 17px;
    color: #cbd5e1;
}

.cta-box {
    background-color: #1e293b;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #f59e0b;
    color: #f8fafc;
    margin-top: 10px;
}

.cta-box h3 {
    color: #fbbf24;
}

.cta-box p {
    color: #e2e8f0;
}

.stButton > button {
    border-radius: 8px;
    border: 1px solid #475569;
    background-color: #111827;
    color: #f8fafc;
}

.stButton > button:hover {
    border-color: #f59e0b;
    color: #fbbf24;
}
</style>
""", unsafe_allow_html=True)


def ask_backend(question: str) -> str:
    """
    Sends user question to FastAPI backend.
    """

    try:
        response = requests.post(
            f"{BACKEND_URL}/chat",
            json={"message": question},
            timeout=10
        )

        response.raise_for_status()
        data = response.json()

        return data.get("response", "Sorry, I could not understand the response from backend.")

    except requests.exceptions.RequestException:
        return """
Backend is not reachable right now.

Please make sure Docker is running and the backend service is active.
"""


def is_conversation_ending(user_message: str) -> bool:
    """
    Detects when the user is done with the conversation.
    """

    ending_words = [
        "no",
        "nope",
        "nothing",
        "that's all",
        "thats all",
        "done",
        "not now",
        "no thanks",
        "thank you",
        "thanks",
        "bye",
        "exit"
    ]

    cleaned_message = user_message.lower().strip()

    return cleaned_message in ending_words


def add_follow_up(answer: str) -> str:
    """
    Adds follow-up question after every normal bot answer.
    """

    return f"""{answer}

---

Is there anything else I can help you with?"""


def show_cta_message() -> str:
    """
    CTA message shown only when user ends the conversation.
    """

    return """
Thank you for chatting with Ask Kinkini.

### Want this chatbot for yourself?

I can create a similar personal or business FAQ assistant for freelancers, coaches, consultants, small businesses, and education institutes.

Use it to answer common questions, explain your services, collect leads, and share your work through one simple link.
"""


st.markdown('<div class="main-title">Ask Kinkini 🤖</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">A personal portfolio assistant that answers questions about my skills, projects, services, and contact details.</div>',
    unsafe_allow_html=True
)

st.write("---")


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! I am Ask Kinkini. You can ask me about Kinkini's skills, projects, services, pricing, or contact details."
        }
    ]

if "conversation_ended" not in st.session_state:
    st.session_state.conversation_ended = False


st.subheader("Suggested Questions")

suggested_questions = [
    "Who are you?",
    "What is your work experience?",
    "What services do you offer?",
    "What are your skills?",
    "Show your projects",
    "Can you make a Power BI dashboard?",
    "Can you clean Excel data?",
    "Can you make a chatbot?",
    "What is your pricing?",
    "How can I contact you?"
]

cols = st.columns(2)

for index, question in enumerate(suggested_questions):
    with cols[index % 2]:
        if st.button(question, key=f"suggested_{index}"):
            answer = ask_backend(question)
            final_answer = add_follow_up(answer)

            st.session_state.messages.append({
                "role": "user",
                "content": question
            })

            st.session_state.messages.append({
                "role": "assistant",
                "content": final_answer
            })

            st.rerun()


st.write("---")
st.subheader("Chat")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


user_question = st.chat_input("Ask something about Kinkini...")

if user_question:
    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    if is_conversation_ending(user_question):
        st.session_state.messages.append({
            "role": "assistant",
            "content": show_cta_message()
        })

        st.session_state.conversation_ended = True

    else:
        answer = ask_backend(user_question)
        final_answer = add_follow_up(answer)

        st.session_state.messages.append({
            "role": "assistant",
            "content": final_answer
        })

    st.rerun()