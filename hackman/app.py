from flask import Flask, render_template, request
from main.app import App

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/about")
def about():
    return render_template('AboutUs.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_Chat_response(input)


def get_Chat_response(text):
    app = App()
    return app.bot_response(text)

if __name__ == '__main__':
    app.run()
