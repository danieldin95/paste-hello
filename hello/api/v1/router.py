from wsgi import Router
from wsgi import Resource


class ControllerTest(object):
    """Controller Test"""
    def __init__(self, *args, **kwargs):
        print "ControllerTest.__init__: ", "args =", args, "kwargs =", kwargs

    def get(self, req):
        print "req", req
        return {
            'name': self.__class__.__name__,
            'properties': self.get.__name__
        }


class MyRouterApp(Router):
    """MyRouteApp"""

    def __init__(self, mapper, *args, **kwargs):
        print "MyRouterApp.__init__: ", "mapper =", mapper, "args =", args, "kwargs =", kwargs
        controller = ControllerTest()
        mapper.connect('/test',
                       controller=Resource(controller),
                       action='get',
                       conditions={'method': ['GET']})
        super(MyRouterApp, self).__init__(mapper)
