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

ACCURACY = 0.9
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
        self.fleet_pos = (0, 3)
        self.control_point =  (5, 2)
        self.loop_index = 0
        self.battle_amount = 0
        self.dragged = 1 #part of map where camera is located

        self.abstract_map = [[0,0,5,5,1,0,1,1,5],[0,0,5,5,1,0,1,0,1],[0,1,1,0,1,5,1,1,1]]
        self.stage_road = [(0,2),(1,2),(2,2),(3,2),(4,2),(4,1),(4,0),(5,0),(6,0),(6,1),(6,2),(7,2),(8,2),(7,0)]
        self.box = None


    def compare_to_screen(self, _img, _folder=False):
        '''if it's special img, find it in folder callde by a chapter name
        or it's common img'''
        if _folder:
            self.box = pag.locateOnScreen("img/{}/{}.png".format(self.name, _img), confidence=ACCURACY)
        else:
            self.box = pag.locateOnScreen("img/{}.png".format(_img), confidence=ACCURACY)

    def set_first_mouse_position(self):
        """set mouse and fleet to the first cell"""
        screen_size = pag.size()
        pag.moveTo(screen_size[0]/2, screen_size[1]/2)
        self.drag_map(DRAG_MAP_X, DRAG_MAP_Y)

        self.find_and_click("angle")
        pag.move(FIRST_CELL_X, FIRST_CELL_Y)
        pag.click()
        FREEZE(CLICK_TIME)

    def find_and_click(self, _img):
        #check if template from unique folder or is common
        if _img in SPETIAL_TEMPLATE:
            self.compare_to_screen(_img, True)
        else:
            self.compare_to_screen(_img)

        if self.box!=None:
            if _img=="clear":
                pag.moveTo(self.box)
                pag.move(None, 145)
                pag.click()
            else:
                pag.click(self.box)

    def check(self, _img):
        self.compare_to_screen(_img)
        if self.box!=None:
            pag.moveTo(300, 300)
            pag.dragTo(800, 400, 2, button='left')
            return True        

    def drag_map(self, x, y):
        pag.drag(x, y, 1, button='left')

    def drag_this_map(self, position):
        """common drag map to move at the big fields"""
        #forward && backward
        if position == "forward":
            pos = pag.position()
            pag.drag(-MOVE_MAP_X, 0, 1, button="left")
            pag.move(DRAG_ERROR_X, None)
        else:
            pos = pag.position()
            pag.drag(MOVE_MAP_X, 0, 1, button="left")
            pag.move(-DRAG_ERROR_X, None)

    def in_battle(self):
        self.compare_to_screen("in_battle")
        if self.box!=None:
            return True
        return False

    def move_next(self):
        #find an control point
        box = pag.locateOnScreen("img/{}/{}.png".format(self.name, "control_point"), confidence=ACCURACY)
        pag.moveTo(box)
        x, y = pag.position()

        if self.loop_index == TIME_TO_DRAG:
            self.drag_this_map("forward")


        if self.loop_index+1 < len(self.stage_road):
            position = self.stage_road[self.loop_index]
            if position == (8,2):
                FREEZE(1)
                pag.click()

            self.loop_index+=1            
            new_x = (position[0]-self.control_point[0])*MOVE_X
            new_y = (position[1]-self.control_point[1])*MOVE_Y
            
            pag.moveTo(x+new_x, y+new_y)
            pag.click()
            

    def run(self):
        for pos in range(len(self.stage_road)):
            #drag to another part of map
            #can be dragged a few times in different sides
            #also, calculate new mouse position
            self.compare_to_screen("connection")
            if self.box!=None:
                pag.click(self.box)
                time.sleep(10)

            if pos == TIME_TO_DRAG:
                self.drag_this_map("forward")

            #save mouse position
            x, y = pag.position()

            '''
            self.compare_to_screen("boss")  
            if self.box!=None:
                pag.click(self.box)
                break
            '''
            #move mouse according to required point from path
            point = self.stage_road[pos]
            if point[0] > self.fleet_pos[0]:
                pag.moveTo(x+MOVE_X, y)
            elif point[0] < self.fleet_pos[0]:
                pag.moveTo(x+MOVE_X*(-1), y)
            else:
                pass

            if point[1] > self.fleet_pos[1]:
                pag.moveTo(x, y+MOVE_Y)
            elif point[1] < self.fleet_pos[1]:
                pag.moveTo(x, y+MOVE_Y*(-1))
            else:
                pass

            pag.click(None, None)
            time.sleep(FREEZE_CLICK+5)
            #if ambush
            x, y = pag.position()
            self.check_ambush()
            pag.moveTo(x, y)
            #or aviation
            #also feature for supply items in the map
            pag.click(None, None)
            time.sleep(FREEZE_CLICK)

            #try to go to the battle menu
            pag.click(None, None)

            #save new fleet position and mouse point
            x, y = pag.position()
            self.fleet_pos = point

            #wait while map is loading
            time.sleep(FREEZE_CLICK)
            self.battle()
            pag.moveTo(x, y)
            time.sleep(FREEZE_CLICK)
            
    def battle(self):
        self.compare_to_screen("battle")
        if self.box!=None:
            #self.battle_amount+=1
            pag.click(self.box)

            pag.moveTo(1230, 650)
            time.sleep(TIME_FOR_BATTLE)
            pag.click(None, None)
            FREEZE(CLICK_TIME)
            pag.click(None, None)
            FREEZE(CLICK_TIME)
            pag.click(None, None)
            FREEZE(CLICK_TIME)

            self.compare_to_screen("end")
            if self.box!=None:
                pag.click(self.box)


class ControlPlay():
    """class is for selecting chapters
        and control game process such as ambush and connection errors"""
    def __init__(self):
        self.chapter = None 

    def click_on(self, item):
        if item in SPETIAL_TEMPLATE:
            box = pag.locateOnScreen("img/{}/{}.png".format(self.chapter.name, item), confidence=ACCURACY)
        else:
            box = pag.locateOnScreen("img/{}.png".format(item), confidence=ACCURACY)
        if box!=None:
            pag.click(box)


    def set_chapter(self, chapter):
        self.chapter = chapter

    def start_chapter(self):
        for item in START_CHAPTER_TEMPLATE:
            self.click_on(item)
            FREEZE(CLICK_TIME)
        FREEZE(CLICK_TIME)
        box = pag.locateOnScreen("img/{}.png".format("strategy"), confidence=ACCURACY)
        pag.click(box[0]+5, box[1]+5)


        #self.chapter.set_first_mouse_position()

    def clear_chapter(self):
        for i in range(len(self.chapter.stage_road)):
            self.chapter.move_next()
            FREEZE(CLICK_TIME)

            x, y = pag.position()
            self.click_on("ambush")
            FREEZE(CLICK_TIME)
            self.click_on("connection")
            FREEZE(CLICK_TIME)

            pag.moveTo(x, y)
            self.chapter.battle()

            FREEZE(CLICK_TIME*2)

    def retreat(self):
        self.click_on("retreat")
        FREEZE(CLICK_TIME)
        self.click_on("retreatconfirm")
        



Play = ControlPlay()
Play.set_chapter(Chapter81())
Play.start_chapter()
Play.clear_chapter()
Play.retreat()

'''
Chapter = Chapter81()

#go to chapter map
for el in ACTION_TEMPLATE: 
    Chapter.find_and_click(el)    
    time.sleep(FREEZE_CLICK)

#move to the start of chapter
Chapter.get_first_position()

if Chapter.in_battle():
    Chapter.run()
    time.sleep(FREEZE_CLICK)
    Chapter.retreat()
'''