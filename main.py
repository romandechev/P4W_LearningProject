from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

# Global variables
is_logged_in = False


@app.route("/", methods=["POST", "GET"])
@app.route("/index.html", methods=["GET", "POST"])
def index_page():
    global is_logged_in

    # If we receive a POST request, then set is_logged_in to true
    # Otherwise, set is_logged_in to false
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        is_logged_in = True
        print(f"user {email} has logged in with {password}")

    else:
        is_logged_in = False

    return render_template("index.html", logged_in=is_logged_in), 200


if __name__ == "__main__":
    app.run(debug=True)
