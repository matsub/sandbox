import sqlite3
import bottle
from bottle import (
    jinja2_template as template,
    request,
)
from bottle_sqlite import SQLitePlugin

app = bottle.Bottle()
PER_PAGE = 10

db = sqlite3.connect('example.db')
USER_TOTAL, = db.execute('SELECT COUNT(*) FROM users').fetchone()


class Test(object):

    def function(self, arg):
        return arg


@app.route('/users/')
@app.route('/users/<page:int>')
def pagination(db, page=0):
    # number of records per page
    per = int(request.query.per or PER_PAGE)
    start, end = page * per, (page + 1) * per

    # fetch records
    users = db.execute(
        'SELECT * FROM users WHERE id >= ? AND id < ?', (start, end))
    keys = ('id', 'name')
    users = (dict(zip(keys, user)) for user in users)

    parameters = {
        'page': page,
        'users': users,
        'has_next': end < USER_TOTAL,
        'query_string': '?' + request.query_string,
    }
    return template("pagination.html", **parameters)


if __name__ == '__main__':
    app.install(SQLitePlugin(dbfile='example.db'))
    app.run(port=8080, reloader=True)
