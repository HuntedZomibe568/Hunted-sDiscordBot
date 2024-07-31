from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot is running!'

@app.route('/start')
def start():
    return 'Bot is starting!'

if __name__ == "__main__":
    app.run()
