from flask import jsonify
from time import time

from . import main

@main.route('/')
def index():
    return jsonify({
        'code': 200,
        'time': time()
    })