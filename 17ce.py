#!/usr/bin/env python
# coding=utf-8

import urllib
import json
import time
import hashlib
import requests
import ast
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


#testUrl = 'www.acfun.com'
testUrl = raw_input('请输入您要测试的网址：')


headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
            'Referer':'http://www.17ce.com/',
            'Origin':'http://www.17ce.com',
            'Content-type':'application/x-www-form-urlencoded',
            'Host':'www.17ce.com',
            'Connection':'keep-alive',
            'Accept':'*/*',
            'DNT':'1'
        }


#获取POST后网页返回的数据
def getPage(url, post, headers):
    #获取response

    response = requests.post(url, data = post, headers = headers)

    page = response.content
    # s = Session()
    # req = Request('POST', url, data = post, headers = headers)
    # prepped = req.prepare()
    # resp = s.send(prepped)
    # page = resp.content

    data = ast.literal_eval(page)
    datas = json.dumps(data,ensure_ascii=False)
    jsondatas = json.loads(datas)
    return jsondatas




#发送第一次POST所获得数据
def getFirstData():
    #POST地址
    targetUrl = 'http://www.17ce.com/site/http'
    #post = urllib.urlencode(post1)
    #print post
    verify=hashlib.sha1("C^dLMi%r&JH7bkmdFCgGl8" + testUrl + "1" +"TnvST&D9LJ").hexdigest()
    urlEncoded = urllib.quote(testUrl)
    post = '&url=%s&curl=&rt=1&nocache=0&host=&referer=&cookie=&agent=&speed=&postfield=&verify=%s&pingcount=&pingsize=&area[]=0&area[]=1&area[]=2&area[]=3&&isp[]=0&isp[]=1&isp[]=2&isp[]=6&isp[]=7&isp[]=8&isp[]=4&'%(urlEncoded,verify)
    #print post
    #pdb.set_trace()
    #以dict形式获取到所需的数据
    data = getPage(targetUrl, post, headers)
    #print data
    #print data['tid']
    return data['tid']

def getSecondData():
    #此处获得的是对应输入网址的post表单信息，获得对于该网址的关键
    tids = getFirstData()
    #第二个POST表单
    post2 = {
        'tid':tids,

        'num':'1',

        'ajax_over':'0'
    }
    post = urllib.urlencode(post2)
    #第二个POST网址
    targetUrl = 'http://www.17ce.com/site/ajaxfresh'
    #以dict形式获取到所需的数据
    datas = {}
    for i in range(60):

        time.sleep(1)
        datas.update(getPage(targetUrl, post, headers))
    #datas = getPage(targetUrl, post, headers)
    #print datas
    data = datas['freshdata']
    #print type(data)
    #print data
    for key , value in data.items():
        print value['name'], value['speed']




if __name__ == '__main__':
    getSecondData()
