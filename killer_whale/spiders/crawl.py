#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import urllib2
import scrapy
from urlparse import urlparse, urljoin
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from items import myItem
from scrapy.http import Request
from scrapy.exceptions import CloseSpider

class mySpider(CrawlSpider):

    name = 'mySpider'

    def __init__(
        self,
        #algo,
        num,
        directory,
        urls,
        *args,
        **kwargs
        ):

        parsed_url = urlparse(urls)
        domain = str(parsed_url.netloc)
        #self.algo = algo
        self.num = int(num)
        self.directory = ''.join(['../../', directory])
        #self.allowed_domains = [domain]
        self.start_urls = [urls]
        
        # extract all the links on the page and parse them with parse_url 
        self.rules = (Rule(LinkExtractor(allow = ()), callback='parse_url', follow = True),)

        super(mySpider, self).__init__(*args, **kwargs)

        if not os.path.isdir(self.directory):
            os.makedirs(self.directory)

        # make the directory to store the html files in

    def parse_url(self, response):

        if self.num == 0:
            #if there have been self.num files created then close down the spider
            raise CloseSpider('')
            
        else:

            item = myItem()
            item['html'] = response.body
            item['url'] = response.url
            item['links'] = [link.url for link in LinkExtractor().extract_links(response)]
            return item

def main():
    ''' Take first 5 arguments and execute scrapy spider '''

    # obtain current working directory from the path of this script

    cwd = os.path.dirname(os.path.realpath(__file__))

    # get commmand line arguments

    if len(sys.argv) < 4:
        print 'not enough arguments'
        return
    start_urls = sys.argv[1]
    num_page = sys.argv[2]
    dest_dir = sys.argv[3]
    #algo = sys.argv[4]

    args = ' '.join([
        'scrapy',
        'crawl',
        'mySpider',
    #    '-a',
       # 'algo=%s' % algo,
        '-a',
        'num=%s' % num_page,
        '-a',
        'directory=%s' % dest_dir,
        '-a',
        'urls=%s' % start_urls,
        ])

    subprocess.call(args, cwd=cwd, shell=True)


if __name__ == '__main__':
    main()
