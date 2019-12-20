import cv2
import time
import json
import win32api
import win32con
import pyautogui as pag
import numpy as np 
from abc import ABC
from abc import abstractmethod


MOVE_X = 140
MOVE_Y = 100
ACCURACY = 0.9
FREEZE_CLICK = 5
TIME_FOR_BATTLE = 100
CONTROL_TEMPLATE = "control"
CONNECTION_TEMPLATE = "connection"
ACTION_TEMPLATE = ["chapter", "start", "clear", "run", "control"]


class Chapter71():
    def __init__(self):
        self.name = "7.1"
        self.fleet_pos = (0, 2)
        self.abstract_map = [[0,3,3,6,3,0,5,5],[10,3,5,5,3,3,5,5],[10,0,5,5,0,3,3,9]]
        
        self.stage_road = [(0,1),(1,1),(1,0),(2,0),(3,0),(4,0),(4,1),(5,1),(5,2),(6,2),(7,2)]
        self.box = None


    def compare_to_screen(self, _img):
        self.box = pag.locateOnScreen("img/{}.png".format(_img), confidence=ACCURACY)

    def find_and_click(self, _img):
        self.compare_to_screen(_img)
        if self.box!=None:
            pag.click(self.box)

    def check(self, _img):
        self.compare_to_screen(_img)
        if self.box!=None:
            pag.moveTo(300, 300)
            pag.dragTo(800, 400, 2, button='left')
            return True        

    def drag_map(self, _direction):
        if _direction == "left":
            pass

        elif _direction == "right":
            pag.drag(-600, 0, 4, button='left')
            pag.move(240, 0)

        elif _direction == "up":
            pass
        elif _direction == "down":
            pass
        else:
            pass

        return pag.position()

    def run(self):
        pag.moveTo(304, 516)

        x, y = pag.position()

        for pos in range(len(self.stage_road)):

            time.sleep(FREEZE_CLICK)
            #move map and recieve new mouse coordinates
            if pos == 5:
                x, y = self.drag_map("right")
            
            #move mouse according to required point from path
            point = self.stage_road[pos]
            if point[0] > self.fleet_pos[0]:
                pag.moveTo(x+MOVE_X, y)
            elif point[0] < self.fleet_pos[0]:
                pag.moveTo(x+MOVE_X*(-1), y)
            else:
                pag.move(None, None)

            if point[1] > self.fleet_pos[1]:
                pag.moveTo(x, y+MOVE_Y)
                pag.move(-5, None)
            elif point[1] < self.fleet_pos[1]:
                pag.moveTo(x, y+MOVE_Y*(-1))
                pag.move(5, None)
            else:
                pag.move(None, None)


            #game auto focuse on boss fleet, so just set mouse on it
            #if len(self.stage_road)-1 == pos:
            #    pag.moveTo(450, 650)

            #try to start battle, save mouse positions and set new fleet position
            pag.click(None, None)
            self.fleet_pos = point
            x, y = pag.position()

            time.sleep(FREEZE_CLICK)
            pag.click(None, None)
    
            self.compare_to_screen("connection")
            if self.box!=None:
                pag.click(self.box)
    
            self.battle()


    def battle(self):
        self.compare_to_screen("battle")
        if self.box!=None:
            pag.click(self.box)

            pag.moveTo(1161, 645)
            time.sleep(TIME_FOR_BATTLE)
            pag.click(None, None)
            time.sleep(FREEZE_CLICK)
            pag.click(None, None)
            time.sleep(FREEZE_CLICK)
            pag.click(None, None)
            time.sleep(FREEZE_CLICK)
            pag.moveTo(1099, 692)
            pag.click(None, None)
            time.sleep(FREEZE_CLICK+5)

            self.compare_to_screen("eliteship")
            if self.box!=None:
                for el in range(2):
                    pag.click(self.box[1])

            self.compare_to_screen("end")
            if self.box!=None:
                pag.click(self.box)
                pag.click(self.box)

            time.sleep(FREEZE_CLICK+3)
            
    def retreat(self):
        self.compare_to_screen("retreat")
        if self.box!=None:
            pag.click(self.box)
            time.sleep(FREEZE_CLICK)
            self.compare_to_screen("retreatconfirm")
            pag.click(self.box)
            time.sleep(FREEZE_CLICK)



