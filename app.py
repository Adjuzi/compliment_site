from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/get_compliment', methods=['GET'])
def get_compliment():
    compliment = requests.get('https://complimentr.com/api')
    return compliment.text


if __name__ == '__main__':
    app.run()
