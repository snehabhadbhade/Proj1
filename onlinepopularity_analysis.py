__author__ = 'snehabhadbhade'

import csv
from collections import defaultdict

infile = open("OnlineNewsPopularity_fb","rU")
reader=csv.reader(infile, dialect="excel", delimiter=",", lineterminator="\n")
reader=csv.DictReader(infile, delimiter=",")

tot_count = defaultdict(int)

for row in reader:
    if row['sentiment'] == 'positive':
        tot_count['positive_publications'] +=1
        tot_count['positive_shares'] += int(row['shares'])
        tot_count['positive_fbshares'] += int(row['fb_shares'])
    if row['sentiment'] == 'negative':
        tot_count['negative_publications'] +=1
        tot_count['negative_shares'] += int(row['shares'])
        tot_count['negative_fbshares'] += int(row['fb_shares'])
    if row['sentiment'] == 'neutral':
        tot_count['neutral_publications'] +=1
        tot_count['neutral_shares'] += int(row['shares'])
        tot_count['neutral_fbshares'] += int(row['fb_shares'])



print tot_count
