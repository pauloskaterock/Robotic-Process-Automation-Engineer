import pyautogui as pyag

from time import sleep
foto_python = pyag.position()
botao_fechar = pyag.position()
from pyautogui import click, doubleClick
from pyautogui import click, moveTo
moveTo(foto_python, duration=1); sleep(0.5); doubleClick(); sleep(2); moveTo(botao_fechar, duration=0.5);click()

