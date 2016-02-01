#!/usr/bin/python
# coding:utf-8

"""
xpath : http://www.w3school.com.cn/xpath/xpath_syntax.asp
@author : royguo@uworks.cc
"""

import scrapy

class UserSpider(scrapy.Spider):
  name = "YZYW Spider"
  start_urls = ['http://yizaoyiwan.com/users?page=' + str(i) for i in xrange(1,41)]

  def __init__(self):
    pass

  def parse(self, response):
    for href in response.xpath("//div[@class='media-heading']/a/@href").extract():
      full_url = response.urljoin(href)
      yield scrapy.Request(full_url, callback = self.parse_user)

  def parse_user(self, response):
    email_tag = u'邮箱'
    email = response.xpath("//li[label = '%s']/a/text()" % email_tag).extract()
    if len(email) == 1:
      yield {
            'name' : response.xpath("//div[@class='panel-heading']/text()").extract(), 
            'email' : response.xpath("//li[label = '%s']/a/text()" % email_tag).extract()
            }
