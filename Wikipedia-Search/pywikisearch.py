import wikipedia

print("Welcome to the app which find an answer to your question from wikipedia")

while True:
    ques = input("What would you like to ask Wikipedia?")
    wikipedia.set_lang("en") #change "en" to convenient language for example wikipedia.set_lang("es") will set the language to spanish
    try:
        print(wikipedia.summary(ques, sentences=3))
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"DisambiguationError: {e}")
    except wikipedia.exceptions.PageError as e:
        print(f"PageError: {e}")
    more = input("Do you want to ask anything else? (y/n)")
    if more.lower() != 'y':
        break