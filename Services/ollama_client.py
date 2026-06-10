import ollama
import os

from dotenv import load_dotenv

load_dotenv()


class OllamaClient:

    def __init__(self):

        self.model_name = os.getenv(
            "OLLAMA_MODEL",
            "llama3"
        )

    def generate_response(self, prompt):

        try:

            response = ollama.chat(
                model=self.model_name,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response["message"]["content"]

        except Exception as e:

            raise Exception(f"Ollama Error: {str(e)}")
