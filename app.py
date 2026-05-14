from flask import Flask, render_template, request, jsonify
import base64
import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature

app = Flask(__name__)

keys = {"private": None, "public": None}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_keys', methods=['POST'])
def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    keys["private"] = private_key
    keys["public"] = private_key.public_key()
    return jsonify({"status": "RSA key berhasil dibuat!"})

@app.route('/sign', methods=['POST'])
def sign():
    if not keys["private"]:
        return jsonify({"error": "Generate keys dulu!"}), 400
    
    file = request.files['file']
    file_data = file.read()
    
    signature = keys["private"].sign(
        file_data,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    
    sig_b64 = base64.b64encode(signature).decode('utf-8')
    return jsonify({"signature": sig_b64})

@app.route('/verify', methods=['POST'])
def verify():
    if not keys["public"]:
        return jsonify({"error": "Keys belum ada!"}), 400
    
    file = request.files['file']
    signature_b64 = request.form['signature']
    
    try:
        file_data = file.read()
        signature = base64.b64decode(signature_b64)
        
        keys["public"].verify(
            signature,
            file_data,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        return jsonify({"is_valid": True})
    except InvalidSignature:
        return jsonify({"is_valid": False})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)