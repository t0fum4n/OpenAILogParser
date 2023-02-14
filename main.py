import requests

model = "text-davinci-002" # the OpenAI API model you want to use
prompt = "What is the meaning of life?" # the prompt you want to generate a response for

url = f"https://api.openai.com/v1/engines/{model}/jobs"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer API_KEY", # Replace API_KEY with your OpenAI API key
}

data = {
  "prompt": prompt,
  "max_tokens": 128,
  "temperature": 0.5,
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print(result["choices"][0]["text"])
else:
    print("Failed to generate response from OpenAI API")
