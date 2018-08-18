import config 
import common

def check_life(x,y):
    if common.value_arr(x,y) != 0 :
        config.dead += 1
        return 1
    return 0;

def check_boundary(x,y):
    if x == 2 or x == common.cols-2 or y == 2 or y == common.rows-2 :
        return 1;
    return 0;

def check(x,y):
    if (check_life(x,y) == 1):
        config.restart = 1
        return 2
    elif (check_boundary(x,y) == 1):
        return 1
    else :
        return 0 