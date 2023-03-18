from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def fetch_home_page():
    return 'Welcome to the homepage'

@app.route('/register', methods=['GET'])
def fetch_registeration_page():
    return 'Welcome to the registeration page'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
