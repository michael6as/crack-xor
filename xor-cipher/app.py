from flask import Flask, request
from flask_cors import CORS
import json

from cipher.encryptor import XorEncryptor

app = Flask(__name__)
CORS(app)


@app.route('/crack', methods=['POST'])
def crack():
    enc = XorEncryptor()
    json_params = request.get_json()
    ascii_arr = json_params['text']
    key_size = int(json_params['keySize'])
    possible_keys = enc.guess_key(ascii_arr, key_size)

    # Couldn't find a nicer way to return the generator to the client...
    all_keys = []
    for key in possible_keys:
        all_keys.append(key)
    return json.dumps(all_keys)


if __name__ == '__main__':
    app.run()
