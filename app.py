# Import Flask
from flask import Flask

# Create an app, being sure to pass __name__
app = Flask(__name__)

# Define what to do when a user goes to the index route
@app.route('/')
def hello_world():
    print("Server received request for 'Home' page...")
    return 'Hello world'

# Define what to do when a user goes to the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

if __name__ == "__main__":
    app.run(debug=True)


