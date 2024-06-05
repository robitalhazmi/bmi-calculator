from flask import Flask
import os

app = Flask(__name__)

# set up root route
@app.route("/")
def hello_world():
	return "BMI Calculator App"

# Get the PORT from environment
port = os.getenv('PORT', '8080')
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=int(port))