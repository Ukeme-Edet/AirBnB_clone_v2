#!/usr/bin/python3
"""
This script starts a Flask web application.

The application listens on 0.0.0.0, port 5000.

Routes:
	- /states_list: Displays an HTML page with a list of all State objects.
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


@app.route("/states_list")
def states_list():
    """
    Displays an HTML page with a list of all State objects.

    Returns:
            HTML: The list of State objects.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
