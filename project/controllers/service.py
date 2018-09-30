# -*- coding: utf-8 -*-
from project import app
from flask import jsonify, render_template, request
import logging

DEFAULT_ASYNC = False

@app.route('/security', methods=['POST', 'GET'])
def security():
    logging.info('/security')
    origin = request.remote_addr
    logging.info('Analysis job requested from {}'.format(origin))
    if request.args.get('async', DEFAULT_ASYNC):
        pass # not implemented at this time. Requires callback URL
    else:

        analyzer = SecurityAnalyzer()
        response = {
            'analysis': analyzer.analyze_bytecode(request.args.get('bytecode'))
        }
        return jsonify(response)


class SecurityAnalyzer(object):

    def __init__(self, *args, **kwargs):
        pass

    def analyze_bytecode(self, bytecode):
        analysis = {
            'mythril': self._mythril(bytecode)
        }
        return analysis

    def _mythril(self, bytecode):
        max_depth = 12
        """
        TODO:
            - use mythril (https://github.com/ConsenSys/mythril)
            - use CLI argument for bytecode input and JSON output : myth -xo json -d -c "0x6060" --max-depth 12
            -  Alternatively, bypass the CLI and setup via "import mythril" python code
        """
        mythril_analysis = {
            'config': {
                'max-depth': max_depth
            },
            'results': {
                # TODO put JSON results from mythril here
            }
        }
        return mythril_analysis
