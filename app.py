from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return {'msg': 'working testing dbbbb'}


if _name_ == '__main__':
    app.run(host='0.0.0.0', port=5000)
