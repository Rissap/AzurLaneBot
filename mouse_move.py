import time
import random
import win32api
import win32con
'''import pyautogui
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt'''


def click(x, y):
    win32api.SetCursorPos((x,y))
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)    
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

#time.sleep(5)
for x in range(2):
    #screen = pyautogui.screenshot(region=(0,0, 1366, 768))
    #image = cv.cvtColor(np.array(screen), cv.COLOR_RGB2BGR)
    #cv.imwrite("tmp.png", image)

    click(random.randint(0, 1200), random.randint(0, 700))
    time.sleep(1)