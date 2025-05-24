import os
from openai import OpenAI
from retriever import load_retriever, search_chunks
from context import ContextManager
from utils import classify_intent, static_syntax_check

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
# Load FAISS index and doc chunks
index, doc_chunks = load_retriever(
    "embeddings/quickstart.index",
    "embeddings/quickstart.pkl"
)

class CodeAssistantAgent:
    def __init__(self):
        self.context = ContextManager()

    def handle(self, user_input):
        self.context.add('user', user_input)
        intent = classify_intent(user_input)
        if intent == 'generate':
            reply = self._generate_code(user_input)
        elif intent == 'retrieve':
            reply = self._retrieve_with_rag(user_input)
        elif intent == 'debug':
            reply = self._debug_code(user_input)
        else:
            reply = self._general(user_input)
        self.context.add('assistant', reply)
        return reply

    def _generate_code(self, prompt):
        messages = self.context.get() + [
            {"role": "system", "content": "Generate code for the user's request."}
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message.content

    def _retrieve_with_rag(self, prompt):
        retrieved_chunks = search_chunks(prompt, index, doc_chunks, client, k=4)
        context = "\n\n".join(retrieved_chunks)
        messages = [
            {"role": "system", "content": f"You are a coding assistant. Here are relevant docs:\n{context}"},
            {"role": "user", "content": prompt}
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        # Optionally: return context along with the answer for demo/debug
        return f"**[Doc Chunks Used in RAG]**\n```\n{context}\n```\n\n**[LLM Answer]**\n{response.choices[0].message.content}"

    def _debug_code(self, prompt):
        import re
        code = re.search(r"```(.*?)```", prompt, re.DOTALL)
        code = code.group(1) if code else prompt
        static_result = static_syntax_check(code)
        messages = self.context.get() + [
            {"role": "system", "content": "Debug and improve this code."},
            {"role": "user", "content": code}
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        llm_result = response.choices[0].message.content
        return f"{static_result}\n\nAI Debugging:\n{llm_result}"

    def _general(self, prompt):
        messages = self.context.get() + [
            {"role": "system", "content": "Assist with the user's coding question."}
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message.content

