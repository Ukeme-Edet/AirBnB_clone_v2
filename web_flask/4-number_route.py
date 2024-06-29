#!/usr/bin/python3
"""
This script starts a Flask web application.

The application listens on 0.0.0.0, port 5000.

Routes:
    - /: Displays "Hello HBNB!"
    - /hbnb: Displays "HBNB"
    - /c/<text>: Displays "C " followed by the value of the text variable with\
        underscores replaced by spaces.
    - /python/<text>: Displays "Python " followed by the value of the text\
        variable with underscores replaced by spaces and default value\
        set to "is cool".
    - /number/<n>: Displays "n is a number" only if n is an integer.
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """
    Displays "Hello HBNB!"

    Returns:
            str: "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
    Displays "HBNB"

    Returns:
            str: "HBNB"
    """
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """
    Displays "C " followed by the value of the text variable with\
        underscores replaced by spaces.

    Args:
        text (str): The text to display.

    Returns:
        str: The formatted text.
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python/")
@app.route("/python/<text>")
def python(text="is cool"):
    """
    Displays "Python " followed by the value of the text variable with\
        underscores replaced by spaces and default value set to "is cool".

    Args:
        text (str): The text to display.

    Returns:
        str: The formatted text.
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def number(n):
    """
    Displays "n is a number" only if n is an integer.

    Args:
            n (int): The number to display.

    Returns:
            str: The formatted text.
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
