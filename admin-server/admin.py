from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def fetch_admin_page():
    return 'Welcome to the admin page'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True)