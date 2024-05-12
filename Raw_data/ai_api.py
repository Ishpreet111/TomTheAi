import requests

url = "https://cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com/v1/chat/completions"

while True:
    msg = input("You: ")
    
    if msg.lower() == "exit":
        break
    
    else:
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": f"{msg}"
                }
            ],
            "model": "gpt-4-turbo-preview",
            "max_tokens": 200,
            "temperature": 0.9
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "b3fd226e18msh4d8edfea405d7b1p17a187jsna9104698d53d",
            "X-RapidAPI-Host": "cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            print(f"Tommy: {data['choices'][0]['message']['content']}")
        else:
            print("Error:", response.text)
