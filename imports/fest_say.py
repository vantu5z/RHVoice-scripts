#!/usr/bin/python
# coding: utf8
# Функция чтения текста Фестивалем

import subprocess

def fest_say(text):
    p = subprocess.Popen(
        ['festival', "--tts", "--language", "russian"], 
        stdin=subprocess.PIPE, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, close_fds=True)
    stdout, stderr = p.communicate(text.encode('utf-8'))
