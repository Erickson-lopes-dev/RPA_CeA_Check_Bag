from flask import Flask, request, jsonify
from RPA_Selenium.zattini_bot import rpa
import json
import time

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return "<h1> Estou funcionando! </h1>"


@app.route('/rpa', methods=['POST'])
def rpa_cea():

    result = {}

    try:
        start = time.time()
        json_data = json.loads(request.data)
        result = rpa(json_data)
        result["temp"] = "--- %s seconds ---" % (round(time.time() - start, 2))
    except Exception as error:
        result['error'] = error

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
