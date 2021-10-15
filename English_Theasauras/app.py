import json
import difflib

from difflib import get_close_matches

data = json.load(open("data.json"))     # Importing data from data.json

def show_def(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        choice = input("Did you mean %s instead ? Enter Y for yes or N for no: " % get_close_matches(word, data.keys())[0])
        if choice == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif choice == "N":
            return "The word doesn't exist. Please double check it!!"
        else:
            return "We didn't understand your entry!"
    else:
        return "The word doesn't exist. Please double check it!!"


word = input("Please enter your word: ")

output = show_def(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

