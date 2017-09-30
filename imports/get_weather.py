#!/usr/bin/python
# coding: utf8
# Функция для получения погоды с сайта wunderground.com.
# Возвращает текущую температуру и погодные условия,
# а также прогноз на вечер и на выходные.
# Для работы требуется apikey (ключ),
# его можно получить пройдя регистрацию на сайте,
# там же можно узнать необходимую метеорологическую станцию.

from urllib.request import urlopen
import json
import datetime

def get(apikey, Station_ID):
  # собираем строку запроса
  req = ('http://api.wunderground.com/api/' + apikey +
         '/conditions/forecast/lang:RU/q/' + Station_ID + '.json')

  # загружаем данные
  response    = urlopen(req)
  json_data   = response.read().decode()
  parsed_json = json.loads(json_data)

  # выборка текущих данных о погоде
  # температура в цельсиях
  temp_c  = int(parsed_json['current_observation']['temp_c'])
  # погодные условия
  weather_now = parsed_json['current_observation']['weather']

  # получаем дату на сегодняшний день
  now_date = datetime.datetime.now()
  cur_day = now_date.day                # в виде числа

  sat_prognoz = ''
  fr_mark = 0                           # отметка, что сегодня пятница
  sub_temp = ''
  sub_prognoz = ''
  vos_temp = ''
  vos_prognoz = ''

  # получение прогноза на сегодня и на выходные
  for day in parsed_json['forecast']['simpleforecast']['forecastday']:

     # погодные условия на сегодняшний вечер
     if cur_day==day['date']['day']:
          weather_today = day['conditions']
          if day['date']['weekday']=='Пятница':  fr_mark = 1

     # прогноз на субботу
     if day['date']['weekday']=='Суббота':
          sub_prognoz = day['conditions']
          sub_temp = int(day['high']['celsius'])

     # прогноз на воскресенье
     if day['date']['weekday']=='Воскресенье':
          vos_prognoz = day['conditions']
          vos_temp = int(day['high']['celsius'])

  return temp_c, weather_now, weather_today, fr_mark, sub_temp, sub_prognoz, vos_temp, vos_prognoz
