from random import randint

import person
import wall
import common
import config


def floor(floor_y):
    for i in range(1,common.cols+1):
        common.set_arr(i,floor_y,"3")
        print('\033['+str(floor_y)+';'+str(i) +
                'H\033[32m' + str("-"))

def create_floor(m):
    if config.m != '':
        floor(common.mids_r+1)

def create_Enemy():
    if (randint(0,20) in {2,5}):
        e=person.Enemy('2',randint(common.r2,common.cols),common.mids_r)
        config.e_list.append(e)
    
    for i in config.e_list:
        ret = i.move(i.x-1,i.y)
        if ( ret == 1):
            config.e_list.remove(i)

def create_Mario():
    config.m = person.Mario("1",common.r1,common.mids_r)

def create_Wall():
    if (randint(0, 10) == 5):
        # create a wall
        w = wall.Wall(common.cols-1)
        config.w_list.append(w)