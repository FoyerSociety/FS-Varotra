from flask import Flask , request, render_template

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html'), 200


@app.route("/admin")
def administration():
	return 'Tsy itako oo', 404


@app.route("/user/<int:username>")
def user(username):
	return "Je suis le compte de " + str(username)

if __name__ == "__main__":
	app.run()
