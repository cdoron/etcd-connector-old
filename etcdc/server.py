#
# Copyright 2022 IBM Corp.
# SPDX-License-Identifier: Apache-2.0
#

from fybrik_python_logging import init_logger, logger, DataSetID, ForUser
from .config import Config

import cherrypy
import json

@cherrypy.expose
class EtcdConnectorService(object):

    @cherrypy.tools.accept(media='application/json')
    def POST(self):
        logger.trace("got POST request")
        rawData = cherrypy.request.body.read(int(cherrypy.request.headers['Content-Length']))
        b = json.loads(rawData)
        return json.dumps({'x': 4, 'c': b})

class EtcdConnectorServer():
    def __init__(self, config_path: str, port: int, loglevel: str, *args, **kwargs):
        self.port = port
        with Config(config_path) as config:
            init_logger(loglevel, config.app_uuid, 'etcd-connector')

    def start(self):
        conf = {
            '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            }
        }
        cherrypy.config.update({'log.screen': False,
                        'log.access_file': '',
                        'log.error_file': '',
                        'server.socket_port': self.port})
        cherrypy.quickstart(EtcdConnectorService(), '/', conf)
        logger.trace("EtcdConnectorService started")
        
