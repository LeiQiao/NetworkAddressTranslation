from flask import Flask, request, g
from flask_httpauth import HTTPBasicAuth
import os
import re

app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_token(user, password):
    g.user = ''.join(re.findall(re.compile('\w+'), user))
    g.password = ''.join(re.findall(re.compile('\w+'), password))
    if len(g.user) == 0 or len(g.password) == 0:
        return False
    return True


@app.route('/nat', methods=['POST'])
@auth.login_required
def set_nat():
    file_name = g.user + '_' + g.password + '.ip.txt'
    real_ip = request.headers['X-Real-IP']
    with open(os.path.join(app.static_folder, file_name), 'wb') as f:
        f.write(real_ip.encode('utf-8'))
    return real_ip, 200


@app.route('/nat', methods=['GET'])
@auth.login_required
def get_nat():
    file_name = g.user + '_' + g.password + '.ip.txt'
    try:
        with open(os.path.join(app.static_folder, file_name), 'rb') as f:
            content = f.read()
            return content, 200
    except Exception as e:
        str(e)
        return '', 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)
