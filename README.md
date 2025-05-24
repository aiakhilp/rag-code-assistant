RAG Code Assistant

    An AI-powered code assistant that grounds answers in real documentation using RAG (Retrieval-Augmented Generation).
    Sample data and embeddings are included—you can start immediately!

Features

    Natural Language Understanding: Ask questions in plain English.

    Code Generation & Retrieval: Get code snippets and examples—generated or pulled from real docs.

    RAG-powered Doc Search: Answers are grounded in official/sample documentation via embeddings.

    Debugging Assistance: Paste buggy code to get explanations and fixes.

    Context Awareness: Multi-turn, conversational support—follow up on previous queries.

    Traditional + AI Methods: Combines classic techniques (regex, AST, FAISS) with modern AI (embeddings, GPT).

    Ready-to-Run: Comes with sample data and embeddings. No setup needed to try it out!

Project Structure

rag-code-assistant/
│
├── app.py               # Streamlit web app
├── agent.py             # Main agent logic
├── retriever.py         # RAG (retriever & embedding) logic
├── context.py           # Context manager
├── utils.py             # Utilities (intent detection, etc.)
├── requirements.txt
├── README.md
│
├── data/                # Sample documentation (e.g. quickstart.html)
├── embeddings/          # Prebuilt vector index and metadata (e.g. .pkl, .index)

Quick Start (with Sample Data & Embeddings)

    git clone https://github.com/<yourusername>/rag-code-assistant.git
    cd rag-code-assistant
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt




    


Set your OpenAI API Key

export OPENAI_API_KEY="sk-..."  # Your OpenAI key

Run the Assistant

    streamlit run app.py

    That’s it!

        The app opens in your browser.

        You can immediately start asking questions—no need to preprocess docs or build embeddings.

How to Use

    Ask for code examples:
    “Show me an example of a GET request with requests”

    Get explanations:
    “How do I send query parameters?”

    Debug your code:
    Paste buggy code and ask: “Fix this code”

    Follow up:
    “Now make it print only even numbers”

    Multi-turn:
    The assistant remembers your queries and context.

How It Works

    Documentation (in /data) is broken into text chunks and embedded using OpenAI embeddings.

    Embeddings (in /embeddings) are indexed with FAISS for fast, semantic similarity search.

    On your question:
    The assistant retrieves relevant doc chunks using RAG and augments the prompt sent to GPT, improving factuality and reliability.

    Intent classification and static code checks are handled with lightweight, traditional Python methods for speed and accuracy.

Adding Your Own Documentation

If you want to use your own docs or expand the knowledge base:

    Save your documentation as .html, .txt, or .md in the /data/ directory.

        Example: data/flask_docs.html

    Edit retriever.py

        Change the doc_path variable (or extend to use multiple docs).

        Example:

    doc_path = "data/flask_docs.html"

Rebuild Embeddings & Index

python retriever.py

    This processes your new docs and saves fresh embeddings and FAISS index in /embeddings.

Restart the Assistant

    streamlit run app.py

        Now your assistant will use your custom documentation for RAG-powered answers.

Troubleshooting

    Assistant not using new docs?

        Double-check your doc file and doc_path in retriever.py.

        Make sure you re-ran python retriever.py.

        Restart the Streamlit app.

    App won’t start?

        Ensure your virtual environment is activated and dependencies are installed.

        Make sure you’ve set your OpenAI API key.

    Slow or generic answers?

        For best performance, use reasonably sized documentation.

        Phrase your questions clearly, as they might appear in documentation.

Extending & Customizing

    Add more documentation files and adjust chunking for larger docs.

    Enhance the UI to show retrieved doc chunks.

    Integrate other LLMs or embedding providers.

    Add support for more programming languages or frameworks.

Sample Queries for Demo

    “Show me an example of making a POST request with requests.”

    “How do I upload a file with requests?”

    “Write a function to check if a string is a palindrome.”

    “Fix this code: for i in range(5 print(i)”

Contributing & Support

    Pull requests welcome!

    For issues or questions, open an issue on this repo.
