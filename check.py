import config 
import common

def check_life(x,y,who):
    if who is "Wall" :
        if common.value_arr(x,y) == 1:
            raise config.Dead_Mario
    elif who is "Enemy":
        if common.value_arr(x,y) == 1:
            raise config.Dead_Mario
        elif common.value_arr(x,y) == 8:
            raise config.Wall_Here
    elif who is "Mario" :
        if common.value_arr(x,y) != 1 and common.value_arr(x,y) != 0:
            raise config.Dead_Mario

def check_boundary(x,y):
    if x == 1 or x == common.cols or y == 1 or y == common.rows :
        raise config.Touch_Boundary

def check(x,y,who):
    check_life(x,y,who)
    check_boundary(x,y)