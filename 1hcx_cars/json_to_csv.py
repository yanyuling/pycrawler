#!/usr/bin/python
#coding:utf-8

import json
import csv
import datetime

"""
  所有的编码转换都需要通过unicode作为桥梁，如果元数据是直接unicode(通过type(s)查看)，直接encode即可
  如果元数据的格式是`str`, 则需要先decode然后再encode
"""

JSON_FILE = 'cars.json'
CSV_FILE = 'cars.csv'

def unicodeToUTF8(src):
  pass

if __name__ == '__main__':
  f  = open(JSON_FILE)
  data = json.load(f)
  f.close()

  f = csv.writer(open(CSV_FILE, 'wb+'))

  for item in data:
    f.writerow([item.get('carNumber',u'\u65e0').encode('utf-8'),
                item.get('insuranceCity', u'\u65e0').encode('utf-8'), 

                datetime.datetime.fromtimestamp(item['createTime']/1000).strftime('%Y-%m-%d %H:%M:%S.%f'),
                datetime.datetime.fromtimestamp(item['updateTime']/1000).strftime('%Y-%m-%d %H:%M:%S.%f'),
                datetime.datetime.fromtimestamp(item['expiredTime']/1000).strftime('%Y-%m-%d %H:%M:%S.%f'),
                datetime.datetime.fromtimestamp(item.get('priceTime',86400000000)/1000).strftime('%Y-%m-%d %H:%M:%S.%f'),

                item['isCompulsoryInsuranceCanBuy'],
                item.get('priceDevice',u'\u65e0').encode('utf-8'),
                item['isBusinessInsuranceCanBuy'],
                item['isPrice'],
                item.get('status', u'\u65e0').encode('utf-8'),
                item.get('carId', 0),
                item.get('userId', 0),
                item.get('planType', u'\u65e0').encode('utf-8'),
                item.get('planDetail', u'\u65e0').encode('utf-8')])
