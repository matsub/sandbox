import os
import bottle
from .label import Label
from bottle import jinja2_view as view
from bottle import (
        abort,
        request,
        )

label = Label(__file__)
label.apply(bottle)
app = bottle.Bottle()

custom_filters = {
        'filters': {
            'titled': lambda s: s.title(),
            },
        }
label.append_template_paths(['templates'])
label.append_filters(custom_filters)

@app.route('/test')
@view('test.html')
def testing():
    return dict(title='test')

@app.route('/add_one/<num:int>')
def add_one(num):
    print(request)
    return "%d + 1 =  %d" % (num, num+1)

@app.route('/ohno')
def ohno():
    abort(404)
