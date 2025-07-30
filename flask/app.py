from flask import Flask
import os

app = Flask(__name__)
file = "/data/message.txt"

@app.route('/')
def read():
   with open(file, "r") as f:
      content = f.read()
   return f"<h1>message:</h1><p>{content}</p>"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)
