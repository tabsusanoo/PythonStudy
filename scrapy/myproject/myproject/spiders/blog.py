# -*- coding: utf-8 -*-
import scrapy
from myproject.items import MyprojectItem

class BlogSpider(scrapy.Spider):
    name = 'blog'
    allowed_domains = ['susanoo.me']
    start_urls = ['https://susanoo.me/thoughts/thoughts0519.html']

    def parse(self, response):
        filename = response.url.split("/")[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)
