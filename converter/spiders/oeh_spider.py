import logging

from .base_classes import EduSharingBase


class OEHSpider(EduSharingBase):
    name = "oeh_spider"
    friendlyName = "Open Edu Hub"
    url = "https://redaktion.openeduhub.net/edu-sharing/"
    apiUrl = "https://redaktion.openeduhub.net/edu-sharing/rest/"
    version = "0.1.1"
    mdsId = "mds_oeh"

    def __init__(self, **kwargs):
        EduSharingBase.__init__(self, **kwargs)

    def getBase(self, response):
        base = EduSharingBase.getBase(self, response)
        base.replace_value("type", self.getProperty("ccm:objecttype", response))
        return base


    def getLOMTechnical(self, response):
        technical = EduSharingBase.getLOMTechnical(self, response)
        if "ccm:wwwurl" in response.meta["item"]["properties"]:
            technical.replace_value("format", "text/html")
            technical.replace_value("location", response.meta["item"]["properties"]["ccm:wwwurl"][0])
        return technical


    def shouldImport(self, response=None):
        if "ccm:collection_io_reference" in response.meta["item"]["aspects"]:
            logging.info(
                "Skipping collection_io_reference with id "
                + response.meta["item"]["ref"]["id"]
            )
            return False
        return True
