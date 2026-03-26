from flask import Flask, request, redirect, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["dummy"]                
collection = db["flask-tutorial"]   

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            name = request.form['name']
            collection.insert_one({"name": name})
            return redirect('/success')
        except Exception as e:
            return render_template('index.html', error=str(e))
    
    return render_template('index.html', error="")

@app.route('/success')
def success():
    return "Data submitted successfully"

app.run(debug=True)