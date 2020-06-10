#website blocking
import time
from datetime import datetime as dt

hosts_temp='hosts'
hosts_path="C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=['facebook.com', 'www.facebook.com', 'instagram.com', 'www.instagram.com', 'www.twitter.com', 'twitter.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 7) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23):
        print(dt.now())
        print("Currently in work mode, social media is blocked")
        with open(hosts_temp,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect +' ' + website +'\n')
        time.sleep(5)
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
        print("Free time")
        time.sleep(5)
