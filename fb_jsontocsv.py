import json
import time
import csv
j_fb = open("/Users/manshan/Documents/fb.json")
data_fb = json.load(j_fb)
convert = lambda x: time.strftime("%Y-%m-%d", time.localtime(x))
d_fb = list(map(convert, data_fb['chart']['result'][0]['timestamp']))
convert2 = lambda x: '{:.2f}'.format(x)
openp = list(map(convert2, data_fb['chart']['result'][0]['indicators']['quote'][0]['open']))
closep = list(map(convert2, data_fb['chart']['result'][0]['indicators']['quote'][0]['close']))
lowp = list(map(convert2, data_fb['chart']['result'][0]['indicators']['quote'][0]['low']))
highp = list(map(convert2, data_fb['chart']['result'][0]['indicators']['quote'][0]['high']))
vol = data_fb['chart']['result'][0]['indicators']['quote'][0]['volume']
z = zip(d_fb, openp, closep, lowp, highp, vol)
header = ['Date', 'Open', 'Close', 'Low', 'High', 'Volume']
fb_data = open("/Users/manshan/Documents/fb.csv", "w")
csv_writer = csv.writer(fb_data)
csv_writer.writerow(header)
for ele in z:
    csv_writer.writerow(ele)
fb_data.close()


