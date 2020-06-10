#website blocking
import time

from datetime import datetime as dt

hosts_path="C:\Windows\System32\drivers\etc\hosts"

redirect="127.0.0.1"

website_list=['facebook.com', 'www.facebook.com', 'instagram.com', 'www.instagram.com', 'www.twitter.com', 'twitter.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print(dt.now())
        print("Currently in work mode, social media is blocked")
        time.sleep(5)
    else:
        print("Free time")
        time.sleep(5)
