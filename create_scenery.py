from random import randint

import person
import wall
import common
import config
import check

def floor(floor_y):
    for i in range(1,common.cols+1):
        common.set_arr(i,floor_y,"3")

def create_floor():
        floor(common.mids_r+1)

def create_Enemy():

    if (randint(0,20) ==  5):
        try:
            check.check_life(common.cols-4,common.mids_r,"Enemy")
            e=person.Enemy('2',common.cols-4,common.mids_r)
            config.e_list.append(e)
        except config.Dead_Mario:
            pass
    
    for i in config.e_list:
        try :
            #print(i.x)
            #print(i.y)
            i.move(i.x-1,i.y)
        except config.Wall_Here:
            pass


def create_Mario():
        config.m = person.Mario("1",common.r3,common.mids_r)

def create_Wall():
    if (randint(0, 10) == 5):
        # create a wall
        while (1):
            pos = randint(config.m.x+2,common.r2)
            if common.value_arr(pos,common.mids_r) == 0:
                break

        w = wall.Wall(pos)
        config.w_list.append(w)

def check_floor():
    if common.value_arr(config.m.x,config.m.y+1)  != 3 :
        while(common.value_arr(config.m.x,config.m.y+1) != 3) :
            config.m.move(config.m.x,config.m.y+1)