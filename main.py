from flask import Flask , request, render_template
import pyodbc
conn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql/lib64/libmsodbcsql-17.6.so.1.1}; SERVER=127.0.0.1; PORT=1433; DATABASE=VENTEDB; UID=SA; PWD=root18**; Trusted_Domain=domain.local;') 
app = Flask(__name__)


cursor = conn.cursor()
cursor.execute("""
			   INSERT INTO Client(nom_client, cin_client, adresse_client, Password) 
			   VALUES
			   ('Aina','123232325231', 'Manakara', 'ainajah')
			   
			""")
cursor.commit()
 
#for row in cursor:
#     print(row)




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
