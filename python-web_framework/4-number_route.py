"""flask is imported to use as a server run the database query"""
from flask import Flask

app=Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
 return "Hello HBNB!"

@app.route("/hbnb")
def hbnb():
 return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
 return f"C{text.replace('_', '')}"

@app.route("/c/<text>", strict_slashes=False)
def c(text="is cool"):
 return f"C{text.replace('_', '')}"

@app.route("/number/<n>", strict_slashes=False)
def N(n):
 if isinstance(n, int):
  return f"n is a number"
 else:
  return "n is not a number"


if __name__ == "__main__":
 app.run(host="0.0.0", port=5000, debug=True)
