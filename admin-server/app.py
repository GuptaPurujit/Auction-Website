from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def fetch_admin_page():
    return 'Welcome to the admin page'

@app.route('/login', methods=['GET'])
def fetch_login_page():
    return 'Welcome to the login page'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)