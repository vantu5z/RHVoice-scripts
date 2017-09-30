#!/usr/bin/python
# coding: utf8
# Скрипт получает новости с special.tass.ru и читает их RHVoice
# также хранит последнюю сказанную новость в указанном месте

import string
import sys
import time                             # для задержки

import lxml.html as html

# импорт вспомогательных функций, которые лежат в 'imports'
from imports.get_cur_time import *      # получение времени и склонения часов/минут
from imports.RHVoice_say import *       # чтение текста RHVoice

# =================================================================================

say_time = get_cur_time()               # текущее время в формате строки  "HH час(ов) ММ минут(а)"

# откуда и куда качать новости
url = "http://special.tass.ru/kosmos"
kosmos_last = 'полный_путь_до/tmp/kosmos.last'

news_list = []

# получаем новости
page = html.parse(url)
items = page.xpath('//div[@class = "b-list"]/div[@class = "b-item"]')
for item in items:
  news_list.append([item.xpath('.//h2[@class = "b-item__title"]/a/text()')[0].strip(),
                    item.xpath('.//div[@class = "b-item__text"]/text()')[0].strip()])

# получаем последнюю оглашённую новость в прошлый раз
try:
  f2 = open(kosmos_last, 'r')            # если файл есть, то читаем из него
except:
  f2 = open(kosmos_last, 'w+')           # в случае если файла нет, то создаем
last_line = f2.readline()
last_line = last_line.replace("\n","")   # удаляем символы новой строки, если есть
f2.close()

metka = 0       # метка записи последней новости
metka_new = 0   # метка свежих новостей

# запись последней новости
if len(news_list) > 0:
  f2 = open(kosmos_last, 'w')
  f2.write(news_list[0][0])
  f2.close

# цикл по списку новостей
for item in news_list:
  if item[0] == last_line: break    # прерывание цикла, если новые новости закончились
  if metka_new == 0:
    RHVoice_say("Время " + say_time + ". Свежие новости космонавтики.")
    time.sleep(1)
    metka_new = 1                   # отметка, что вступление уже сказано
  RHVoice_say(item[0])
  RHVoice_say(item[1])
  time.sleep(2)                     # пауза между новостями

# завершающая фраза, если были свежие новости
if metka_new == 1: RHVoice_say("Вот и все новости на этот час. Спасибо за внимание.")
