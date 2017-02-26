import re
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup as bs


number = re.compile('\d+')


def get_rows(soup):
    """一覧のページから年ごとのtrエレメントを取得します"""
    for row in soup.table.find_all('tr'):
        raw_year = row.td.strong.string
        year = number.search(raw_year).group()
        yield year, row


def get_monthly_page(row):
    """一覧のページから月ごとのURLを取得します"""
    for anchor in row.find_all('a'):
        raw_month = anchor.string
        month = number.search(raw_month).group()
        yield month, anchor['href']


def fetch_excel(url):
    """\
    各月のページから
    「産業，従業上の地位・雇用形態（雇用者については従業者規模）別就業者数」
    のエクセルファイルを取得します。
    """
    src = urllib.request.urlopen(url)
    soup = bs(src, "html.parser")
    # HTMLを読み、目的のデータをもったhtmlエレメントに到達します
    row = soup.find_all('tr')[11]
    data = row.find_all('td')[2]
    # aエレメントが示すURIを取得します
    uri = urllib.parse.urljoin(url, data.a['href'])
    # 取得したURIからファイルを取得します
    return urllib.request.urlopen(uri)


def save_excel(response, year, month):
    # yyyy_mm.xlsという名前で保存します。
    fname = '_'.join([year, month]) + '.xls'
    with open(fname, 'wb') as f:
        f.write(response.read())


if __name__ == '__main__':
    URL = "http://www.e-stat.go.jp/SG1/estat/GL08020102.do" \
        "?_toGL08020102_&tclassID=000000110001&cycleCode=1"
    src = urllib.request.urlopen(URL)
    soup = bs(src, "html.parser")

    for year, row in get_rows(soup):
        for month, url in get_monthly_page(row):
            uri = urllib.parse.urljoin(URL, url)
            res = fetch_excel(uri)
            save_excel(res, year, month)
