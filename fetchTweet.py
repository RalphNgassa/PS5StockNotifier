import os
import tweepy as tw
import pandas as pd

consumer_key= 'a5qTQjjki7HKHWmKEVA4AZ14W'
consumer_secret= 'Zaysb2JWngqx7TBcQtIoV4KACSxlQbYV2aHB9ou26GDSHKf5HC'
access_token= '1222538341041823745-uIEHoafsh5d8DT2urkZkXFQpBmgBPo'
access_token_secret= 'aSkwe1PTopQtx5u9MFYERmlbTQ31CWoPhMgbJswfO7XE3'

uid = "14877019"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

new_search = "ps5"
date_since = "2021-11-08"

async def on_connect():
    
    tweets = tw.Cursor(api.user_timeline,
                   user_id=uid,
                   exclude_replies = True,
                   include_rts=True).items(5)

    for tww in tweets:
        print (tww.text)

await on_connect()
