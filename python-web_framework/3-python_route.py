"""flask is imported to use as a server run the database. Lorem ipsum dolor sit amet consectetur adipiscing elit tempus natoque faucibus viverra, litora
 odio vitae cras blandit ut est integer nisl in accumsan himenaeos
 Lorem ipsum dolor sit amet consectetur adipiscing elit tempus natoque faucibus viverra, litora odio vitae cras blandit ut est integer nisl in accumsan himenaeos, facilisis eu maecenas lectus ante platea commodo curabitur fermentum et. 
Pellentesque euismod proin himenaeos nullam felis eros maecenas egestas tristique, pretium imperdiet morbi habitasse ullamcorper cras ad accumsan turpis, quis congue phasellus ultricies potenti volutpat varius torquent. 
Curae ante congue eu parturient imperdiet dui tempus penatibus, ultrices magnis massa dapibus sed lacus aenean porta aliquam, pretium consequat diam leo velit phasellus quis.

Dignissim velit molestie laoreet gravida egestas quis ante cursus sapien tincidunt hac, dui suspendisse pharetra netus fringilla pulvinar penatibus vivamus orci bibendum. Integer sociosqu nostra taciti ultricies ad pulvinar per, rhoncus sociis nascetur interdum tempor auctor sed dapibus, vivamus proin senectus ligula ante erat. Curae aptent ut erat hendrerit mi hac dignissim, pulvinar id semper inceptos quam felis sem vel, luctus auctor metus dui lobortis dis.
,
"""
from flask import Flask

"""Create app variable intialize flask network"""
app=Flask(__name__)

"""Create app variable intialize flask network which will initiate the return of 
HELLO HBNB"""
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
