
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

with open('file.txt','r') as file:
    conversation = file.read()

bot = ChatBot("Sunanda's Resume ChatBot")
trainer = ListTrainer(bot)
trainer.train(conversation)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/get")
def get_bot_response():
	userText = request.args.get('msg')
	return str(bot.get_response(userText))
if __name__ == "__main__":
	app.run()