import json

def get_msg(key):
    with open("messages.json") as file:
        data = json.load(file)
        return data['messages'][key]
