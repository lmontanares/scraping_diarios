from typing import Tuple
from scrapy.spiders import SitemapSpider
from scrapy.http import Request
import logging
from logzero import logger
from diarios_chile.items import DiariosChileItem
import re
from scrapy.selector import Selector


class SiteMapBiobioChile(SitemapSpider):
    # handle_httpstatus_list = [301]
    name = "biobiochile"
    allowed_domains = ["biobiochile.cl"]
    sitemap_urls = ["https://www.biobiochile.cl/static/sitemap.xml"]
    # sitemap_urls = ["https://www.biobiochile.cl/robots.txt"]
    sitemap_follow = [""]
    sitemap_rules = [
        (r"/noticias/", "parse"),
    ]
    custom_settings = {"REDIRECT_ENABLED": True}

    def parse(self, response):
        item = {}
        item["url"] = response.url
        item["title"] = response.css("title::text").get()
        regex = re.search(r"(\D*)(/\d{4}/\d{2}/\d{2})", response.url)
        item["category"] = "/".join(regex.group(1).split("/")[3:])
        item["date"] = regex.group(2)[1:]
        yield item
