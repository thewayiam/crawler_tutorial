#! /usr/bin/env python
# -*- coding: utf-8 -*-
from scrapy.selector import Selector


response = Selector(text=open('example.html').read())
p_tags = response.xpath('//p')
for p_tag in p_tags:
    p_text = p_tag.xpath('text()').extract_first()
    table_tag = p_tag.xpath('following-sibling::table[1]')
    print p_text, table_tag

table_tags = response.xpath('//table')
for table_tag in table_tags:
    p_tag = table_tag.xpath('preceding-sibling::p[1]')
    p_text = p_tag.xpath('text()').extract_first()
    print p_text, table_tag