class Chapter81():
    def __init__(self):
        self.name = "8.1"
        self.fleet_pos = (0, 0)
        #self.abstract_map = []
        
        self.stage_road = [(0,3),(1,3),(2,3),(3,3),(4,3),(4,2),(5,2),(6,2),(7,2),(7,3)]
        self.box = None


    def compare_to_screen(self, _img):
        self.box = pag.locateOnScreen("img/{}.png".format(_img), confidence=ACCURACY)

    def find_and_click(self, _img):
        self.compare_to_screen(_img)
        if self.box!=None:
            pag.click(self.box)

    def check(self, _img):
        self.compare_to_screen(_img)
        if self.box!=None:
            pag.moveTo(300, 300)
            pag.dragTo(800, 400, 2, button='left')
            return True        

    def drag_map(self, _direction):
        if _direction == "left":
            pass

        elif _direction == "right":
            pag.drag(-600, 0, 4, button='left')
            pag.move(240, 0)

        elif _direction == "up":
            pass
        elif _direction == "down":
            pass
        else:
            pass

        return pag.position()

    def run(self):
        pag.moveTo(369, 400)

        x, y = pag.position()

        for pos in range(len(self.stage_road)):

            time.sleep(FREEZE_CLICK)
            #move map and recieve new mouse coordinates
            if pos == 5:
                x, y = self.drag_map("right")


            self.compare_to_screen("boss")  
            if self.box!=None:
                pag.click(self.box)
                break
            
            #move mouse according to required point from path
            point = self.stage_road[pos]
            if point[0] > self.fleet_pos[0]:
                pag.moveTo(x+MOVE_X, y)
            elif point[0] < self.fleet_pos[0]:
                pag.moveTo(x+MOVE_X*(-1), y)
            else:
                pag.move(None, None)

            if point[1] > self.fleet_pos[1]:
                pag.moveTo(x, y+MOVE_Y)
                pag.move(-5, None)
            elif point[1] < self.fleet_pos[1]:
                pag.moveTo(x, y+MOVE_Y*(-1))
                pag.move(5, None)
            else:
                pag.move(None, None)


            #game auto focuse on boss fleet, so just set mouse on it
            #if len(self.stage_road)-1 == pos:
            #    pag.moveTo(450, 650)

            #try to start battle, save mouse positions and set new fleet position
            pag.click(None, None)
            self.fleet_pos = point
            x, y = pag.position()

            time.sleep(FREEZE_CLICK)
            pag.click(None, None)
            
            time.sleep(FREEZE_CLICK)
            self.compare_to_screen("pos")
            if self.box!=None:
                pag.click(self.box)

            self.compare_to_screen("connection")
            if self.box!=None:
                pag.click(self.box)
    
            self.battle()


    def battle(self):
        self.compare_to_screen("battle")
        if self.box!=None:
            pag.click(self.box)

            pag.moveTo(1161, 645)
            time.sleep(TIME_FOR_BATTLE)
            pag.click(None, None)
            time.sleep(FREEZE_CLICK)
            pag.click(None, None)
            time.sleep(FREEZE_CLICK)
            pag.click(None, None)
            time.sleep(FREEZE_CLICK)
            pag.moveTo(1099, 692)
            pag.click(None, None)
            time.sleep(FREEZE_CLICK+5)

            self.compare_to_screen("eliteship")
            if self.box!=None:
                for el in range(2):
                    pag.click(self.box[1])

            self.compare_to_screen("end")
            if self.box!=None:
                pag.click(self.box)
                pag.click(self.box)

            time.sleep(FREEZE_CLICK+3)
            
    def retreat(self):
        self.compare_to_screen("retreat")
        if self.box!=None:
            pag.click(self.box)
            time.sleep(FREEZE_CLICK)
            self.compare_to_screen("retreatconfirm")
            pag.click(self.box)
            time.sleep(FREEZE_CLICK)


Chapter = Chapter71()


for el in ACTION_TEMPLATE:
    Chapter.find_and_click(el)
    time.sleep(FREEZE_CLICK)
time.sleep(5)

if Chapter.check(CONTROL_TEMPLATE):
    Chapter.run()
    Chapter.retreat()