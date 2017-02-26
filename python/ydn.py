import urllib.request
import urllib.parse
import json
import sqlite3

BASEURL = "https://query.yahooapis.com/v1/public/yql?"


def yql(param):
    yql_url = BASEURL + urllib.parse.urlencode(param)
    response = urllib.request.urlopen(yql_url).read()
    return json.loads(response.decode())


def init_conditions(cursor):
    """\
    "condition": {
        "date": "Thu, 02 Feb 2017 04:00 PM AKST",
        "temp": "17",
        "text": "Mostly Sunny",
        "code": "34"
    }
    """
    cursor.execute('''CREATE TABLE IF NOT EXISTS conditions
              (date text, text text, temp real)''')


def format(condition, form):
    def _format():
        for key, type in form:
            yield type(condition[key])
    return tuple(_format())


if __name__ == '__main__':
    # YQLへ送るSQL文などのパラメータを用意しておきます
    param = {
        "q": """\
        SELECT item.condition
            FROM weather.forecast
                WHERE woeid=1118370
                    AND u='c'
        """,
        "format": "json",
        "unit": "c",
    }

    # SQLiteデータベースと接続し、書き込むデータベースを用意します
    with sqlite3.connect('weather.db') as conn:
        cursor = conn.cursor()
        init_conditions(cursor)

        # YQLでweatherデータベースから現在の天気を取得します
        results = yql(param)['query']['results']
        condition = results['channel']['item']['condition']
        print(condition)
        # 取得したデータをSQLiteのデータベース用に加工します
        form = (('date', str), ('text', str), ('temp', float))
        values = format(condition, form)
        print(values)

        # SQLiteに書き込みます
        cursor.execute("INSERT INTO conditions VALUES (?, ?, ?)", values)
