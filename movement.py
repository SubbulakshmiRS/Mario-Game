import common
import config


def move_all_left_right(x1,x2):
    # bcoz Mario is moving right by this much

    death =0
    delete_elements(x1,x2)

    if x2 == common.cols :
        a=x1
        b=0
        x=x1-x2
    elif x1 == 0:
        a=x2
        b=common.cols
        x=x2-x1

    step = 1 if a<=b else -1
    if (a > b):
        for i in reversed(range(a,b)):
            for j in range(common.rows):
                if common.ARR[i-x][j] in {"^", "O", "I"} and common.ARR[i][j] != " ":
                    print(common.ARR[i-x][j])
                    #print(common.value_arr(i,j))
                    death = 1
                elif common.ARR[i-x][j] in {"^", "O", "I"}:
                    continue
                common.ARR[i-x][j] = common.ARR[i][j]
    else :
        for i in range(a,b):
            for j in range(common.rows):
                if common.ARR[i-x][j] in {"^", "O", "I"} and common.ARR[i][j] != " ":
                    print(common.ARR[i-x][j])
                    #print(common.value_arr(i,j))
                    death = 1
                elif common.ARR[i-x][j] in {"^", "O", "I"}:
                    continue
                common.ARR[i-x][j] = common.ARR[i][j]


    for i in config.e_list:
        i.change(i.x-x, i.y)

    for i in config.w_list:
        i.change(i.x-x, i.y)

    for i in config.g_list:
        i.change(i.x-x, i.y)
    
    for i in config.m_list:
        i.change(i.x-x, i.y)

    if death != 0:
        raise config.Dead_Mario


def delete_elements(x1,x2):
    # delete all the elements which are in range x1 to x2
    for i in config.e_list:
        if i.x in range(x1, x2):
            config.e_list.remove(i)
            i.refresh_out()
    for i in config.w_list:
        if i.x in range(x1, x2):
            config.w_list.remove(i)
            i.refresh_out()
    for i in config.p_list:
        if i.x in range(x1, x2):
            config.p_list.remove(i)
            i.refresh_out()
    for i in config.m_list:
        if i.x in range(x1, x2):
            config.m_list.remove(i)
            i.refresh_out()   

def move_all(x):
    x1=x2=0
    if x > 0:
        x1=0
        x2=x
    elif x < 0:
        x1=common.cols+x
        x2=common.cols

    move_all_left_right(x1,x2)
