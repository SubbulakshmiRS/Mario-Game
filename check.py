import config 
import common

#for raising all errors due to movement of different elements of the game
def check_life(x,y,who):
    if who is "Wall" :
        if common.value_arr(x-1,y) in {"^","O","I"}:
            raise config.Dead_Mario
    elif who is "Enemy":
        if (common.value_arr(x,y) in {"<",">"} ) :
            raise config.Enemy_Here
        elif common.value_arr(x,y) == "|":
            raise config.Wall_Here
        elif common.value_arr(x,y+1) != "0":
            raise config.Gap_Here
        elif common.value_arr(x,y-1) in {"^","O","I"}:
            raise config.Mario_Above
    elif who is "Mario" :
        if common.value_arr(x,y) not in {" ","I","O","^","$"}:
            raise config.Dead_Mario
    elif who is "Marijuana":
        for j in range(0,2):
            for i in range(-2,3):
                if common.value_arr(x+i,y+j) in {"^","O","I"}:
                    raise config.Dead_Mario
        for i in range(-2,3):
            for j in range(0,2):
                if common.value_arr(x+i,y+j) in {"|","-"}:
                    raise config.Wall_Here
    elif who is "Boss" :
        if common.value_arr(x,y-4) == "I":
            raise config.Mario_Above

#specifically for when the elements are created or when they move near the boundary
def check_boundary(x,y):
    if x == 1 or x == common.cols or y == 1 or y == common.rows :
        raise config.Touch_Boundary


def check(x,y,who):
    check_life(x,y,who)
    check_boundary(x,y)