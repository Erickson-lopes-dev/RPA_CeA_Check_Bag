from flask import Flask, request, jsonify
from RPA_Selenium.zattini_bot import rpa
import logging
import json
import time
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def route_test():
    arquivos = []
    try:
        pasta = os.path.join(os.getcwd(), 'logs')
        arquivos = [arquivos for diretorio, subpastas, arquivos in os.walk(pasta)][0]

    except Exception as error:
        return {'status': f"ERRo {str(error)} {str(type(error))}"}

    return jsonify({"test": "Aplicação testada!", "files": arquivos})


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
