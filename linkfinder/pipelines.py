import json
import csv
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class LinkfinderPipeline(object):
#     def process_item(self, item, spider):
#         return item

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('pipelinejson.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

class CsvWriterPipeline(object):

    def __init__(self):
        self.writer = csv.writer(open('pipelinecsv.csv', 'a'), lineterminator='\n')

    def process_item(self, item, spider):
        csv = [item[key] for key in item.keys()]
        self.writer.writerow(csv)
        return item
