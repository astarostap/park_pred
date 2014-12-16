from flask import Flask
import flask.views

app = Flask(__name__)

class View(flask.views.MethodView):
	def get(self):
		return "Hello World!"

app.add_url_rule('/', view_func=View.as_view('main'))

app.debug = True


if __name__ == "__main__":
    app.run()