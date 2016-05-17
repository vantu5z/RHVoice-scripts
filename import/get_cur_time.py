#!/usr/bin/python
# coding: utf8
# Функция получения времени в формате строки в виде: "НН час(а,ов) ММ минут(а,ы)"

import string
import datetime
from sklon import *

def get_cur_time():
   # получение текущего времени
    now_time = datetime.datetime.now()	# Текущая дата со временем
    cur_hour = now_time.hour
    cur_minute = now_time.minute
    last_min = cur_minute % 10   	# последняя минута (например 38 -> 8)

    lc_hour = sklon(cur_hour,u' час',u' часа',u' часов')		# склоняем "час"
    lc_minute = sklon(cur_minute,u' минута',u' минуты',u' минут')	# склоняем "минуту"

   # корректровка один и два - на одна, две
    if cur_minute == 1: say_time = str(cur_hour) + lc_hour + u" одна минута"
    elif last_min == 1 and cur_minute != 11: say_time = str(cur_hour) + lc_hour + " " + str(cur_minute-1) + u" одна минута"
    elif cur_minute == 2: say_time = str(cur_hour) + lc_hour + u" две минуты"
    elif last_min == 2 and cur_minute != 12: say_time = str(cur_hour) + lc_hour + " " + str(cur_minute-2) + u" две минуты"
    elif cur_minute == 0: say_time = str(cur_hour) + lc_hour + u" ровно"
    else: say_time = str(cur_hour) + lc_hour + " " + str(cur_minute) + lc_minute

    return say_time