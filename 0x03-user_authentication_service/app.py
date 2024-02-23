#!/usr/bin/env python3
"""This ia a flask app
"""
from auth import Auth
import logging
from flask import Flask, abort, jsonify, redirect, request


logging.disable(logging.WARNING)


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """This the index function"""
    return jsonify({"message": "Bienvenue"})
