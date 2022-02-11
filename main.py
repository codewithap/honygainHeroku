from flask import Flask,request
import subprocess
import time
import requests
import threading
app = Flask(__name__)

subprocess.call("python main.py" , shell=True)

@app.route("/")
def home():
    return "working"

@app.route("/start")
def s():
    def f1():
        ip = request.environ['SERVER_NAME']
        while(True):
            r = requests.get(f"{ip}:5000")
            print(r)
            subprocess.call("python main.py" , shell=True)
            time.sleep(1200)
    t = threading.Thread(target=f1)
    t.start()
    return f"{request.environ['SERVER_NAME']}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=5000)
