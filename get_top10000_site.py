import requests
from bs4 import BeautifulSoup
import bs4
import traceback
import re
import os
import csv
import sys  # 命令行参数


def getHTMLText(url):  # 爬取网页
    kv = {'user-agent': 'Mozilla/5.0'}  # 模拟浏览器
    try:
        r = requests.get(url, headers=kv, timeout=20)
        print(url, r.status_code)  # 抽风返回500
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "the function getHTMLText() is error!"


def getAllUrl(numPage):
    url_lists = []
    for i in range(1,numPage):
        if i == 1:
            url = 'http://top.chinaz.com/all/index.html'
        else:
            url = 'http://top.chinaz.com/all/index_' + str(i) + '.html'
        #print(url)
        url_lists.append(url)
    return url_lists


def saveinfo(infostring):
    num_info = 0
    root = "G://"
    path = root + 'url.csv'
    if not os.path.exists(root):  # 判断根目录是否存在
        os.mkdir(root)

    with open("douban.txt", "w") as f:
        f.write(infostring)

def getAllinfo(info_url_lists):
    info_lists = ''
    rank = 0
    for info_url in info_url_lists:
        text = getHTMLText(info_url)
        soup = BeautifulSoup(text, "html.parser")
        urls = soup.findAll('span', attrs={'class':'col-gray'})

        for url in urls:
            urlstring = str(url.string)

            #print(not "(更新：2018-03-18)".startswith('('))
            if not urlstring.startswith('('):
                rank = rank + 1
                urlstring = str(rank)+','+urlstring
                print(urlstring)
                info_lists=info_lists+urlstring+'\n'

    saveinfo(info_lists)
    
def main():
    page_url_lists = getAllUrl(340)
    getAllinfo(page_url_lists)
main()
