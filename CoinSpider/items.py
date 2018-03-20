# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CoinUrl(scrapy.Item):
    _id = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()


class Coin(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    english_name = scrapy.Field()
    short_name = scrapy.Field()
    chinese_name = scrapy.Field()
    exchanger_count = scrapy.Field()
    publish_time = scrapy.Field()
    publish_name = scrapy.Field()
    white_paper = scrapy.Field()
    website = scrapy.Field()
    block_explorer = scrapy.Field()
    is_token = scrapy.Field()
    ico_price = scrapy.Field()
    description = scrapy.Field()
    market_capitalization = scrapy.Field()  # 流通市值
    publish_count = scrapy.Field()  # 发行量
    market_count = scrapy.Field()  # 流通量
    tx_count = scrapy.Field()  # 交易额
    market_ranking = scrapy.Field()
    tx_ranking = scrapy.Field()
    price = scrapy.Field()
    time = scrapy.Field()
    lowest_price = scrapy.Field()
    highest_price = scrapy.Field()


class ICO(scrapy.Item):
    coin = scrapy.Field()
    status = scrapy.Field()
    token_platform = scrapy.Field()
    ico_dispatch = scrapy.Field()
    invest_ratio = scrapy.Field()
    ico_count = scrapy.Field()
    ico_publish_count = scrapy.Field()
    ico_start_time = scrapy.Field()
    ico_end_time = scrapy.Field()
    market_price = scrapy.Field()
    ico_type = scrapy.Field()
    ico_aims = scrapy.Field()
    ico_amount = scrapy.Field()
    ico_average_price = scrapy.Field()
    ico_finish_count = scrapy.Field()
    ico_finish_amount = scrapy.Field()
    characteristic = scrapy.Field()
    security_audit = scrapy.Field()
    legal_form = scrapy.Field()
    selling_website = scrapy.Field()
    blog = scrapy.Field()
