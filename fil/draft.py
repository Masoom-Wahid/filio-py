import json

def reader(path):
    with open(path) as file:
        data = json.load(file)
    print(data)

text = 'data.json'

reader(text)