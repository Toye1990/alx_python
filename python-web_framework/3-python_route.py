#flask is imported to use as a server run the database. Lorem ipsum dolor sit amet consectetur adipiscing elit tempus natoque faucibus viverra, litora
#odio vitae cras blandit ut est integer nisl in accumsan himenaeos,
from flask import Flask

#Create app variable intialize flask network#
app=Flask(__name__)

"""Create app variable intialize flask network which will initiate the return of 
HELLO HBNB"""
# Define routes with the strict_slashes=False option
@app.route("/", strict_slashes=False)
def hello():
 return "Hello HBNB!"

"""Create app variable intialize flask network which will initiate the return of 
HBNB"""
@app.route("/hbnb")
def hbnb():
 return "HBNB"

"""Create app variable intialize flask network which will initiate the return of 
of an empty space"""
@app.route("/c/<text>", strict_slashes=False)
def c(text):
 return f"C{text.replace('_', '')}"

"""Create app variable intialize flask network which will initiate the return of 
of text"""
@app.route("/c/<text>", strict_slashes=False)
def c(text="is cool"):
 return f"C{text.replace('_', '')}"

if __name__ == "__main__":
 app.run(host="0.0.0", port=5000, debug=True)
