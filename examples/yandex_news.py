#!/usr/bin/python
# coding: utf8
# Скрипт получает новости с news.yandex.ru и читает их RHVoice

import string
import sys
import time 				# для задержки
from urllib.request import urlretrieve
# полный путь до следующих скриптов, если они лежат отдельно от основного скрипта
sys.path.insert(0, "полный_путь_до_скриптов/import")
from get_cur_time import *		# включает функцию получения времени и склонения часов/минут
from RHVoice_say import *		# включает функцию чтения текста RHVoice

say_time = get_cur_time()  # получаем текущее время в формате строки  "HH час(ов) ММ минут(а)"

# пытаемся получить новости с Яндекса
try:
 urlretrieve("http://news.yandex.ru/index.rss", '/tmp/yandex.rss')
 f = open('/tmp/yandex.rss', 'r')

 RHVoice_say("Время " + say_time + ". Свежие Яндекс новости.")
 time.sleep(1) 

 line = f.readline()

 while line:

    if "<title>" in line:  # фильтруем по строкам с названием новости
      line = line.strip()  # удаляем лишние пробелы
      line = line.replace("<title>","")
      line = line.replace("</title>",".")

      if line != "Яндекс.Новости: Главные новости." :  # пропускаем строку про главные новости
          print (line)
          RHVoice_say(line)
          time.sleep(1)

    line = f.readline()    # следующая строка

 f.close()

 RHVoice_say("Вот и все новости на этот час. Спасибо за внимание.")

except:
 RHVoice_say("Время " + say_time + ". Новости получить не удалось.")