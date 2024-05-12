from django.shortcuts import render
import requests
import pyperclip
from django.http import HttpResponse

def getinfo(request):
    if request.method == "POST":
        url = "https://cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com/v1/chat/completions"
        msg = request.POST.get('input-feild00')
            
        if msg.lower() == "exit":
            pyperclip.copy("GoodBye!")
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
                pyperclip.copy(f"{data['choices'][0]['message']['content']}")
            else:
                pyperclip.copy("Error:", response.text)
    
    elif request.method == "GET":

        return render(request, 'index.html')
    
    return HttpResponse("Answer Successfully Copied", status=405)
