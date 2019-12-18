import cv2
import time
import win32api
import win32con
import pyautogui
import numpy as np 

class MainControl():
    def __init__(self):
        pass

    def change_chapter(self):
        pass

    def 

'''
FREEZ_BETWEEN_ACTION = 2
FREEZ_BETWEEN_SORTEING = 10

screen = pyautogui.screenshot(region=(0,0, 1366, 768))
img_gray = cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2GRAY)
template = cv2.imread('test_img/chapter.png', 0)
w, h = template.shape[::-1] 
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) 
threshold = 0.8
loc = np.where( res >= threshold)
print("loc =", loc)

for pt in zip(*loc[::-1]): 
    print(pt)
    win32api.SetCursorPos((pt[0]+59, pt[1]+59))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,pt[0]+59,pt[1]+59,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,pt[0]+59,pt[1]+59,0,0)
    cv2.rectangle(img_gray, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
    break
time.sleep(FREEZ_BETWEEN_ACTION)

screen = pyautogui.screenshot(region=(0,0, 1366, 768))
img_gray = cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2GRAY)
template = cv2.imread('test_img/start_sorting.png', 0)
w, h = template.shape[::-1] 
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) 
threshold = 0.8
loc = np.where( res >= threshold)
print("loc =", loc)
for pt in zip(*loc[::-1]): 
    print(pt)
    win32api.SetCursorPos((pt[0]+59, pt[1]+59))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,pt[0]+111,pt[1]+39,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,pt[0]+111,pt[1]+39,0,0)
    cv2.rectangle(img_gray, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
    break
time.sleep(FREEZ_BETWEEN_ACTION)

screen = pyautogui.screenshot(region=(0,0, 1366, 768))
img_gray = cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2GRAY)
template = cv2.imread('test_img/start_sorting.png', 0)
w, h = template.shape[::-1] 
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) 
threshold = 0.8
loc = np.where( res >= threshold)
print("loc =", loc)
for pt in zip(*loc[::-1]): 
    print(pt)
    win32api.SetCursorPos((pt[0]+59, pt[1]+59))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,pt[0]+111,pt[1]+39,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,pt[0]+111,pt[1]+39,0,0)
    cv2.rectangle(img_gray, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
    break
time.sleep(FREEZ_BETWEEN_SORTEING)

screen = pyautogui.screenshot(region=(0,0, 1366, 768))
img_gray = cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2GRAY)
template = cv2.imread('test_img/rock_point.png', 0)
w, h = template.shape[::-1] 
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) 
threshold = 0.8
loc = np.where( res >= threshold)
print("loc =", loc) 
for pt in zip(*loc[::-1]): 
    print(pt)
    win32api.SetCursorPos((pt[0], pt[1]))
    time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,pt[0],pt[1],0,0)
    time.sleep(1)
    win32api.SetCursorPos((pt[0]+500, pt[1]+50))
    time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,pt[0]+500,pt[1]+50,0,0)
    time.sleep(1)
    break
time.sleep(FREEZ_BETWEEN_ACTION)

#cv2.imwrite('test_img/{}.jpg'.format("1"),img_gray) 
'''