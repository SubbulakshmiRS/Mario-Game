from random import randint

import person
import wall
import common
import config
import check

def floor(floor_y):
    for i in range(1,common.cols+1):
        if (common.value_arr(i,floor_y) != 4 ):
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
    if (randint(0, 20) == 5):
        # create a wall
        while (1):
            pos = randint(config.m.x+4,common.r2)
            if common.value_arr(pos,common.mids_r) == 0 and common.value_arr(pos,common.mids_r+1) == 3:
                break

        w = wall.Wall(pos)
        config.w_list.append(w)

def create_Platform():

    if config.p_list == []:
        p=wall.Platform(randint(config.m.x +2,common.cols-1),randint(0,common.mids_r-5))
        config.p_list.append(p)
    elif(randint(0,5) == 1):
        p=wall.Platform(randint(config.m.x +2,common.cols-1),randint(0,common.mids_r-5))
        config.p_list.append(p)
    
    for i in config.p_list :
        x=randint(-1,1)+i.x
        i.move(i.x)

def create_Gap():

    if config.g_list == []:
        g=wall.Gap(config.m.x+2,common.mids_r+1)
        config.g_list.append(g)
    elif(randint(0,5) == 1):
        g=wall.Gap(randint(config.m.x +2,common.cols-1),common.mids_r+1)
        config.g_list.append(g)


def check_floor():
    if common.value_arr(config.m.x,config.m.y+1)  != 3 :
        while(common.value_arr(config.m.x,config.m.y+1) != 3) :
            config.m.move(config.m.x,config.m.y+1)

def create_scene():
    create_scenery.create_Wall()
    create_scenery.create_Enemy()
    create_scenery.create_Gap()
    create_scenery.create_Platform()
    create_scenery.create_floor()