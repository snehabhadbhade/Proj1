__author__ = 'snehabhadbhade'

import csv
import requests
import json
import time
import urllib2
from xml.etree import ElementTree
import re
from BeautifulSoup import BeautifulSoup


infile = open("OnlineNewsPopularity_sentiment","rU")
reader=csv.reader(infile, dialect="excel", delimiter=",", lineterminator="\n")
reader=csv.DictReader(infile, delimiter=",")

file_records = []
count_records = 1

for row in reader:
    if count_records>500:
        break
    file_record = {}
    news_url = row['url']
    news_url.rstrip()
    file_record['url'] = news_url
    file_record['shares'] = row['shares']
    file_record['sentiment'] = row['sentiment']

    try:
        url="https://graph.facebook.com/fql?q=SELECT total_count FROM link_stat WHERE url=\""+news_url+"\""
        r = requests.get(url)
        text = json.loads(r.text)
        key = text.keys()
        if key[0] != 'error':
            data = text['data']
            for item in data :
                if item['total_count']:
                    total_count = item['total_count']
        else:
            total_count = 'error'
        file_record['fb_shares'] = total_count

    except urllib2.URLError as e:
        file_record['fb_shares'] = 'error'
    time.sleep(5)
    file_records.append(file_record)
    count_records+= 1

fieldnames = ["url","sentiment","shares","fb_shares"]
output_file = open("OnlineNewsPopularity_fb", 'w')
csvwriter = csv.DictWriter(output_file, delimiter=',', fieldnames=fieldnames)
csvwriter.writeheader()
for row in file_records:
    csvwriter.writerow(row)
output_file.close()
