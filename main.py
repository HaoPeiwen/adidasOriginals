#!/usr/bin/env python
#encoding: utf-8
#author: Peiwen
import time
import itchat
#from itchat.content import *
import re
from configparser import ConfigParser

math_dict = {
    '加':'+',
    '减':'-',
    '乘':'*',
    '除':'/',
    '除以':'/',
    '乘以':'*'
}

config = ConfigParser()
config.read('ID.config', encoding='UTF-8') 

d_id = [config['ID']['Size'], config['ID']['Id'], config['ID']['Phone']]


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def Trans(matched):
    value = matched.group('value')
    if value in math_dict:
        return math_dict[value]
    else:
        return value

def Math(text):
    s = re.search(u"问题：[\S]+=？",text).group()[3:-2]
    m =re.sub(u"(?P<value>[\u4e00-\u9fa5]+)",Trans,s)
    return str(int(eval(m)))


def Example(text):
    pattern = re.compile(u"例如：\S+\n")
    s = re.search(pattern, text).group().split('，')
    s[0] = s[0][3:]
    s[-1] = s[-1][:-1]
    ans = ''
    for i in s:
        if len(i) == 1 and is_number(i):
            ans += d_id[0]+'，'
        elif len(i) == 18 and is_number(i):
            ans += d_id[1]+'，'
        elif len(i) == 11 and is_number(i):
            ans += d_id[2]+'，'
        else:
            ans += i +'，'
    ans = ans[:-1]
    return ans

def YEEZY_repeat(text, city):
    pattern = re.search(u"该城市的", text).group()
    return 'YEEZY'+city

@itchat.msg_register(itchat.content.TEXT, isMpChat=True)
def text_reply(msg):
    flag = 0
    try:
        ans = Math(msg.text)
        flag = 1
    except:
        pass
    try:
        ans = Example(msg.text)
        flag =1
    except:
        pass
    try:
        ans = YEEZY_repeat(msg.text, '上海')
        flag =1
    except:
        pass

    if flag == 1:
        return ans
    
@itchat.msg_register(itchat.content.TEXT)
def reply(msg):
    flag = 0
    try:
        ans = Math(msg.text)
        flag = 1
    except:
        pass
    try:
        ans = Example(msg.text)
        flag =1
    except:
        pass
    try:
        ans = YEEZY_repeat(msg.text, '上海')
        flag =1
    except:
        pass

    if flag == 1:
        return ans
    
itchat.auto_login(hotReload=True)
itchat.run()

