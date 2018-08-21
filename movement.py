import common
import config

def move_all_left(x):
    #bcoz Mario is moving right by this much
    #but change y
    death =0
    delete_elements(x)
    for i in range(x,common.cols):
        for j in range(common.rows):
            if common.ARR[i][j] == 1 :
                continue
            elif common.ARR[i-x][j] == 1 and common.ARR[i][j] != 1:
                death = 0
            common.ARR[i-x][j] = common.ARR[i][j]
    
    for i in config.e_list:
        i.change(i.symbol,i.x-x,i.y)

    for i in config.w_list:
        i.change(i.symbol,i.x-x,i.y)
    
    if death != 0 :
        raise config.Dead_Mario

def delete_elements(x):
    #delete all the elements which are crossing the boundary
    for i in config.e_list:
        if i.x in range(0,x):
            config.e_list.remove(i)
    for i in config.w_list:
        if i.x in range(0,x):
            config.w_list.remove(i)