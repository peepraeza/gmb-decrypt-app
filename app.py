from flask import Flask, request
from decrypt import AESCipher

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/decrypt", methods=['POST'])
def decrypt():
    request_data = request.get_json()
    message = request_data['message']
    key = request_data['key']
    dec = AESCipher(message, key).decrypt()
    return dec

@app.route("/encrypt", methods=['POST'])
def encrypt():
    request_data = request.get_json()
    message = request_data['message']
    key = request_data['key']
    enc = AESCipher(message, key).encrypt()
    return enc