from flask import Flask
from flask import render_template
from flask import request

import database_interface

app = Flask(__name__)

# Global variables
is_logged_in = False


@app.route("/hello", methods=["GET"])
def hello_page():
    return "foobar"


@app.route("/", methods=["POST", "GET"])
@app.route("/index.html", methods=["GET", "POST"])
def index_page():
    global is_logged_in

    # If we receive a POST request, then attempt to login
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Attempt to login with the supplied email and password
        is_logged_in = database_interface.check_login(email, password)

        # Debug message showing whether login was successful or not
        if is_logged_in:
            print(f"user {email} has logged in with {password}")
        else:
            print(f"user {email} failed to log in with {password}")

            # Reset logged_in to false
    else:
        is_logged_in = False

    return render_template("index.html", logged_in=is_logged_in), 200


if __name__ == "__main__":
    app.run(debug=True)
