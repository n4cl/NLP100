# coding: utf-8

from flask import Blueprint, request, jsonify


app = Blueprint(__name__, "service")


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return "Not Implemented"

    elif request.method == "GET":
        return "Not Implemented"
