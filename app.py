from flask import Flask, request, jsonify
import json
import time

from RPA_Selenium.zattini_bot import rpa

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    start = time.time()
    json_data = json.loads(request.data)
    result = rpa(json_data)
    result["temp"] = "--- %s seconds ---" % (round(time.time() - start, 2))
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
