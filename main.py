from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index_page():
    return render_template("index.html"), 200


if __name__ == "__main__":
    app.run(debug=True)
