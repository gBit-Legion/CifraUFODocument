from flask import Flask

app = Flask(__name__)


@app.route('/', methods='POST')
def start_page():
    pass


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
