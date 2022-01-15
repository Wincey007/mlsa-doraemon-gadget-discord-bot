from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Doraemon's Gadgets bot is ready to use"

def run():
    app.run(host='0.0.0.0', port=80)

def keep_alive():
    t = Thread(target=run)
    t.start()