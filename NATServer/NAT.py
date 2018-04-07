from flask import Flask, request
import os

app = Flask(__name__)


@app.route('/nat', methods=['POST'])
def set_nat():
    real_ip = request.headers['X-Real-IP']
    with open(os.path.join(app.static_folder, 'ip.txt'), 'wb') as f:
        f.write(real_ip.encode('utf-8'))
    return real_ip, 200


@app.route('/nat', methods=['GET'])
def get_nat():
    try:
        with open(os.path.join(app.static_folder, 'ip.txt'), 'rb') as f:
            content = f.read()
            return content, 200
    except Exception as e:
        str(e)
        return '', 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)
