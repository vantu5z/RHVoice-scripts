#!/usr/bin/python
# coding: utf8
# Здесь производится подготовка текста к передаче в RHVoice,
# удаляются или заменяются символы.
# Необходимо указать расположение словаря "dic_prep.txt".

import string

dic_prep = 'полный_путь_до_словаря/dic_prep.txt'

def prepare_txt(text):

   text = text.replace("\n","")   # удаляем символ новой строки, если есть
 
  # удаляем скобки из текста
   text = text.replace(')','')
   text = text.replace('(','')

  # пробуем подгрузить словарь и исправляем текст в соответствии со словарём
   try:
     f = open(dic_prep, 'r')	
     line = f.readline()

     while line:
      a,b = line.split(" = ")
      text = text.replace(a, b)
      text = text.replace("\n","")
      line = f.readline()
   except:
      print('Ошибка при загрузке или обработке словаря dic_prep')
 
   return text