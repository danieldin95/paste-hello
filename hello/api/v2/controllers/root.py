from pecan import abort, expose

# Note: this is *not* thread-safe.  In real life, use a persistent data store.
BOOKS = {
    '0': 'The Last of the Mohicans',
    '1': 'Catch-22'
}


class BookController(object):

    def __init__(self, id_):
        print "BookController.__init__: ", id_
        self.id_ = id_

    @property
    def book(self):
        if self.id_ is None or self.id_ == "":
            return BOOKS
        if self.id_ in BOOKS:
            return dict(id=self.id_, name=BOOKS[self.id_])

    @expose(generic=True, template='json')
    def index(self):
        print "BookController.index: ", self.id_
        return self.book

    @index.when(method='POST', template='json')
    def index_post(self, **kw):
        print "BookController.index_post: ", kw
        BOOKS[self.id_] = kw['name']
        return self.book

    @index.when(method='PUT', template='json')
    def index_put(self, **kw):
        print "BookController.index_put: ", kw
        BOOKS[self.id_] = kw['name']
        return self.book

    @index.when(method='DELETE', template='json')
    def index_delete(self):
        del BOOKS[self.id_]
        return dict()


class RootController(object):

    version_info = {
        'id': 'v2.0',
        'status': 'CURRENT'
    }

    @expose()
    def _lookup(self, *remainder):
        print remainder
        if len(remainder) < 2:
            abort(404)
        if remainder[0] == "book":
            index = remainder[1]
            if index == "":
                remainder = remainder[1:]
            else:
                remainder = remainder[2:]
            return BookController(index), remainder

    @expose(generic=True, template="json")
    def index(self):
        return self.version_info

    @index.when(method="POST")
    @index.when(method="PUT")
    @index.when(method="PATCH")
    @index.when(method="DELETE")
    def not_supported(self):
        abort(405)
