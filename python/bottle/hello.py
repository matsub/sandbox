import os
import bottle
from bottle import ConfigDict
from myapp import hoge

app = bottle.Bottle()
app.merge(hoge.app)

configuration = {
        'default': 'config.DevelopmentConfig',
        'production': 'config.ProductionConfig',
        'development': 'config.DevelopmentConfig',
        'testing': 'config.TestingConfig',
        }


def configure_app(app):
    # specification of configuration
    spec = os.getenv('BOTTLE_CONFIGURATION', 'default')
    app.config.load_module(configuration[spec])

    # SECRET_KEY or something
    app.config.load_config('application.cfg', silent=True)


@app.route('/hello')
def hello():
    return "Hello, World!"


if __name__ == '__main__':
    # configure_app(app)
    app.run(reloader=True, port=8080, debug=True)
