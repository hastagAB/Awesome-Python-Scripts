import json
from difflib import get_close_matches


data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data :
        return data[w]
# Added to deal with input words which starts with capital letter
    elif w.title() in data:
        return data[w.title()]
#in case user enters words like USA or NATO
    elif w.upper() in data:
        return data[w.upper()]
#will check the close range words
    elif len(get_close_matches(w,data.keys())) >0:
#Condition given to the user
        yn = input("Did you mean %s instead? Enter Y if yes or N for no: " %get_close_matches(w,data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == 'N':
            return "The word doesn't exist,please recheck"
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exit, Please re-check it!"

word = input("Enter word:")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
