#!/usr/bin/python
# coding: utf8
# Скрипт получает новости с news.yandex.ru и читает их RHVoice

import string
import sys
import time                             # для задержки
from urllib.request import urlretrieve
# импортируем вспомогательные функции, которые лежат в 'imports'
from imports.get_cur_time import *      # включает функцию получения времени и склонения часов/минут
from imports.RHVoice_say import *       # включает функцию чтения текста RHVoice

say_time = get_cur_time()               # получаем текущее время в формате строки  "HH час(ов) ММ минут(а)"

# пытаемся получить новости с Яндекса
try:
  urlretrieve("http://news.yandex.ru/index.rss", '/tmp/yandex.rss')
  f = open('/tmp/yandex.rss', 'r')

  RHVoice_say("Время " + say_time + ". Свежие Яндекс новости.")
  time.sleep(1) 

  line = f.readline()

  while line:

    if "<title>" in line:                               # фильтруем по строкам с названием новости
      line = line.strip()                               # удаляем лишние пробелы
      line = line.replace("<title>","")
      line = line.replace("</title>",".")

      if line != "Яндекс.Новости: Главное." :   # пропускаем строку про главные новости
          print (line)
          RHVoice_say(line)
          time.sleep(1)
          
    if "<link>" in line:                                 # фильтруем по строкам с ссылкой на новость
      line = line.strip()
      line = line.replace("<link>","")
      line = line.replace("</link>","")

      if line != "https://news.yandex.ru/index.html?from=rss" :   # пропускаем лишние строки
        print (line + "\n")
      
    line = f.readline()    # следующая строка

  f.close()

  RHVoice_say("Вот и все новости на этот час. Спасибо за внимание.")

except:
  RHVoice_say("Время " + say_time + ". Новости получить не удалось.")
