from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI") # Set the connection string to connect to the database using an environment variable
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # Create SQLALchemy object

class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), nullable=False)
	last_name = db.Column(db.String(30), nullable=False)

@app.route('/')
def home():
    return "Hello Internet!"

@app.route('/diff', methods=["GET", "POST"])
def hell_diff():
	if request.method == "Post":
		return "<h2>post request</h2>"
	else: 
		return "<h2>get request</h2>"

@app.route('/edit/<int:word>') 
def edit(word): 
	return f"<h1>{word * 5}</h1>" 

@app.route('/redirects')
def redirects(): 
	return redirect("http://google.com") 

@app.route('/urlfor') 
def urlfor(): 
	return redirect(url_for("home"))


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
