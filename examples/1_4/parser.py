#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
from scrapy.selector import Selector


response = Selector(text=open('example.html').read())
titles = response.xpath(u'//p[re:test(., "公\s*職\s*人\s*員.*表$")]')
for title in titles:
    title_text = title.xpath('normalize-space(string())').extract_first()
    first_table = title.xpath('following-sibling::table[1]')
    print(title_text, first_table)
    p_tags = title.xpath('following::p[string-length(text()) > 0]')
    for p_tag in p_tags:
        p_text = p_tag.xpath('normalize-space(string())').extract_first()
        table_tag = p_tag.xpath('following-sibling::table[1]')
        if re.search(u'公\s*職\s*人\s*員.*表$', p_text):
            break
        print(p_text, table_tag)

    table_tags = title.xpath('following-sibling::table')
    for table_tag in table_tags:
        p_tag = table_tag.xpath('preceding::p[string-length(text()) > 0][1]')
        p_text = p_tag.xpath('normalize-space(string())').extract_first()
        if re.search(u'公\s*職\s*人\s*員.*表$', p_text):
            break
        print(p_text, table_tag)
