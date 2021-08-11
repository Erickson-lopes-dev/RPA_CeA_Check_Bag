from flask import Flask, request, jsonify
from RPA_Selenium.zattini_bot import rpa
import logging
import json
import time
import os

app = Flask(__name__)


def generator_log(name, path_file):
    loggers = {}

    if loggers.get(name):
        return loggers.get(name)
    else:
        logger = logging.getLogger(name)
        handler = logging.FileHandler(f'{path_file}')
        formatter = logging.Formatter('[%(levelname)s] [%(message)s] [%(asctime)s]')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        loggers[name] = logger

        if logger.hasHandlers():
            logger.handlers.clear()

        logger.addHandler(handler)

        return logger


@app.route('/', methods=['GET'])
def route_test():
    log_test = generator_log('route_test', 'logs/route_test.log')
    log_test.info('Testando aplicação')

    arquivos = []
    try:
        pasta = os.path.join(os.getcwd(), 'logs')
        arquivos = [arquivos for diretorio, subpastas, arquivos in os.walk(pasta)][0]
        log_test.info('Coletando arquivos logs')
    except Exception as error:
        log_test.error(error)
    else:
        log_test.info('Enviando dados')

    rc = []
    rt = []
    try:

        rt = open('logs/route_test.log', encoding='utf-8').readlines()
        rc = open('logs/rpa_cea.log').readlines()
    except Exception as error:
        log_test.info(error)

    else:
        log_test.info('Enviando dados')
        return jsonify({"test": "Aplicação testada!", "files": arquivos, "route_test": rt, "rpa_cea": rc})


@app.route('/rpa', methods=['POST'])
def rpa_cea():
    log_cea = generator_log('rpa_cea', 'logs/rpa_cea.log')
    log_cea.info('Acessando rota - /rpa')
    result = {}

    try:
        start = time.time()
        json_data = json.loads(request.data)
        log_cea.info('Carregando dados da request.data')
        result = rpa(json_data, log_cea)
        result["temp"] = "--- %s seconds ---" % (round(time.time() - start, 2))
    except Exception as error:
        log_cea.error('Erro Fatal')
        result['error'] = error

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=False)
