from converter.items import *
from .base_classes import LomBase, JSONBase
import json
from converter.constants import Constants
from scrapy.selector import Selector
import scrapy

# Spider to fetch API from Serlo
class TutorySpider(scrapy.Spider, LomBase, JSONBase):
    name = "tutory_spider"
    friendlyName = "tutory"
    url = "https://www.tutory.de/"
    objectUrl = "https://www.tutory.de/bereitstellung/dokument/"
    baseUrl = "https://www.tutory.de/api/v1/share/"
    version = "0.1.1"

    def __init__(self, **kwargs):
        LomBase.__init__(self, **kwargs)

    def start_requests(self):
        url = self.baseUrl + "worksheet?groupSlug=entdecken&pageSize=999999"
        yield scrapy.Request(url=url, callback=self.parseList)

    def parseList(self, response):
        data = json.loads(response.body)
        for j in data["worksheets"]:
            responseCopy = response.replace(url=self.objectUrl + j["id"])
            responseCopy.meta["item"] = j
            if self.hasChanged(responseCopy):
                yield self.parse(responseCopy)

    def getId(self, response):
        return str(response.meta["item"]["id"])

    def getHash(self, response):
        return response.meta["item"]["updatedAt"] + self.version

    def parse(self, response):
        return LomBase.parse(self, response)

    def getBase(self, response):
        base = LomBase.getBase(self, response)
        base.add_value("lastModified", response.meta["item"]["updatedAt"])
        base.add_value(
            "thumbnail",
            self.objectUrl + response.meta["item"]["id"] + ".jpg?width=1000",
        )
        return base

    def getValuespaces(self, response):
        valuespaces = LomBase.getValuespaces(self, response)
        discipline = list(
            map(
                lambda x: x["code"],
                filter(
                    lambda x: x["type"] == "subject",
                    response.meta["item"]["metaValues"],
                ),
            )
        )
        valuespaces.add_value("discipline", discipline)

        valuespaces.add_value("learningResourceType", "worksheet")
        return valuespaces

    def getLicense(self, response):
        license = LomBase.getLicense(self, response)
        license.add_value("internal", Constants.LICENSE_COPYRIGHT_LAW)
        return license

    def getLOMGeneral(self, response):
        general = LomBase.getLOMGeneral(self, response)
        general.add_value("title", response.meta["item"]["name"])
        if 'description' in response.meta["item"]:
            general.add_value("description", response.meta["item"]["description"])
        else:
            html = self.getUrlData(response.url)["html"]
            if html:
                data = (
                    Selector(text=html)
                    .xpath('//ul[contains(@class,"worksheet-pages")]//text()')
                    .getall()
                )
                cutoff = 4
                if len(data) > cutoff:
                    for i in range(cutoff):
                        del data[0]

                text = " ".join(data)
                text = text[:1000]
                general.add_value("description", text)
        return general

    def getLOMTechnical(self, response):
        technical = LomBase.getLOMTechnical(self, response)
        technical.add_value("location", response.url)
        technical.add_value("format", "text/html")
        technical.add_value("size", len(response.body))
        return technical
