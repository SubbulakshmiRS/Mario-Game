import common
import config


def move_all_left_right(x1,x2):

    death =0
    delete_elements(x1,x2)

    a=b=x=0
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
        #Mario is moving left
        death = replace(reversed(range(b,a)),x)
    else :
        #Mario is moving right
        death = replace(range(a,b),x)


    #change all the lists' data 
    for i in (config.e_list +
                config.w_list +
                config.p_list +
                config.m_list +
                config.f_list +
                config.s_list + config.b_list) :
        i.change(i.x-x, i.y)

    if config.b != "":
        config.b.change(config.b.x-x,config.b.y)

    if death != 0:
        raise config.Dead_Mario


def delete_elements(x1,x2):
    # delete all the elements which are in range x1 to x2
    for i in config.e_list :
        if i.x in range(x1, x2):
            config.e_list.remove(i)
            i.refresh_out()

    for i in config.w_list :
        if i.x in range(x1, x2):
            config.w_list.remove(i)
            i.refresh_out()

    for i in config.p_list :
        if i.x in range(x1, x2):
            config.p_list.remove(i)
            i.refresh_out()

    for i in config.m_list :
        if i.x in range(x1, x2):
            config.m_list.remove(i)
            i.refresh_out()

    for i in config.f_list :
        if i.x in range(x1, x2):
            config.f_list.remove(i)
            i.refresh_out()

    for i in config.s_list :
        if i.x in range(x1, x2):
            config.s_list.remove(i)
            i.refresh_out()

    for i in config.b_list :
        if i.x in range(x1, x2):
            config.b_list.remove(i)
            i.refresh_out()            

    
#check whether left or right and accordingly decide the range
def move_all(x):
    x1=x2=0
    if x > 0:
        x1=0
        x2=x
    elif x < 0:
        x1=common.cols+x
        x2=common.cols

    move_all_left_right(x1,x2)

#replace or overwrite all in the above range
def replace(r,x):
    death = 0
    for i in r:
        for j in range(common.rows):
            if common.ARR[i-x][j] in {"^", "O", "I"} and common.ARR[i][j] not in {" ","^", "O", "I"}:
                death = 1
            elif common.ARR[i][j] in {"^", "O", "I"}:
                continue
            common.ARR[i-x][j] = common.ARR[i][j]

    return death