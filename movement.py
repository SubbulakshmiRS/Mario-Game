import common
import config


def move_all_left_right(x1, x2):

    death = 0
    delete_elements(x1, x2)

    a = b = x = 0
    if x2 == common.cols:
        a = x1
        b = 0
        x = x1-x2
    elif x1 == 0:
        a = x2
        b = common.cols
        x = x2-x1

    step = 1 if a <= b else -1
    if (a > b):
        # Mario is moving left
        death = replace(reversed(range(b, a)), x)
    else:
        # Mario is moving right
        death = replace(range(a, b), x)

    # change all the lists' data
    for i in (config.E_LIST +
              config.W_LIST +
              config.P_LIST +
              config.M_LIST +
              config.F_LIST +
              config.S_LIST + config.B_LIST):
        i.change(i.x_pos-x, i.y_pos)

    if config.B != "":
        config.B.change(config.B.x_pos-x, config.B.y_pos)

    if death != 0:
        raise config.DeadMario


def delete_elements(x1, x2):
    # delete all the elements which are in range x1 to x2
    for i in config.E_LIST:
        if i.x_pos in range(x1, x2):
            config.E_LIST.remove(i)
            i.refresh_out()

    for i in config.W_LIST:
        if i.x_pos in range(x1, x2):
            config.W_LIST.remove(i)
            i.refresh_out()

    for i in config.P_LIST:
        if i.x_pos in range(x1, x2):
            config.P_LIST.remove(i)
            i.refresh_out()

    for i in config.M_LIST:
        if i.x_pos in range(x1, x2):
            config.M_LIST.remove(i)
            i.refresh_out()

    for i in config.F_LIST:
        if i.x_pos in range(x1, x2):
            config.F_LIST.remove(i)
            i.refresh_out()

    for i in config.S_LIST:
        if i.x_pos in range(x1, x2):
            config.S_LIST.remove(i)
            i.refresh_out()

    for i in config.B_LIST:
        if i.x_pos in range(x1, x2):
            config.B_LIST.remove(i)
            i.refresh_out()


# check whether left or right and accordingly decide the range
def move_all(x):
    x1 = x2 = 0
    if x > 0:
        x1 = 0
        x2 = x
    elif x < 0:
        x1 = common.cols+x
        x2 = common.cols

    move_all_left_right(x1, x2)

# replace or overwrite all in the above range


def replace(r, x):
    death = 0
    for i in r:
        for j in range(common.rows):
            if common.ARR[i-x][j] in {"^", "O", "I"} and common.ARR[i][j] not in {" ", "^", "O", "I"}:
                death = 1
            elif common.ARR[i][j] in {"^", "O", "I"}:
                continue
            common.ARR[i-x][j] = common.ARR[i][j]

    return death
