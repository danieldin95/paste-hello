import time

import oslo_config
import oslo_messaging


class CommandEndpoint(object):
    """"""
    target = oslo_messaging.Target(namespace='command', version='1.0')

    def __init__(self):
        """"""

    def stop(self, ctx):
        print "CommandEndpoint.stop:", ctx


class HelloEndpoint(object):
    """"""

    def hello(self, ctx, arg):
        print "HelloEndpoint.hello:", ctx, arg
        return arg


for (k, v) in oslo_config.cfg.CONF.items():
    print k, v

transport = oslo_messaging.get_transport(oslo_config.cfg.CONF)

target = oslo_messaging.Target(topic='hello-rpc', server='master')

endpoints = [
    CommandEndpoint(),
    HelloEndpoint(),
]

rpc_server = oslo_messaging.get_rpc_server(transport,
                                           target,
                                           endpoints,
                                           executor='blocking')
try:
    rpc_server.start()
    while True:
        time.sleep(0.5)
except KeyboardInterrupt as e:
    print e

rpc_server.stop()
rpc_server.wait()
