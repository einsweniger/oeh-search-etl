# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import json
import re
from w3lib.html import replace_escape_chars
import psycopg2
from scrapy.exporters import JsonItemExporter
import io
from datetime import date

class ScrapyPipeline(object):
    def process_item(self, item, spider):
        return item

class JoinLongWhiteSpaceStringsPipeline(object):
    def process_item(self, item, spider):
        if spider.name == "zoerr_spider":
            return item
        if spider.name == "hhu_spider":
            return item
        if item['author']:
            item['author'] = re.sub('  +', ', ', item['author'])
            item['tags'] = " ".join(item['tags'].split())
            return item

class TagPipeline(object):
    def process_item(self, item, spider):
        if item['tags']:
            item['tags'] = item['tags'].replace(" ", ",")
            return item

class NormLinksPipeline(object):
    def process_item(self, item, spider):
        print("Items is: ", item)
        if spider.name == "zoerr_spider":
            return item
        elif item['url']:
            if not any(x in item['url'] for x in ["http://", "https://"]):
                item['url'] = "https://" + item['url']
                return item
            else:
                return item

class NormLicensePipeline(object):
    def process_item(self, item, spider):
        if item['license']:
            if any(x in item["license"].lower() for x in ["cc_0", "cc 0" "cc0", "public domain", "publicdomain", "zero"]):
                item["license"] = "CC 0"
                return item
            elif all(x in item['license'].lower() for x in ["sa", "by"]) and not "nc" in item["license"].lower():
                item["license"] = "CC BY-SA"
                return item
            elif any(x in item['license'].lower() for x in ["sa", "nd", "nc"]) == False:
                item["license"] = "CC BY"
                return item
            elif all(x in item["license"].lower() for x in ["by","sa","nc"]) == True:
                item["license"] = "CC BY-SA-NC"
                return item
            elif all(x in item["license"].lower() for x in ["by", "nc", "nd"]) == True:
                item["license"] = "CC BY-NC-ND"
                return item
            elif "nd" and not "nc" in item["license"].lower():
                item["license"] = "CC BY-ND"
                return item
            elif "nc" in item['license'].lower() and (any(x in item['license'].lower() for x in ["nd", "sa"]) == False):
                item["license"] = "CC BY-NC"
                return item
            else:
                raise DropItem("Missing or unknown license in %s" % item)


class PostgresPipeline(object):

    def __init__(self):
        self.create_connection()

    def open_spider(self, spider):
        spider_name = spider.name
        print(spider_name)

    def create_connection(self):
        self.conn = psycopg2.connect(
            host = 'localhost',
            user = 'search',
            password = 'admin',
            database = 'search'
        )
        self.curr = self.conn.cursor()

    def process_item(self, item, spider):
        self.store_db(item, spider)
        return item

    def store_db(self, item, spider):
        output = io.BytesIO()
        exporter = JsonItemExporter(output)
        exporter.export_item(item)
        #todo build up uuid
        uuid = spider.name+'_'+item['sourceId']
        print(output.getvalue().decode('UTF-8'))
        self.curr.execute("""insert into "references" values (%s,%s,%s,now(),now(),now(),%s,%s)""", (
            uuid,
            spider.name, # source name
            item['sourceId'], # source item identifier
            #date.today(), # first fetched
            #date.today(), # last fetched
            #date.today(), # last modified
            item['hash'], # hash
            output.getvalue().decode('UTF-8') # json
        ))
        output.close()
        self.conn.commit()
