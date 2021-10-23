from flask import Flask

from worker import add

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    add.delay(2, 2)
    return "OK", 201


if __name__ == '__main__':
    app.run(debug=True)
