from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "hello docker image!"

@app.route("/<something>")
def hello(something):
    return "{}, welcome to docker image".format(something)

if __name__ == '__main__':
    app.run()