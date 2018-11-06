"""
All elements of the scenery of the game
"""
from random import randint

import person
import obstacle
import common
import config
import check
import scene


def floor(floor_y):
    """
    Coordinates of floor
    """
    for i in range(1, common.COLS+1):
        if common.value_arr(i, floor_y) == " ":
            common.set_arr(i, floor_y, "0")
            common.set_arr(i, floor_y+1, "0")


def create_floor():
    """
    Create floor
    """
    floor(common.MIDS_R+1)


def create_enemy():
    """
    Create enemy using random functions and within a range of coordinates
    """
    if randint(0, 20) == 5:
        try:
            check.check_life(common.COLS-1, common.MIDS_R, "Enemy")
            eitem = person.Enemy(common.COLS-1, common.MIDS_R)
            config.E_LIST.append(eitem)
        except (config.EnemyHere, config.GapHere):
            pass

    for i in config.E_LIST:
        try:
            i.move(i.x_pos-2, i.y_pos)
        except config.WallHere:
            pass
        except config.EnemyHere:
            config.E_LIST.remove(i)


def create_mario():
    """
    Create Mario from fixed coordinates for the given screen space
    """
    config.M = person.Mario(common.R3, common.MIDS_R)


def create_wall():
    """
    Randomly generating , with out making it conjusted , walls as obstacles
    """
    if config.W_LIST == []:
        pos = randint(config.M.x_pos+4, common.R2)
        if common.value_arr(pos, common.MIDS_R) == " " and \
            common.value_arr(pos, common.MIDS_R+1) == "0":
            try:
                witem = obstacle.Wall(pos)
                config.W_LIST.append(witem)
            except config.GapHere:
                pass

    elif len(config.W_LIST) < int((3*common.COLS)/80):
        if randint(0, 10) == 5:
            # create a obstacle
            pos = config.W_LIST[-1].x_pos + randint(10, 20)
            if pos < common.COLS - 3:
                try:
                    witem = obstacle.Wall(pos)
                    config.W_LIST.append(witem)
                except config.GapHere:
                    pass

    else:
        pass


def create_platform():
    """
    Randomly generating , with out making it conjusted , walls as platforms
    Mario can walk on these
    """
    if config.P_LIST == []:
        pitem = obstacle.Platform(
            randint(config.M.x_pos+2, common.COLS-5), randint(common.R1_R, common.MIDS_R-5))
        config.P_LIST.append(pitem)
    elif len(config.P_LIST) < int(common.COLS/20):
        if randint(0, 5) == 1:
            pos = config.P_LIST[-1].x_pos + randint(7, 15)
            if pos < (common.COLS - 3):
                pitem = obstacle.Platform(pos, randint(
                    common.R1_R, common.MIDS_R-5))
                config.P_LIST.append(pitem)

    for i in config.P_LIST:
        xitem = randint(-3, 3)+i.x_pos
        i.move(xitem)


def create_gap():
    """
    Randomly generating gaps on which the enemy or Mario can fall into
    """
    if config.G_LIST == []:
        gitem = obstacle.Gap(randint(config.M.x_pos + 2, common.COLS-2))
        config.G_LIST.append(gitem)
    elif randint(0, 10) == 1:
        gitem = obstacle.Gap(randint(config.M.x_pos + 2, common.COLS-2))
        config.G_LIST.append(gitem)


def create_fish():
    """
    Create fish below the floor / ground level
    """
    if config.F_LIST == []:
        fitem = scene.Fish(randint(2, common.COLS-2),
                           randint(common.MIDS_R + 3, common.ROWS-2))
        config.F_LIST.append(fitem)
    elif randint(0, 10) == 1:
        fitem = scene.Fish(randint(2, common.COLS-2),
                           randint(common.MIDS_R + 3, common.ROWS-2))
        config.F_LIST.append(fitem)

    for i in config.F_LIST:
        i.move(i.x_pos+1)


def create_star():
    """
    Create stars at the top most quarter of the screen
    """
    if config.S_LIST == []:
        sitem = scene.Star(randint(2, common.COLS-2), randint(2, common.R1_R))
        config.S_LIST.append(sitem)
    elif randint(0, 5) == 1:
        sitem = scene.Star(randint(2, common.COLS-2), randint(2, common.R1_R))
        config.S_LIST.append(sitem)


def create_marijuana():
    """
    Points for Mario which can be taken in parts
    """
    if config.M_LIST == []:
        try:
            mitem = obstacle.Marijuana(randint(common.MIDS, common.COLS-3))
            config.M_LIST.append(mitem)
        except (config.DeadMario, config.WallHere):
            pass
    elif len(config.M_LIST) <= max(len(config.W_LIST), int(common.COLS/20)):
        pos = config.M_LIST[-1].x_pos + randint(5, 10)
        if randint(0, 10) == 1 and pos < common.COLS-3:
            try:
                mitem = obstacle.Marijuana(pos)
                config.M_LIST.append(mitem)
            except (config.DeadMario, config.WallHere):
                pass


def create_boss():
    """
    Create the level2 BOSS enemy (smart bullets)
    """
    if config.B == "":
        config.B = obstacle.Boss(common.R6, common.MIDS_R)
    else:
        try:
            check.check(config.B.x_pos, config.B.y_pos, "Boss")
            if randint(0, 5) == 1:
                config.B.shoot(config.M.x_pos)
        except config.MarioAbove:
            config.STAGE = "won"

# the gravity effect is created here
def check_floor():
    """
    For gravity check
    """
    if common.value_arr(config.M.x_pos, config.M.y_pos+1) != "0":
        while common.value_arr(config.M.x_pos, config.M.y_pos+1) != "0":
            config.M.move(config.M.x_pos, config.M.y_pos+1)


def create_scene():
    """
    Complete scene with all the elements
    """
    create_floor()
    if config.M != "":
        if config.LEVEL == 1:
            create_wall()
            create_enemy()
            create_gap()
            create_platform()
            create_marijuana()
            create_star()
            create_fish()
        elif config.LEVEL == 2:
            create_boss()
            create_platform()
            create_star()
