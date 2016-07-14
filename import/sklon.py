#!/usr/bin/python
# coding: utf8
# функция склонения числительного
# например: sklon(18,'градус','градуса','градусов') -> 'градусов'

import string

def sklon(n, form1, form2, form5):

    n = abs(n)		# убираем минус, если есть
    n  = n % 100	# две последних цифры
    n1 = n % 10		# последняя цифра

    if n>10 and n<20 : form=form5
    elif n1>1 and n1<5 : form=form2
    elif n1==1 : form=form1
    else: form=form5

    return form