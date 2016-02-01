#!/usr/bin/python
#coding:utf-8

import json
import csv

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

  for item in data[1:10]:
    print item['carNumber'].encode('utf-8')
    f.writerow([item['carNumber'].encode('utf-8'), 
                item['insuranceCity'].encode('utf-8'), 
                item['createTime'],
                item['updateTime'],
                item['status']])
