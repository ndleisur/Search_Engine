# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from scrapy import signals
from scrapy.exporters import BaseItemExporter

class DuplicatesPipeline(object):

    def __init__(self):
        self.urls_scraped = set()

    def process_item(self, item, spider):
        if item['url'] in self.urls_scraped:
            spider.num += 1
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.urls_scraped.add(item['url'])
            
            #name the html file
            filename = '%s.html' % spider.num
            
            #decrease self.num to make sure you create the files
            spider.num -= 1
            
            filepath = ''.join([spider.directory, filename])
            
            with open(filepath, 'wb') as f:
                f.write(item['html'])
            item['html'] = ''
            # write the html source into a file in the specified directory

            index = ''.join([spider.directory, 'index.dat'])
            
            with open(index, 'a') as g:
                g.write(' '.join([filename, item['url'], '\n']))
            # write each html filename and current url to the index.dat file
            item['filename'] = filename
            return item
        
class FilterAndWritePipeline(object):
    
    def __init__(self):
        self.ans = {}
        self.items = []
        self.matches = {}
        
    def process_item(self, item, spider):
        self.matches[item['url']] = item['filename']
        self.items.append(item)
        
    def close_spider(self, spider):
        for item in self.items:
            itemFiles = []
            
            for l in item['links']:
                if l != item['url']:
                    
                    if l in self.matches:
                        itemFiles += [self.matches[l]]
            self.ans[item['filename']] = itemFiles
            
            
        with open('../../graph.dat', 'wb') as g:
            g.write(str(self.ans))       