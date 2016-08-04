#!/usr/bin/python
# coding: utf8
# Функция получения времени в формате строки в виде: "НН час(а,ов) ММ минут(а,ы)"

import string
import datetime
from imports.sklon import *

def get_cur_time():
    # получение текущего времени
    now_time = datetime.datetime.now()                           # текущая дата со временем
    cur_hour = now_time.hour
    cur_minute = now_time.minute
    last_min = cur_minute % 10                                   # последняя минута (например 38 -> 8)

    lc_hour = sklon(cur_hour,' час',' часа',' часов')            # склоняем "час"
    lc_minute = sklon(cur_minute,' минута',' минуты',' минут')   # склоняем "минуту"

    # корректровка один и два - на одна, две
    if cur_minute == 1: say_time = str(cur_hour) + lc_hour + " одна минута"
    elif last_min == 1 and cur_minute != 11: say_time = str(cur_hour) + lc_hour + " " + str(cur_minute-1) + " одна минута"
    elif cur_minute == 2: say_time = str(cur_hour) + lc_hour + " две минуты"
    elif last_min == 2 and cur_minute != 12: say_time = str(cur_hour) + lc_hour + " " + str(cur_minute-2) + " две минуты"
    elif cur_minute == 0: say_time = str(cur_hour) + lc_hour + " ровно"
    else: say_time = str(cur_hour) + lc_hour + " " + str(cur_minute) + lc_minute

    return say_time
