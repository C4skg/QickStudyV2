from flask import request
from flask import jsonify,render_template
from time import time
from . import main

@main.route('/')
def index():
    return jsonify({
        'code': 200,
        'time': time()
    })