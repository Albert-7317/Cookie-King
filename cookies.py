###details this bot is for cookie clicker by BizzQuit###
###use https://orteil.dashnet.org/cookieclicker/ with page in top left position at 100% zoom###

###imports###
import pyautogui as pag
import time


####function###
def cookieBuffer(buffer):
    for i in range(0,buffer):
        pag.click(284, 482)

def buyWorker(depth):
    y = 1014
    for i in range(0,depth):
        pag.click(1614, y)
        y = y - 64

def buyUpgrade():
    x = 1612
    for i in range(0,5):
        pag.click(x, 187)
        x = x + 70

###main event###
while True:
    time.sleep(5)
    cookieBuffer(300)
    for i in range(0, 20):
        cookieBuffer((15*2))
        buyWorker(3)
        buyUpgrade()
    cookieBuffer(300)
    for i in range(0, 20):
        cookieBuffer((100*2))
        buyWorker(6)
        buyUpgrade()
    for i in range(0, 20):
        cookieBuffer((200*2))
        buyWorker(9)
        buyUpgrade()
    for i in range(0, 20):
        cookieBuffer((250*2))
        buyWorker(9)
        buyUpgrade()
    print('it hath been complete sire')
    
    break