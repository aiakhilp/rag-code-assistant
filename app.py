import streamlit as st
from agent import CodeAssistantAgent

st.set_page_config(page_title="RAG Code Assistant")
st.title("RAG-Powered Code Assistant")

if 'agent' not in st.session_state:
    st.session_state['agent'] = CodeAssistantAgent()
if 'history' not in st.session_state:
    st.session_state['history'] = []

# Chat history
for msg in st.session_state['history']:
    st.markdown(f"**{msg['role'].capitalize()}:** {msg['content']}")

user_input = st.text_area("Ask your coding question here:", height=80)

if st.button("Send"):
    agent = st.session_state['agent']
    response = agent.handle(user_input)
    st.session_state['history'].append({'role': 'user', 'content': user_input})
    st.session_state['history'].append({'role': 'assistant', 'content': response})
    st.rerun()

