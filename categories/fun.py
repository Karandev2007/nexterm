import requests

def joke():
    print("Here's a joke for you:")
    try:
        res = requests.get("https://official-joke-api.appspot.com/jokes/programming/random")
        data = res.json()[0]
        print(f"{data['setup']} ... {data['punchline']}")
    except:
        print("❌ Couldn't fetch a joke right now.")