

class Log(object):
    """
    Log Application
    """

    def __init__(self, app, *args, **kws):
        print "Log.__init__:", "args = ", args, "kws =", kws
        self.app = app

    def __call__(self, environ, start_response):
        print "Log.__call__: you can write log."
        return self.app(environ, start_response)

    @classmethod
    def factory(cls, global_conf, **kwargs):
        print 'Log.factory:', 'global_conf =', global_conf, 'kwargs =', kwargs
        return cls
