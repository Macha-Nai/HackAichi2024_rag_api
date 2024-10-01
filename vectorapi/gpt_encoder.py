import openai
from dotenv import load_dotenv
from os.path import join, dirname
import os


def gpt_encode(text: str) -> str:
    dotenv_path = join(dirname(__file__), ".env")
    load_dotenv(dotenv_path, verbose=True)
    openai_api_key = os.environ.get('OPENAI_API_KEY')

    client = openai.Client()
    client.api_key = openai_api_key
    prompts = 'You are working on vector data for inclusion in a RAG. Please be sure to extract keywords in English that are important to the text you are about to input. Do not display any text other than the keywords in the output. \nInput:' + text
    print("prompts ", prompts)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "",
            },
            {"role": "user", "content": prompts},
        ],
    )
    message_object = completion
    print("message_object ", message_object)
    return "hogehoge"
