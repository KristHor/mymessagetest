import requests

url = "http://127.0.0.1:8000/message/"


def post_json():
    payload = {"username": "Dummy json", "message": "Dummy message"}

    r = requests.post(url, data=payload)

    r.json()


def get_jason():
    r = requests.get(url, data={'key': 'value'})

    return r.text





