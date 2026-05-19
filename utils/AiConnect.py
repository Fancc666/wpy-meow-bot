from openai import OpenAI
from utils.EnvironTool import config

class AiHandler:
    def __init__(self) -> None:
        self.client = OpenAI(
            api_key=config.get("API_KEY", ""),
            base_url="https://ai.tju.edu.cn/api/v3"
        )
    def _send_request(self, text):
        response = self.client.chat.completions.create(
            model="tju-llm",
            messages=[
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content
