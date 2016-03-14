__author__ = 'snehabhadbhade'

import csv

#Preprocess OnlineNewsPopularity File:Extract important data

infile = open("OnlineNewsPopularity.csv","rU")
reader=csv.reader(infile, dialect="excel", delimiter=",", lineterminator="\n")
reader=csv.DictReader(infile, delimiter=",")

file_records = []

for row in reader:
    file_record = {}
    file_record['url'] = row['url']
    file_record['n_tokens_title'] = row[' n_tokens_title']
    file_record['num_hrefs'] = row[' num_hrefs']
    file_record['num_images'] = row[' num_imgs']
    file_record['num_videos'] = row[' num_videos']
    file_record['channel_is_lifestyle'] = row[' data_channel_is_lifestyle']
    file_record['channel_is_entertainment'] = row[' data_channel_is_entertainment']
    file_record['channel_is_bus'] = row[' data_channel_is_bus']
    file_record['channel_is_socmed'] = row[' data_channel_is_socmed']
    file_record['channel_is_tech'] = row[' data_channel_is_tech']
    file_record['channel_is_world'] = row[' data_channel_is_world']
    file_record['weekday_is_monday'] = row[' weekday_is_monday']
    file_record['weekday_is_tuesday'] = row[' weekday_is_tuesday']
    file_record['weekday_is_wednesday'] = row[' weekday_is_wednesday']
    file_record['weekday_is_thursday'] = row[' weekday_is_thursday']
    file_record['weekday_is_friday'] = row[' weekday_is_friday']
    file_record['weekday_is_saturday'] = row[' weekday_is_saturday']
    file_record['weekday_is_sunday'] = row[' weekday_is_sunday']
    file_record['is_weekend'] = row[' is_weekend']
    file_record['shares'] = row[' shares']
    file_records.append(file_record)

#Write to a new file

fieldnames = ["url","n_tokens_title","num_hrefs","num_images","num_videos","channel_is_lifestyle", "channel_is_entertainment","channel_is_bus","channel_is_socmed", "channel_is_tech", "channel_is_world", "weekday_is_monday","weekday_is_tuesday","weekday_is_wednesday","weekday_is_thursday","weekday_is_friday","weekday_is_saturday","weekday_is_sunday","is_weekend","shares"]
output_file = open("OnlineNewsPopularity_new", 'w')
csvwriter = csv.DictWriter(output_file, delimiter=',', fieldnames=fieldnames)
csvwriter.writeheader()
for row in file_records:
    csvwriter.writerow(row)
output_file.close()



    

