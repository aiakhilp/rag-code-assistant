class ContextManager:
    def __init__(self):
        self.history = []

    def add(self, role, content):
        self.history.append({"role": role, "content": content})

    def get(self, n=10):
        return self.history[-n:]

