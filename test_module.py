import cv2
import time
import json
import win32api
import win32con
import pyautogui as pag
import numpy as np 
from abc import ABC
from abc import abstractmethod


FREEZE = time.sleep

MOVE_X = 140
MOVE_Y = 100

ACCURACY = 0.8
CLICK_TIME = 5

#first drag to find base position
DRAG_MAP_X = 600
DRAG_MAP_Y = 0

#common drag to make available parts of map
MOVE_MAP_X = 600
MOVE_MAP_Y = 0

TIME_TO_DRAG = -1

FIRST_CELL_X = 90
FIRST_CELL_Y = 0

DRAG_ERROR_X = 220
#MOVE_ERROR_Y = 0

TIME_FOR_BATTLE = 120

CONTROL_TEMPLATE = "control"
CONNECTION_TEMPLATE = "connection"
SPETIAL_TEMPLATE = ["stage", "angle_1"]
START_CHAPTER_TEMPLATE = ["stage", "start", "run"]

"""
    MOVE__TO - means move to x and y
    MOVE__   - meand add x and y to existed coordinates
"""

"""
abstract map is a map of selected chapter
used to check where enemes ships located and where ships already sunk
cells can be(fleet position and fleet spawns equal to 0):

0 - empty
1 - enemy
2 - boss
-1 - sunk emeny
5 - block
"""

class Chapter71():
    def __init__(self):
        self.name = "7.1"
        self.fleet_pos = (0, 2)
        #self.abstract_map = [[0,3,3,6,3,0,5,5],[10,3,5,5,3,3,5,5],[10,0,5,5,0,3,3,9]]
        
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


class Chapter():
    def __init__(self, _name):
        self.name = _name

        self.box = None
        self.boss = False
        self.dragged = False 
        
        self.fleet_pos = []
        self.stage_road = []
        self.abstract_map = []
        self.control_point = []

    def compare_to_screen(self, _img, _folder=""):
        self.box = pag.locateOnScreen("img/{}{}.png".format(_folder, _img), confidence=ACCURACY)
    
    def find_and_click(self, _img):
        if _img in SPETIAL_TEMPLATE:
            self.compare_to_screen(_img, self.name+"/")
        else:
            self.compare_to_screen(_img)

        if self.box!=None:
            pag.click(self.box)
            FREEZE(CLICK_TIME)

            return True
        return False

    def load_data(self):
        with open('data/settings.json', 'r') as file:
            data = json.load(file)[self.name]

            self.dragged = data["drag"]
            self.fleet_pos = data["fleet"]
            self.stage_road = data["path"]
            self.abstract_map = data["map"]
            self.control_point = data["point"]

            CLICK_TIME = data["wait_click"]
            TIME_FOR_BATTLE = data["wait_battle"]

    def start(self):
        for image in START_CHAPTER_TEMPLATE:
            self.find_and_click(image)

    def move_next(self, position):
        self.box = None
        for _ in range(3):
            self.box = pag.locateOnScreen("img/{}/{}.png".format(self.name, "control"), confidence=ACCURACY)
            if self.box!=None:
                pag.moveTo(self.box)
                x, y = pag.position()

                new_x = (position[0]-self.control_point[0])*MOVE_X
                new_y = (position[1]-self.control_point[1])*MOVE_Y    
                pag.moveTo(x+new_x, y+new_y)
                
                pag.click()
                FREEZE(CLICK_TIME)
                pag.click()
                FREEZE(CLICK_TIME)
                break

            else:
                FREEZE(CLICK_TIME)

    def run(self):
        for point in self.stage_road:
            self.move_next(point)

            #special gameplay - connection errors, ambush, commisions
            self.find_and_click("confirm")
            self.find_and_click("ambush")
            self.find_and_click("confirm")
            
            if self.find_and_click("boss"):
                self.boss = True

            if self.find_and_click("battle"):
                FREEZE(TIME_FOR_BATTLE)
                for _ in range(3):
                    pag.click()
                    FREEZE(CLICK_TIME)

                self.find_and_click("end")

            if self.boss:
                self.retreat()
                break
        self.retreat()

    def retreat(self):
        self.find_and_click("retreat")
        self.find_and_click("confirm")


class ControlPlay():
    """class is for selecting chapters
        and control game process such as ambush and connection errors"""
    def __init__(self):
        self.chapter = None 

    def set_chapter(self, chapter):
        self.chapter = chapter
        self.chapter.load_data()
        self.chapter.start()

    def clear_chapter(self):
        self.chapter.run()



Play = ControlPlay()
chapter = Chapter("8.1")

Play.set_chapter(chapter)
Play.clear_chapter()

