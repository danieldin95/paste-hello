import json
from webob.response import Response


class JsonResponse(Response):
    """

    """
    def __init__(self, *args, **kwargs):
        super(JsonResponse, self).__init__(*args, **kwargs)
        self.content_type = "application/json"

    def _body__set(self, value=b''):
        value = json.dumps(value)
        super(JsonResponse, self)._body__set(value)

    body = property(fset=_body__set)


class Version(object):
    """
    Version Application
    """
    version_info = {
        'id': 'v2.0',
        'status': 'CURRENT'
    }

    def __init__(self, version, *args, **kws):
        print "Version.__init__:", "args = ", args, "kws =", kws
        self.version = version

    def __call__(self, environ, start_response):
        res = JsonResponse()
        self.version_info['id'] = self.version
        res.body = self.version_info
        return res(environ, start_response)

    @classmethod
    def factory(cls, global_conf, **kwargs):
        print 'Version.factory:', 'global_conf =', global_conf, 'kwargs =', kwargs
        return cls(kwargs['version'])
