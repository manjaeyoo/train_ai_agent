from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def get_response(prompt, model="gpt-5.4-mini"):
    response = client.responses.create(
        model=model,
        tools=[{"type": "web_search"}],
        input=prompt
    )
    return response.output_text

def main():
    input_prompt = """
https://platform.openai.com/docs/api-reference/responses/create
를 읽어서 리스폰스 API에 대해 요약 정리해주세요.
"""
    response_text = get_response(prompt=input_prompt, model="gpt-5.4-nano")
    print("대답:")
    print(response_text)


if __name__ == "__main__":
    main()
