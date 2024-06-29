#!/usr/bin/python3
"""
This script starts a Flask web application.

The application listens on 0.0.0.0, port 5000.

Routes:
    - /: Displays "Hello HBNB!"
    - /hbnb: Displays "HBNB"
    - /c/<text>: Displays "C " followed by the value of the text variable with\
        underscores replaced by spaces.
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """
    Displays "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
    Displays "HBNB"
    """
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """
    Displays "C " followed by the value of the text variable with underscores\
        replaced by spaces.
    """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
