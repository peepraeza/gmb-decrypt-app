import sys

from flask import Flask, request, render_template
from decrypt import AESCipher

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/decrypt", methods=['POST'])
def decrypt():
    print('router Call Decrypt', file=sys.stderr)
    request_data = request.get_json()
    message = request_data['message']
    key = request_data['key']
    dec = AESCipher(message, key).decrypt()
    return dec


@app.route("/encrypt", methods=['POST'])
def encrypt():
    print('router Call Encrypt', file=sys.stderr)
    request_data = request.get_json()
    message = request_data['message']
    key = request_data['key']
    enc = AESCipher(message, key).encrypt()
    return enc


@app.route("/process", methods=['POST'])
def precess():
    print('router Call From FrontEnd', file=sys.stderr)
    message = request.form['encryptedData']
    key = request.form['key']
    from_method = request.form['from-method']
    print(key,from_method,message, file=sys.stderr)
    if from_method.lower() == 'decrypt':
        print('call function decrypt', file=sys.stderr)
        resp = AESCipher(message, key).decrypt()
    else:
        print('call function encrypt', file=sys.stderr)
        resp = AESCipher(message, key).encrypt()
    return resp


if __name__ == '__main__':
    app.run(debug=True)
