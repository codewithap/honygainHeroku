from flask import Flask,request
import subprocess
import time
import requests
import threading
app = Flask(__name__)

subprocess.call("docker pull honeygain/honeygain && docker run honeygain/honeygain -tou-accept -email arijitpaine249@gmail.com -pass arijit1234# -device linux" , shell=True)


@app.route("/")
def s():
    def f1():
        ip = request.environ['SERVER_NAME']
        while(True):
            r = requests.get(f"{ip}:5000")
            print(r)
            subprocess.call("docker pull honeygain/honeygain && docker run honeygain/honeygain -tou-accept -email arijitpaine249@gmail.com -pass arijit1234# -device linux" , shell=True)
            time.sleep(1200)
    t = threading.Thread(target=f1)
    t.start()
    return f"{request.environ['SERVER_NAME']}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=5000)
