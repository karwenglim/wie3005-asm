# pages/AI_Assistant.py
import streamlit as st
import ollama

def generate_response():
        response = ollama.chat(model='llama3', stream=True, messages=st.session_state.messages)
        for partial_resp in response:
            token = partial_resp["message"]["content"]
            st.session_state["full_message"] += token
            yield token

def run_ai_assistant():
    st.title("🤖 Assistant")

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "ai", "content": "Hi! How can I help you today?"}]

    # for msg in st.session_state.messages:
    #     if msg["role"] == "user":
    #         st.chat_message(msg["role"], avatar="🧑‍💻").write(msg["content"])
    #     else:
    #         st.chat_message(msg["role"], avatar="🤖").write(msg["content"])

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"""
            <div style='display: flex; justify-content: flex-end;'>
                <div style='background-color: #DCF8C6; padding: 8px 12px; border-radius: 10px; max-width: 70%; margin: 4px 0;'>
                    {msg["content"]}
                </div>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.chat_message("ai", avatar="🤖").write(msg["content"])

    
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        # st.chat_message("user", avatar="🧑‍💻").write(prompt)
        st.markdown(f"""
            <div style='display: flex; justify-content: flex-end;'>
                <div style='background-color: #DCF8C6; padding: 8px 12px; border-radius: 10px; max-width: 70%; margin: 4px 0;'>
                    {prompt}
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.session_state["full_message"] = ""
        st.chat_message("ai", avatar="🤖").write_stream(generate_response)
        st.session_state.messages.append({"role": "ai", "content": st.session_state["full_message"]})

if __name__ == "__main__":
    run_ai_assistant()

