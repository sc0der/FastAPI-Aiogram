def get_msg(key):
    with open("message.json") as file:
        data = json.load(file)
        return data[key]
