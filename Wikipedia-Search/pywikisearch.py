import wikipedia

print("Welcome to the app which find an answer to your question from wikipedia")

while True:
    ques = input("What would you like to ask Wikipedia?")
    print wikipedia.summary(ques)
