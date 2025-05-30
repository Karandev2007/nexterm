import requests
import json
## groq api key here
API_KEY = "enter your key here :)"

def ask(question):
    print(f"Asking AI: {question}") ## show user question

    if not API_KEY:
        print("❌ API key is missing.") ## incase no api key
        return

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama3-70b-8192",
                "messages": [
                    {"role": "user", "content": question}
                ],
                "temperature": 0.7,
                "max_tokens": 500
            }
        )

        data = response.json()

        # print complete response
        if "choices" not in data:
            print("❌ Invalid response:")
            print(json.dumps(data, indent=2))
            return

        answer = data["choices"][0]["message"]["content"].strip()
        print(f"\n💬 {answer}")

    except Exception as e:
        print("❌ Failed to get AI response:", e)