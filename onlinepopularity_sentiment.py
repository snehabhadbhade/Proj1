__author__ = 'snehabhadbhade'
import csv
import requests
import json
import time
import urllib2
from BeautifulSoup import BeautifulSoup

url="http://api.datumbox.com/1.0/SentimentAnalysis.json"
r = requests.get(url)

infile = open("OnlineNewsPopularity_new","rU")
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
    try:
        req = urllib2.Request(news_url)
        response = urllib2.urlopen(req)
        the_page = response.read()
        soup = BeautifulSoup(the_page.decode('utf-8'))
        title = soup.title.string
        #print title
        post_data = {'api_key':'54a32fb4057114ad91ee476eb4a89ad4', 'text':title}
        r = requests.post(url, data=post_data)
        text = json.loads(r.text)
        if text['output']['status'] == 0:
            file_record['sentiment'] = 'error'
        else:
            file_record['sentiment'] = text['output']['result']
            #print text['output']['result']
    except urllib2.URLError as e:
        file_record['sentiment'] = 'error'

    time.sleep(5)

    file_records.append(file_record)
    count_records+= 1

fieldnames = ["url","sentiment","shares"]
output_file = open("OnlineNewsPopularity_sentiment", 'w')
csvwriter = csv.DictWriter(output_file, delimiter=',', fieldnames=fieldnames)
csvwriter.writeheader()
for row in file_records:
    csvwriter.writerow(row)
output_file.close()

















