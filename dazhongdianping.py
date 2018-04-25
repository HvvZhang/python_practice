from __future__ import unicode_literals
import requests
import codecs
from bs4 import BeautifulSoup

from lxml import etree
import bs4
import json
import traceback
import re
import os
import csv
import sys  # 命令行参数
import datetime
import ceshi4

def getHTMLText(url):  # 爬取网页
    # proxie = {
    #     'http': '94.181.39.141:53281'
    # }
    s = requests.session()
    kv = {
        'Connection': 'keep-alive',
        'Host': 'www.dianping.com',
        'Referer': 'http://www.dianping.com/shop/2490844/review_all?queryType=sortType&&queryVal=latest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
        }  # 模拟浏览器
    try:
        print(url)
        r = s.get(url, headers=kv, verify=False, timeout=1000) #, proxies = proxie
        print(r)
        print(r.status_code)  # 返回500
        r.raise_for_status()
        # r.encoding = r.apparent_encoding
        r.encoding = 'utf-8'
        print("encoding", r.encoding)
        return r.text

    except:
        return "the function getHTMLText() is error!"

def savejson(data_num):
    pass


def getAllinfo(info_url, data):
    hospital = []
    text = getHTMLText(info_url)
    html = etree.HTML(text)

    # result = etree.tostring(html)
    # print(result.decode("utf-8"))
    id = 0

    mixid_list = html.xpath("//a[@class='praise']/@data-id")

    mix_id_list = []
    url_list = []

    for mixid in mixid_list:
        mix_id = 'dp_'+mixid
        url = 'http://www.dianping.com/review/'+mixid
        mix_id_list.append(mix_id)
        url_list.append(url)
        print(url + mix_id)


    publish_time_list = []
    publishtime_list = html.xpath("//span[@class='time']/text()")
    for time in publishtime_list:
        publish_time = time.strip()
        if('更新于' in publish_time):
            publish_time = publish_time.split('更新于')[-1]
        publish_time_list.append(publish_time)
        print(publish_time)

    board_entry_url = '' # 模拟登陆之后获取

    # 用户名属性值增长
    i = 0
    author_list = []
    for i in range(0,10):
        # author = html.xpath("//a[@data-click-name='用户名0']")
        author = html.xpath("//a[@data-click-name='{}']/text()".format('用户名'+str(i)))[0].strip()
        i += 1
        author_list.append(author)
        print(author)

    # 评论内容
    abstract_list = []
    content_list = []

    contentlist = html.xpath("//div[@class='review-words Hide' or @class='review-words']") #review-truncated-words Hide

    for cl in contentlist:
        content = ''
        fake_content = cl.xpath("text()")
        # print(fake_content)
        for c in fake_content:  # 有些人分段写评论
            content += c.strip();
        abstract = content[:30]
        print(abstract)
        print(content)
        content_list.append(content)
        abstract_list.append(abstract)

    site_name = html.xpath('//div[@class="review-list-header"]/h1/a/text()')
    print(site_name)
    # title 解析
    title_list = []
    score_list = html.xpath("//span[@class='score']")
    for sc in score_list:
        title = ''
        item_list = sc.xpath("span/text()")
        for item in item_list:
            title += item.strip()+' '
        title_list.append(title)
        print(title)


    for i in range(0, 10):
        data = {}
        data["id"] = 0
        data["mix_id"] = mix_id_list[i]
        data["publish_time"] = publish_time_list[i]
        data["url"] = url_list[i]
        data["board_entry_url"] = info_url
        data["channel_id"] = 4
        data["channel_name"] = '论坛'
        data["title"]=title_list[i]
        data["author"] = author_list[i]
        data["site_name"] = site_name[0]+"的点评"
        data["abstract"] = abstract_list[i]
        data["content"] = content_list[i]
        data["insert_time"] =str(datetime.datetime.now()).replace('-','/')[:-7]
        data["comment_count"] = 0
        data["replay_count"] = 0
        data["view_count"] = 0
        data["tags"] = None

        hospital.append(data)


    return hospital

def main():

    url_lists = [
        'http://www.dianping.com/shop/1724896/review_all?queryType=sortType&&queryVal=latest',
        'http://www.dianping.com/shop/1926973/review_all?queryType=sortType&&queryVal=latest',
        'http://www.dianping.com/shop/13875394/review_all?queryType=sortType&&queryVal=latest',
        'http://www.dianping.com/shop/2229967/review_all?queryType=sortType&&queryVal=latest',
        'http://www.dianping.com/shop/24772252/review_all?queryType=sortType&&queryVal=latest',
        'http://www.dianping.com/shop/2490844/review_all?queryType=sortType&&queryVal=latest',
        'http://www.dianping.com/shop/3095878/review_all?queryType=sortType&&queryVal=latest',
    ]
    all_list = []
    for url_info in url_lists:
        data = {'id': 0, 'mix_id': '', 'channel_id': '4', 'channel_name': '论坛', 'publish_time': '', 'url': '',
                'board_entry_url': '', 'title': '', 'author': '', 'site_name': '', 'abstract': '', 'content': '',
                'insert_time': '', 'comment': 0, 'replay_count': 0, 'view_count': 0, 'tags': None}
        # text = getHTMLText(url_info)
        # html = etree.HTML(text)
        # page_num = html.xpath("//span[@class='PageSel']/text()")
        # print(page_num)
        all_list = all_list + getAllinfo(url_info, data)
    fp = codecs.open('data0425_ceshi2.json', 'a+', 'utf-8')
    fp.write(json.dumps(all_list, indent=2, ensure_ascii=False))
    fp.close()

    # for i in range(1):
    #     getAllinfo(ceshi4.all()[i])

    # for page_source in ceshi4.all():
    #     getAllinfo(page_source)

main()
