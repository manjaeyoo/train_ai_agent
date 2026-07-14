from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# 클라이언트 생성 
sync_client = OpenAI()

# LLM 호출 함수 선언
def call_LLM(prompt: str, model: str = "gpt-5.4-nano") -> str:
    messages = []
    messages.append({"role": "user", "content": prompt})
    responses = sync_client.responses.create(
        model=model,
        input=messages
    )
    return responses.output_text


if __name__ == "__main__":
    test = call_LLM("한국의 수도는?")
    print(test)
