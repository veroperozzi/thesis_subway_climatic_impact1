import datetime
import json

import tweepy

consumer_key = "IslodTkwkR6UzGQ05C2FeqB8Y"
consumer_secret = "mmWVU4u5Nb0xjqjeIiES2jXDDT4Yyf6qGDvlqXHh0Sl2mp9qtd"
access_token = "1604255615261593601-SWpvX6OrluCLKEhAdvtjofJp0Hl66x"
access_token_secret = "up3EbPsyKhSYkR2UXTA3kwlvNyOUfxIZUl2FroIpglpY8"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

start_date = datetime.datetime(2023, 1, 1, 10, 00, 00)
end_date = datetime.datetime(2023, 1, 1, 13, 00, 00)

api = tweepy.API(auth)

headers = ['date', 'time', 'precipitation']
f = open('clima.csv', 'w')

rows = []

screenName = "@SMN_OCBA"
for tweet in tweepy.Cursor(api.user_timeline, screen_name=screenName, since=start_date, until=end_date).items():
    x = json.dumps(tweet._json)
    y = json.loads(x)
    print("Y", y)
    print("Fecha ", y["created_at"])
    fecha = y["created_at"]
    test = y["text"]
    list = test.splitlines()
    if (len(list) - 2 >= 0):
        precipitacion = list[len(list) - 2:len(list) - 1]
        print(" List ", list)
        from datetime import datetime

        fecha = datetime.strptime(fecha, '%a %b %d %H:%M:%S %z %Y')
        date = fecha.strftime('%d-%m-%y')
        time = fecha.strftime('%H:%M:%S')
        print(" TWEET -------------------------------------------")
        print("data :", date)
        print("time :", time)
        precipitacionStr = ''.join(precipitacion[0])
        print("precipitacion : ", precipitacionStr)
        print("--------------------------------------------------")
        myJson = []
        myJson.append(date)
        myJson.append(time)
        myJson.append(precipitacionStr)
        rows.append(myJson)

# tweets = api.user_timeline(screen_name=screenName, count=100)
# tweets_for_csv = [[tweet.text.encode("utf-8")] for tweet in tweets]


import csv

with open('clima.csv', 'w') as f1:
    writer = csv.writer(f1, delimiter=',', lineterminator='\n', )
    writer.writerow(headers)
    for row in rows:
        writer.writerow(row)


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")