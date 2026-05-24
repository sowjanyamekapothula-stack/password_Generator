from flask import Flask, render_template, request
import random
import string
import webbrowser
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", password="")

@app.route('/generate', methods=['POST'])
def generate():

    length = int(request.form['length'])

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return render_template("index.html", password=password)


# Open browser automatically
def open_browser():
    webbrowser.open("http://127.0.0.1:5000/")

if __name__ == "__main__":
    threading.Timer(1.5, open_browser).start()
    app.run(debug=True)