#!/usr/bin/python
# coding:utf-8

"""
xpath : http://www.w3school.com.cn/xpath/xpath_syntax.asp
scrapy docs : http://doc.scrapy.org/en/1.0/intro/examples.html
commands:
  run : 
    scrapy runspider stackoverflow_spider.py -o top-stackoverflow-questions.json
  debug console:
    scrapy shell "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"    
    

@author : royguo@uworks.cc
"""

import scrapy
from settings import COOKIES,HOST

class CarSpider(scrapy.Spider):
  name = "某车险 Spider"
  # if you use start_requests, then start_urls is not nessesary
  # start_urls = ['http://ms.1hcx.com/do?sessionId=253703d5047f0dea09a872e14cf1077c']

  def __init__(self):
    pass

  # This method must return an iterable with the first Requests to crawl for this spider.
  def start_requests(self):
    return [scrapy.Request("%s/do?sessionId=%s" % (HOST, COOKIES['sessionId']),
                               method = 'POST',
                               headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                                          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36',
                                          'Content-Type':'application/x-www-form-urlencoded'},
                               body = u'apiName=com.one.cims.inquiry.list&pageNo=%s&pageSize=10&status=FINISH' % page,
                               cookies = COOKIES,
                               callback=self.parse_item) for page in range(1,6880)]

  # not used
  def parse(self, response):
    pass

  def parse_item(self, response):
    self.logger.info(response.body)
    # inspect response using scrapy shell
#    from scrapy.shell import inspect_response
#    inspect_response(response, self)
    import json
    car_list = json.loads(response.body_as_unicode())['data']['list']
    for car in car_list:
      yield car

