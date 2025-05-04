# pages/AI_Assistant.py
import streamlit as st

def run_ai_assistant():
    st.title("AI Assistant")
    user_input = st.text_input("Ask me anything:", "")
    
    if user_input:
        # Here you could integrate your AI logic or model
        response = f"I received your question: {user_input}. Here's your answer."
        st.write(response)

if __name__ == "__main__":
    run_ai_assistant()
