from flask import Flask , request, render_template
app = Flask(__name__)



@app.route('/')
def index():
	return render_template('index.html'), 200

@app.route("/hanokatra")
def hanokatra():
	return render_template('hanokatra.html'), 200

@app.route("/mpandrindra")
def mpandrindra():
	return render_template('mpandrindra.html'), 200

@app.route("/hamandrika")
def hamandrika():
	return render_template('hamandrika.html'), 200

@app.route("/vokatra")
def vokatra():
	return render_template('vokatra.html'), 200

@app.route("/mpanjifa")
def mpanjifa():
	return render_template('mpanjifa.html'), 200


@app.route("/user/<int:username>")
def user(username):
	return "Je suis le compte de " + str(username)




if __name__ == "__main__":
	app.run()
