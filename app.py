from flask import Flask, request, jsonify
from RPA_Selenium.zattini_bot import rpa
import json
import time

app = Flask(__name__)


@app.route('/teste', methods=['GET'])
def hello():
    return "<h1> Estou funcionando! </h1>"


@app.route('/', methods=['POST'])
def rpa_cea():
    start = time.time()
    json_data = json.loads(request.data)
    result = rpa(json_data)
    result["temp"] = "--- %s seconds ---" % (round(time.time() - start, 2))
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
