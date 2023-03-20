import json

data = json.load(open("data.json"))

def translate(word):
    if word in data:
         return data[word]
    else:
         return ("The word doesnt exist in my dictionary!!")

word = input("So what do you wanna know user: ")

print(translate(word))

