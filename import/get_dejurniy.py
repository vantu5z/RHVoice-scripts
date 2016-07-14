#!/usr/bin/python
# coding: utf8
# Функция получения дежурного из списка на сегодняшнюю дату
# Если дежурный не найден, то вернётся "0"
# Для работы необходимо указать полный путь до списка дежурных

import string, io

dejurstvo = 'полный_путь_до_списка_дежурных/dejurstvo.txt'

def get_dejurniy(cur_date):

   # подгружаем файл
   f = open(dejurstvo, 'r')
   line = f.readline()
   b = "0"			# если нет дежурного, то вернётся "0"

   # ищем дежурного
   while line:
     if cur_date in line:
       a,b = line.split(" = ")
       b = b.replace("\n","")   # удаляем символ новой строки, если есть
       break
     line = f.readline()

   return b