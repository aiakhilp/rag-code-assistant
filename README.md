RAG Code Assistant is an AI-powered, documentation-aware coding helper that answers your programming questions, finds real code examples from documentation, debugs code, and remembers the context of your conversation.
It uses RAG (Retrieval-Augmented Generation) technology: when you ask a question, it looks up relevant info in your documentation and brings that knowledge into its answer.
Features at a Glance

    Ask Anything: Write questions in plain English—get code, explanations, or doc-based answers.

    Real Doc Answers: Retrieves code and explanations from real documentation, not just AI guesses.

    Debugging Help: Paste code with errors to get fixes and explanations.

    Context Awareness: Remembers your conversation, so you can build up tasks step by step.

    Parallel Assistant: Runs in your browser—keep it open next to your IDE/editor.

    Customizable: Use it with any documentation (your own, open source, official docs).

Quick Start
1. Prerequisites

    Python 3.8+

    OpenAI API Key
    (Set it with: export OPENAI_API_KEY="sk-...")

2. Clone and Set Up the Project

git clone <your_repo_url>
cd rag-code-assistant
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Add Documentation

    Default: Comes with Python Requests "Quickstart" doc (data/quickstart.html)

    Custom:

        Save your documentation in the data/ folder (.html, .txt, or .md)

        Example: data/flask_docs.html

4. Embed Documentation (One-Time or When Docs Change)

    Update retriever.py to use your doc (change doc_path variable).

    Run:

python retriever.py

This splits your docs into chunks, creates embeddings, and builds a search index.
5. Run the Assistant

streamlit run app.py

    The app opens in your browser.

    Keep it open beside your coding window for instant access.

How to Use
Ask for Code Examples or Doc Info

    “Show me an example of file upload with requests.”

    “How do I set headers in requests?”

Debug Your Code

    Paste code (with or without errors) and ask for fixes.

    for i in range(5
        print(i)

Get Explanations or Write New Code

    “Write a Python function to check if a string is a palindrome.”

    “What is a Python list comprehension?”

Multi-Turn Conversation

    Build up your queries:

        “How do I fetch JSON from an API?”

        “How do I print a specific field from the JSON response?”

How to Add Your Own Documentation

    Save docs as .html, .txt, or .md in /data/.

        Example: data/my_project_docs.html

    Edit the doc_path variable in retriever.py to point to your file.

    Re-run:

python retriever.py

Restart the assistant:

    streamlit run app.py

You can repeat this for any doc, as often as you like!
Troubleshooting

    “Assistant isn’t using my new docs!”

        Double-check your doc_path in retriever.py

        Make sure you re-ran python retriever.py

        Restart the assistant (Ctrl+C and re-run the streamlit command)

    “App won’t start!”

        Ensure your Python environment is activated

        OpenAI API key is set:
        export OPENAI_API_KEY="sk-..."

    “Assistant answers seem generic.”

        Try to phrase your question as it appears in your documentation.

        Add more docs or increase your chunk size in retriever.py if needed.

Pro Tips

    View Doc Chunks: Enable logging in retriever.py to see what docs are retrieved (great for demoing RAG).

    Use With Any Docs: Works with HTML, Markdown, or plain text.

    Privacy: No code is sent anywhere except to OpenAI for answer generation. (Docs stay local.)

Example Queries (for Python Requests Docs)

    “Show me an example of making a POST request.”

    “How do I handle timeouts with requests?”

    “How to check response status code?”

    “Upload a file using requests.”
