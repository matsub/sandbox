# examples/1_hello/hello.py
from japronto import Application


class App:

    def __init__(self):
        app = Application()
        self.app = app
        self.router = app.router

    def route(self, path):
        def _route(f):
            def __route(*args, **kwargs):
                print(args, kwargs)
                return f(*args, **kwargs)
            self.router.add_route(path, __route)
            return __route
        return _route


app = App()


@app.route('/hello')
def hello(request):
    return request.Response(text='Hello world!')


app.app.run(debug=True)
