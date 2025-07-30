
from flask import Flask, render_template
import os

app = Flask(__name__)
file = "/data/message.txt"

@app.route('/')
def read():
   with open(file, "r") as f:
      content = f.read()
   return render_template("index.html", message=content)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)
