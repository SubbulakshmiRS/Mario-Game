import common
import config

def move_all_left(x):
    #bcoz Mario is moving right by this much
    #but change y
    delete_elements(x)
    for i in range(x,common.cols):
        for j in range(common.rows):
            common.ARR[i-x][j] = common.ARR[i][j]

def delete_elements(x):
    #delete all the elements which are crossing the boundary
    for i in config.e_list:
        if i.x in range(0,x+1):
            config.e_list.remove(i)
    for i in config.w_list:
        if i.x in range(0,x+1):
            config.w_list.remove(i)