from flask import Flask

app = Flask(__name__)  # creating the Flask class object


@app.route('/')
def home():
    return "Welcome..!"


if __name__ == '__main__':
    app.run(debug=True)
