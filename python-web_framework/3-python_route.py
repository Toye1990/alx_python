"""importing flask module"""
from flask import Flask

"""Create an instance"""
app=Flask(__name__)

"""route definition"""
@app.route("/", strict_slashes=False)
def hello():
 return "Hello HBNB!"

"""Create app variable intialize flask network which will initiate the return of 
HBNB"""
@app.route("/hbnb")
def hbnb():
 return "HBNB"

"""c is fun"""
@app.route("/c/<text>", strict_slashes=False)
def c(text):
 return f"C{text.replace('_', '')}"

"""python is cool"""
@app.route("/c/<text>", strict_slashes=False)
def c(text="is cool"):
 return f"C{text.replace('_', '')}"

"""using the if __name__ code to ensure code doesn't run when imported"""
if __name__ == "__main__":
 app.run(host="0.0.0", port=5000, debug=True)
