from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    ip = request.remote_addr
    return render_template('index.html', ip=ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
