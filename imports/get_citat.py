#!/usr/bin/python
# coding: utf8
# Функция получения цитаты из forismatic.com

import pycurl, io

def get_citat():

    data = io.BytesIO()
    c = pycurl.Curl()
    c.setopt(pycurl.POST,1)
    c.setopt(pycurl.WRITEFUNCTION, data.write)
    c.setopt(pycurl.USERAGENT, 'Mozilla/4.0')
    c.setopt(pycurl.POSTFIELDS, 'lang=ru&method=getQuote&format=text')
    c.setopt(pycurl.URL,'http://api.forismatic.com/api/1.0/')
    c.perform()
    c.close
    t = data.getvalue()
    cit = t.decode(encoding='UTF-8')

    return cit
