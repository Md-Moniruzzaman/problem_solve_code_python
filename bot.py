
import pyautogui as pg
import time

time.sleep(10)
txt = open('animals.txt', 'r')
a = 'Congratulation apu... !'

for i in txt:
    pg.write(a)
    pg.press('Enter')