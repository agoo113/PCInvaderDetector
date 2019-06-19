from flask import Flask
import json

app = Flask(__name__)

system_enable = False


@app.route('/')
def hello():
    return 'Dao page'


@app.route('/get_status')
def get_status():
    return json.dumps(system_enable)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
