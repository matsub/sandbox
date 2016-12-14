import os
import bottle


class Label:
    def __init__(self, fname):
        self.dir = os.path.dirname( os.path.abspath(fname) )
        self.template_lookup = set(['./', './views/'])
        self.filters = {}
        self.secret_key = None

    def append_template_paths(self, dirs):
        template_lookup = ( os.path.join(self.dir, dir) for dir in dirs )
        self.template_lookup.add(*template_lookup)

    def append_filters(self, filters):
        self.filters.update(filters)

    def apply(self, bottle):
        # extend filters
        def template(f):
            def wrapper(*args, **kwargs):
                if 'filters' in kwargs:
                    kwargs['filters'].update(self.filters)
                else:
                    kwargs['filters'] = self.filters
                kwargs['template_adapter'] = bottle.Jinja2Template
                kwargs['template_lookup'] = self.template_lookup
                print('!!!!!!!!!!!!!!!!!!',kwargs['template_lookup'])
                return f(*args, **kwargs)
            return wrapper
        bottle.template = template(bottle.template)

        # make all cookies secretly automatically
        def auto_decode(f):
            def wrapper(*args, **kwargs):
                if self.secret_key and 'secret' not in kwargs:
                        kwargs['secret'] = self.secret_key
                return f(*args, **kwargs)
            return wrapper

        bottle.request.get_cookie = auto_decode(bottle.request.get_cookie)
        bottle.response.set_cookie = auto_decode(bottle.response.set_cookie)
