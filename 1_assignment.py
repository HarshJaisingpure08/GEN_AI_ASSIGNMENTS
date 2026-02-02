import cohere

co = cohere.Client("YOUR_COHERE_API_KEY")

response = co.chat(
    model="command-r-plus", 
    temperature=0.7,
    messages=[
        {
            "role": "system",
            "content": "Talk like Joe Goldberg from YOU"
        },
        {
            "role": "user",
            "content": "Write a Bollywood movie plot in 5 sentences"
        }
    ]
)


print(response.text)

