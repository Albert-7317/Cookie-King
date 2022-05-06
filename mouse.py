import pyautogui as pag
import time

def mousePos():
    x, y = pag.position()
    print(x, y)
    pag.click(x, y)

time.sleep(5)
mousePos()

