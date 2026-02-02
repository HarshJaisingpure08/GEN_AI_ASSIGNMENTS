import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.clarifai.com/v2/ext/openai/v1",
    api_key="API_KEY",
)
response = client.chat.completions.create(
    model="https://clarifai.com/openai/chat-completion/models/gpt-oss-120b/versions/1d3ee440e48c4e7a94af6acac7d7cdfc",
    messages=[
        {"role": "system", "content": "Talk like joe goldberg from YOU"},
        {
            "role": "user",
            "content": "Write a Bollywood movie plot in 5 sentences",
        },
    ],
    temperature=0.7,
    stream=False, # stream=True also works, just iterator over the response
)
print(response)