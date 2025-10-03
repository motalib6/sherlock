# chain.py
# This file contains core chain logic connecting language models and tools.
# Contributing here helps extend AI-powered application flows and integrations.

class Chain:
    def __init__(self, steps):
        self.steps = steps

    def run(self, input_text):
        result = input_text
        for step in self.steps:
            result = step.process(result)
        return result

# More than 500 lines in full project including integrations
