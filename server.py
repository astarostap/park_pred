from flask import Flask
import flask.views

app = Flask(__name__)

@app.route("/")
def server():
	return "Hello Abraham and Baris.!"


if __name__ == "__main__":
    app.run(debug=True)