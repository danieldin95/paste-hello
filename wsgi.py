#!/usr/bin/env python2

import os
from paste.deploy import loadapp
from pecan.deploy import deploy
from wsgiref.simple_server import make_server

config = os.path.abspath("api-paste.ini")
application = loadapp("config:{}".format(config), "main")

server = make_server('0.0.0.0', 80, application)
server.serve_forever()
