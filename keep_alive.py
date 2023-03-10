from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hi!, I'm Discord bot made with Pycord! Don't forget to add monitor on me(if you are using Repl.it)" 
    
def run(): 
    # change out '8081 to 8080
    app.run(host='0.0.0.0',port=8081) # This is Repl.it default port 8080.
    
def keep_alive():
    t = Thread(target=run)
    t.start()