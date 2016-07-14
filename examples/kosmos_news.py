#!/usr/bin/python
# coding: utf8
# Скрипт получает новости с sdnnet.ru и читает их RHVoice
# также хранит последнюю сказанную новость в указанном месте

import string
import sys
import time                     # для задержки
import urllib.request
# полный путь до следующих скриптов, если они лежат отдельно от основного скрипта
sys.path.insert(0, "полный_путь_до_скриптов/import")
from get_cur_time import *      # включает функцию получения времени и склонения часов/минут
from RHVoice_say import *       # включает функцию чтения текста RHVoice

say_time = get_cur_time()       # получаем текущее время в формате строки  "HH час(ов) ММ минут(а)" 

# откуда и куда качать новости
url = "http://sdnnet.ru/rss_news/index.rss"
local_filename = '/tmp/kosmos.rss'
kosmos_last = 'полный_путь_до/tmp/kosmos.last'

# получаем новости (представившись Мозилой)
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()
str_h = html.decode(encoding='UTF-8')           # декодируем байты в строку

# записываем во временный файл
f = open(local_filename, 'w+')
f.write(str_h)
f.close()

# получаем последнюю оглашённую новость
try:
  f2 = open(kosmos_last, 'r')            # если файл есть, то читаем из него
except:
  f2 = open(kosmos_last, 'w+')           # в случае если файла нет, то создаем
last_line = f2.readline()
last_line = last_line.replace("\n","")   # удаляем символы новой строки, если есть
f2.close()

metka = 0       # метка записи последней новости
metka_new = 0   # метка свежих новостей

f = open(local_filename, 'r')   # подгружаем временный файл
line = f.readline()             # читаем первую строку из файла

while line:

    if "<title>" in line:                   # фильтруем по строкам с названием новости
      line = line.strip()                   # удаляем лишние пробелы
      line = line.replace("<title>","")
      line = line.replace("</title>",".")   # вконце новости ставим точку 
      line = line.replace("\n","")          # удаляем символы новой строки, если есть

      if line != "Независимый портал космонавтики." :  # пропускаем эту строку
          if metka == 0:
            f2 = open(kosmos_last, 'w')
            f2.write(line)                  # записываем последнюю новость
            f2.close
            metka = 1
          if line == last_line: break       # прерываем цикл "while line", если новые новости закончились
          if metka_new == 0:
            RHVoice_say("Время " + say_time + ". Свежие новости космонавтики.")
            time.sleep(1)
            metka_new = 1                   # ставим отметку, что уже сказали вступление
          RHVoice_say(line)
          time.sleep(1)

    line = f.readline()    # читаем следующую строку

f.close()

# говорим завершающую фразу, если были свежие новости
if metka_new == 1: RHVoice_say("Вот и все новости на этот час. Спасибо за внимание.")
