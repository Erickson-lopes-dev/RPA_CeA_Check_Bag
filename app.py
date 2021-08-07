from flask import Flask, request, jsonify
import json

from RPA_Selenium.zattini_bot import rpa

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    json_data = json.loads(request.data)
    return jsonify(rpa(json_data))


if __name__ == '__main__':
    app.run(debug=True)
