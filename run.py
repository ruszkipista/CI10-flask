import os
from flask import Flask, render_template

# name of the application module or package (="__main__")
# where should Flask look for templates and static files
app = Flask(__name__) 

@app.route("/")  # trigger point through webserver: "/"= root directory
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/careers")
def careers():
    return render_template("careers.html")    

# script runs as main, not as imported code
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "127.0.0.1"),  #get value or use given default
        port=int(os.environ.get("PORT", "8080")),#get value or use given default
        debug=True)         # allow debugging, only for development phase