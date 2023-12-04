import gradio as gr
from langchain.llms import Ollama
import time
from context import contextText

class Assistant:
    def __init__(self):
        self.interface = gr.Blocks()
        self.startInterface()
        self.context = contextText
        self.ollama = Ollama(base_url="http://localhost:11434", model="assistant")

    def startInterface(self):
        with self.interface:
            self.chat = gr.Chatbot()
            self.input = gr.Textbox()
            self.clearButton = gr.ClearButton([self.input, self.chat])
            self.input.submit(self.makeResponse, inputs=[self.input, self.chat], outputs=[self.input, self.chat])

    def makeResponse(self, userText, chatHistory):
        ollamaResponse = ""
        full_input = self.context + userText
        for parte in self.ollama.stream(full_input):
            ollamaResponse += parte
        chatHistory.append((userText, ollamaResponse))
        return "", chatHistory

    def start(self):
        self.interface.launch()

if __name__ == "__main__":
    assistant = Assistant()
    assistant.start()
