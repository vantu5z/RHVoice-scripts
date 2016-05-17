#!/usr/bin/python
# coding: utf8
# функция для получения погоды из wunderground.com, возвращает текущую температуру и погодные условия
# для работы требуется apikey (ключ), его можно получить пройдя регистрацию на сайте,
# там же можно узнать необходимую метеорологическую станцию

from urllib.request import urlopen
import json

def get_weather(apikey, Station_ID):
  # собираем строку запроса
  req = ('http://api.wunderground.com/api/'+apikey+'/conditions/forecast/lang:RU/q/'+Station_ID+'.json')

  # загружаем данные
  response    = urlopen(req)
  json_data   = response.read().decode()
  parsed_json = json.loads(json_data)

  # выборка нужных данных
  temp_c  = parsed_json['current_observation']['temp_c']	# температура в цельсиях
  weather = parsed_json['current_observation']['weather']	# погодные условия

  # TODO добавить получение: давления, погода на завтра, погода на предстоящие выходные

  temp=str(int(temp_c))   # переводим число в строку

  return temp, weather
