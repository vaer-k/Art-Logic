"""Art+Logic Programming Challenge Server"""

import handler as h
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/encode-single/<input_num>', methods=['POST'])
def encode_single(input_num):
    try:
        return h.handle_encode_single(int(input_num))
    except:
        return "Unable to decode"

@app.route('/decode-single/<input_num>', methods=['POST'])
def decode_single(input_num):
    try:
        return str(h.handle_decode_single(str(input_num)))
    except:
        return "Unable to encode"

@app.route('/encode', methods=['POST'])
def encode_file():
    try:
        results = h.handle_encode(request)
        return render_template('results.html', results=results)
    except Exception as e:
        return render_template('error.html', error=e)

@app.route('/decode', methods=['POST'])
def decode_file():
    try:
        results = h.handle_decode(request)
        return render_template("results.html", results=results)
    except Exception as e:
        return render_template('error.html', error=e)        
