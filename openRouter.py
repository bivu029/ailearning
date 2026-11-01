import requests
import json
import os

API_KEY = os.getenv("OPENROUTER_API_KEY")  # or paste your real key here temporarily
print(API_KEY)
response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    },
    data=json.dumps({ 
        
        "model": "openrouter/free",
        "messages": [
            {
                "role": "user",
                "content": "How many r's are in the word 'strawberry'?"
            }
        ],
        "reasoning": {"enabled": True}
    })
)

print("Status:", response.status_code)
print("Response:", response.text)   # <-- this shows the real error

data = response.json()
if "choices" in data:
    msg = data["choices"][0]["message"]
    print(msg.get("content"))
    print(msg.get("reasoning_details"))
else:
    print("Error:", data.get("error"))