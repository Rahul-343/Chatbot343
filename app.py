from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
time.clock = time.time
 
app = Flask(__name__)
 
english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
 
@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/get")
def get_bot_response():
    print("rahul")
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))

@app.route("/*")
def error():
    print("error")
    error ="error 404 not found"
    return error

 
 
if __name__ == "__main__":
    app.run()