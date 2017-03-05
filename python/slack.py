import time
from slackclient import SlackClient

APIKEY = 'your api key here'
sc = SlackClient(APIKEY)
sc.rtm_connect()

while True:
    res = sc.rtm_read()
    if res:
        print(res[0], dir(res[0]))
    time.sleep(1)
