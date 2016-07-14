#!/usr/bin/python
# coding: utf8
# скрипт предназначен для объявления окончания рабочего дня
# сообщает данные о погоде, а также прогноз на выходные
# пока идут сборы домой - читает цитаты

import string
import time                       # для задержки
import alsaaudio                  # для управления громкостью
import sys
import datetime
# полный путь до следующих скриптов, если они лежат отдельно от основного скрипта
sys.path.insert(0, "полный_путь_до_скриптов/import")
from get_cur_time import *        # для получения времени в нужном формате
from RHVoice_say import *         # для чтения текста RHVoice
from fest_say import *            # для чтения текста Фестевалем
from get_citat import *           # для получения цитаты
from sklon import *               # для склонения числительных
from get_dejurniy import *        # для получения дежурного по дате
from get_weather import *         # для получения погоды

# данные для получения погоды (НЕОБХОДИМО ЗАПОЛНИТЬ!)
apikey = 'ключ'                   # ключ от wunderground.com
Station_ID = 'имя_станции'        # имя станции
# ======

now_date = datetime.datetime.now()                                                # текущая дата со временем
cur_date = str(now_date.day)+"."+str(now_date.month)+"."+str(now_date.year)       # собираем строку с текущей датой
dejurniy = get_dejurniy(cur_date)                                                 # получаем дежурного

# получаем дежурного на завтра
tom_date = now_date + datetime.timedelta(days=1)                                  # завтрашняя дата
tom_date_str = str(tom_date.day)+"."+str(tom_date.month)+"."+str(tom_date.year)
dejurniy_2 = get_dejurniy(tom_date_str)

say_time = get_cur_time()               # получаем текущее время в формате строки "HH час(ов) ММ минут(а)"

text_weekend = ''
# если есть подключение к интернет, то получаем и обрабатываем данные о погоде
try:
  weather = get_weather(apikey, Station_ID)

  grad=sklon(weather[0], "градус", "градуса", "градусов")       # склоняем градус

  # собираем спич
  text = "Время " + say_time + ". За окном " + weather[1] + ". Температура " + str(weather[0]) + " " + grad + ". К вечеру " + weather[2] + "."
  # и прогноз на выходные
  if weather[3]==1:
     text_weekend = "в субботу " + str(weather[4]) + " " + sklon(weather[4], "градус", "градуса", "градусов") + ' и ' + weather[5] + ", а в воскресенье " + str(weather[6]) + " " + sklon(weather[6], "градус", "градуса", "градусов") + " и " + weather[7] + "."

# если нет интернета, то
except:
  text = "Время " + say_time + ". сведения о погоде получить не удалось."

m = alsaaudio.Mixer()   # определяем alsaaudio.Mixer для изменения громкости
m.setvolume(95)         # громкость на 95

fest_say(u"От совецкого информ бюро!")          # на мой взгляд, читает с большим выражением, чем RHVoice

m.setvolume(80)

RHVoice_say(text)
if text_weekend: RHVoice_say(text_weekend)      # если сегодня пятница, то сообщим прогноз на выходные

fest_say(u"Пора начинать собираться домой.")

time.sleep(5)                                   # задержка между сообщениями

# сообщаем кто дежурит сегодня и завтра
if dejurniy == "0": RHVoice_say("Обновите график дежурств.")
else: RHVoice_say("Сегодня дежурит " + dejurniy + ".")

if text_weekend: RHVoice_say("Всем удачных выходых!")   # если завтра точно выходные
else:
   if dejurniy_2 == "0" and dejurniy != "0":            # если есть дежурный на сегодня, а на завтра получить не удалось
         RHVoice_say("Похоже завтра выходной!")         # делаем предположение, что завтра не рабочий день
   elif dejurniy_2 != "0":
      if dejurniy == dejurniy_2:                        # если на завтра тотже дежурный
         RHVoice_say("И завтра тоже.")
      else: RHVoice_say("А завтра будет дежурить " + dejurniy_2 + ".")

m.setvolume(75)
time.sleep(30)

# получаем цитату и говорим её, несколько раз через задержки
try:
 cit = get_citat()
 RHVoice_say(cit)
except:
 time.sleep(5)

time.sleep(30)

try:
 cit = get_citat()
 RHVoice_say(cit)
except:
 time.sleep(5)

time.sleep(40)

try:
 cit = get_citat()
 RHVoice_say(cit)
except:
 time.sleep(5)

time.sleep(60)

try:
 cit = get_citat()
 RHVoice_say(cit)
except:
 time.sleep(5)

time.sleep(70)
m.setvolume(85)

say_time = get_cur_time()

fest_say(u"Эй! Время уже " + say_time + u". Пора сваливать!")
