from flask import Flask, render_template, jsonify, redirect, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html", pred=7) 

@app.route("/hi", methods=['GET']) 
def hi():
    return render_template("hi.html") 

if __name__ == "__main__":
    app.run()
