#!/usr/bin/python
# coding: utf8
# Функция чтения текста RHVocie при помощи Speech Dispatcher

import subprocess
from imports.prepare_txt import *       # для подготовки текста

def RHVoice_say(text):

  txt = prepare_txt(text)               # предварительная подготовка текста

# -e, --pipe-mode (Pipe from stdin to stdout plus Speech Dispatcher)
# -w, --wait (Wait till the message is spoken or discarded)
  p = subprocess.Popen(['spd-say', "-e", "-w"], stdin=subprocess.PIPE)
  p.communicate(txt.encode('utf-8'))
