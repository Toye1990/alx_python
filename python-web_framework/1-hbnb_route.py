"""flask is imported to use as a server run the database query"""
from flask import Flask

app=Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
 return "Hello HBNB!"

@app.route("/hbnb")
def hbnb():
 return "HBNB"

if __name__ == "__main__":
 app.run(host="0.0.0", port=5000, debug=True)