import oslo_config
import oslo_messaging


# oslo_messaging.get_transport(oslo_config.cfg.CONF, 'rabbit://user:password@master:5672/')
transport = oslo_messaging.get_transport(oslo_config.cfg.CONF)

target = oslo_messaging.Target(topic='hello-rpc')

client = oslo_messaging.RPCClient(transport, target)

ret = client.call(ctxt={}, method='hello', arg='hi')

cctxt = client.prepare(namespace='command', version='1.0')
cctxt.cast({}, 'stop')
