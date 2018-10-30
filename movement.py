"""
For the screen movement after a_acertain distance
"""
import common
import config


def move_all_left_right(x1_pos, x2_pos):
    """
    Mario cant move anymore left or right
    """
    death = 0
    delete_elements(x1_pos, x2_pos)

    a_a = b_b = x_pos = 0
    if x2_pos == common.COLS:
        a_a = x1_pos
        b_b = 0
        x_pos = x1_pos-x2_pos
    elif x1_pos == 0:
        a_a = x2_pos
        b_b = common.COLS
        x_pos = x2_pos-x1_pos

    if a_a > b_b:
        # Mario is moving left
        death = replace(reversed(range(b_b, a_a)), x_pos)
    else:
        # Mario is moving right
        death = replace(range(a_a, b_b), x_pos)

    # change all the lists' data
    for i in (config.E_LIST +
              config.W_LIST +
              config.P_LIST +
              config.M_LIST +
              config.F_LIST +
              config.S_LIST + config.B_LIST):
        i.change(i.x_pos-x_pos, i.y_pos)

    if config.B != "":
        config.B.change(config.B.x_pos-x_pos, config.B.y_pos)

    if death != 0:
        raise config.DeadMario


def delete_elements(x1_pos, x2_pos):
    """
    Delete all elements closer to the boundary
    """
    # delete all the elements which are in range x1_pos to x2_pos
    list_all = [config.E_LIST, config.W_LIST, config.P_LIST, config.M_LIST,
                config.F_LIST, config.S_LIST, config.B_LIST]
    for k in range(7):
        for i in list_all[k]:
            if i.x_pos in range(x1_pos, x2_pos):
                list_all[k].remove(i)
                i.refresh_out()


# check whether left or right and accordingly decide the range
def move_all(x_amt):
    """
    Move the whole screen according to the movement is
    meant to do
    """
    x1_pos = x2_pos = 0
    if x_amt > 0:
        x1_pos = 0
        x2_pos = x_amt
    elif x_amt < 0:
        x1_pos = common.COLS+x_amt
        x2_pos = common.COLS

    move_all_left_right(x1_pos, x2_pos)

# replace or overwrite all in the above range


def replace(r_item, x_pos):
    """
    Replace or overwrite all in the range
    """
    death = 0
    for i in r_item:
        for j in range(common.ROWS):
            if common.ARR[i-x_pos][j] in {"^", "O", "I"} and \
             common.ARR[i][j] not in {" ", "^", "O", "I"}:
                death = 1
            elif common.ARR[i][j] in {"^", "O", "I"}:
                continue
            common.ARR[i-x_pos][j] = common.ARR[i][j]

    return death
