# -*- coding: utf-8 -*-

fn="%E9%A6%96%E9%A1%B5-%E8%82%BA%E7%99%8C%E7%BB%BF%E5%AE%9D%E4%B9%A6-%E6%A3%80%E6%9F%A5"
print (fn)

from urllib.parse import quote,unquote
uu = unquote(fn)
print (uu.encode('utf-8').decode('utf-8'))
