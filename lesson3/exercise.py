from base64 import b64encode

from flask import Flask, request, jsonify

app = Flask(__name__)

authorized_users = [
    {
        'username': "gsorrentino",
        'password': "password"
    }
]

def check_user_auth(header):
    encoded = header.split()[-1].encode("utf-8")
    if encoded in [b64encode((user['username'] + ":" + user['password']).encode("utf-8")) for user in authorized_users]:
        return True

def login_required(f):
    def decorated(*args, **kwargs):
        raise NotImplementedError
    return decorated        
    
@app.route('/')
def confidential():
    return jsonify({
        "200": "Unrestricted Access"
    })

@app.route('/restricted')
@login_required  
def restricted():
    return jsonify({
        "200": "Authorized"
    })

if __name__ == '__main__':
    app.run(debug=True)