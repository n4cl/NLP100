# coding: utf-8

from flask import Flask
from controller import service

app = Flask(__name__)
app.register_blueprint(service.app, url_prefix="")

if __name__ == '__main__':
    SERVER_IP = "0.0.0.0"
    app.run(host=SERVER_IP, debug=True)
