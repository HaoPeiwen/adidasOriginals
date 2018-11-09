#!/usr/bin/env python
#encoding: utf-8
#author: peiwen
import time
import itchat
#from itchat.content import *
import re
from configparser import ConfigParser

d = {
    '加':'+',
    '减':'-',
    '乘':'*',
    '除':'/',
    '除以':'/',
    '乘以':'*'
}

config = ConfigParser()
config.read('ID.config', encoding='UTF-8') 

d_id = [config['ID']['Size'],config['ID']['Id'],config['ID']['Phone']]


def Trans(matched):
    value = matched.group('value')
    if value in d:
        return d[value]
    else:
        return value

def InputS1(s1):
    s = re.search(u"问题：[\S]+=？",s1).group()[3:-2]
    m =re.sub(u"(?P<value>[\u4e00-\u9fa5]+)",Trans,s)
    return str(int(eval(m)))

def InputS2(s2):
    pattern = re.compile(r"([a-zA-Z0-9]+)，([a-zA-Z0-9]+)，([a-zA-Z0-9]+)")
    s = re.search(pattern,s2).group().split('，')
    ans = ''
    for i in s:
        if len(i) == 1:
            ans += d_id[0]+'，'
        elif len(i) == 18:
            ans += d_id[1]+'，'
        elif len(i) == 11:
            ans += d_id[2]+'，'
    ans = ans[:-1]
    return ans

def testsub(s):
    s = re.search(u"本次",s).group()
    return '测试公众号是否监听'



@itchat.msg_register(itchat.content.TEXT, isMpChat=True)
def text_reply(msg):
    flag = 0
    try:
        ans = InputS1(msg.text)
        flag = 1
    except:
        pass
    try:
        ans = InputS2(msg.text)
        flag =1
    except:
        pass
    try:
        ans = testsub(msg.text)
        flag =1
    except:
        pass
    if flag == 1:
        return ans
    
@itchat.msg_register(itchat.content.TEXT)
def reply(msg):
    flag = 0
    try:
        ans = InputS1(msg.text)
        flag = 1
    except:
        pass
    try:
        ans = InputS2(msg.text)
        flag =1
    except:
        pass
    if flag == 1:
        return ans
    
itchat.auto_login(hotReload=True)
itchat.run()

