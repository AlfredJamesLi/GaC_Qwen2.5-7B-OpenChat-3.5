import requests

if __name__ == "__main__":

    url = "http://0.0.0.0:8000/api/generate/"

    data = {
        "messages_list": [
            [
                {
                    "role": "user",
                    "content": "Which word does not belong with the others?\ntyre, steering wheel, car, engine",
                }
            ],
            [{"role": "user", "content": "9.11 and 9.9, which is bigger?"}],
        ],
        "max_new_tokens": 1024,
        "apply_chat_template": True,
    }

    response = requests.post(url, json=data)
    print(response.json())
