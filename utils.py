import re
import ast

def classify_intent(text):
    if re.search(r'(debug|fix|error|problem)', text, re.I):
        return 'debug'
    elif re.search(r'(example|show me|how to|retrieve|find|documentation|doc)', text, re.I):
        return 'retrieve'
    elif re.search(r'(write|generate|implement|create|code)', text, re.I):
        return 'generate'
    else:
        return 'general'

def static_syntax_check(code):
    try:
        ast.parse(code)
        return "No syntax errors detected."
    except SyntaxError as e:
        return f"Syntax Error: {e}"

