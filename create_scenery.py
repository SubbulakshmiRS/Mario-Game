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
    for i in range(1, common.cols+1):
        if common.value_arr(i, floor_y) == " ":
            common.set_arr(i, floor_y, "0")
            common.set_arr(i, floor_y+1, "0")


def create_floor():
    """
    Create floor 
    """
    floor(common.mids_r+1)


def create_enemy():
    """
    Create enemy using random functions and within a range of coordinates 
    """
    if randint(0, 20) == 5:
        try:
            check.check_life(common.cols-1, common.mids_r, "Enemy")
            eitem = person.Enemy(common.cols-1, common.mids_r)
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
    config.M = person.Mario(common.r3, common.mids_r)


def create_wall():
    if config.W_LIST == []:
        pos = randint(config.M.x_pos+4, common.r2)
        if common.value_arr(pos, common.mids_r) == " " and \
            common.value_arr(pos, common.mids_r+1) == "0":
            try:
                witem = obstacle.Wall(pos)
                config.W_LIST.append(witem)
            except config.GapHere:
                pass

    elif len(config.W_LIST) < int((3*common.cols)/80):
        if randint(0, 10) == 5:
            # create a obstacle
            pos = config.W_LIST[-1].x_pos + randint(10, 20)
            if pos < common.cols - 3:
                try:
                    witem = obstacle.Wall(pos)
                    config.W_LIST.append(witem)
                except config.GapHere:
                    pass

    else:
        pass


def create_platform():

    if config.P_LIST == []:
        pitem = obstacle.Platform(
            randint(config.M.x_pos+2, common.cols-5), randint(common.r1_r, common.mids_r-5))
        config.P_LIST.append(pitem)
    elif len(config.P_LIST) < int(common.cols/20):
        if randint(0, 5) == 1:
            pos = config.P_LIST[-1].x_pos + randint(7, 15)
            if pos < (common.cols - 3):
                pitem = obstacle.Platform(pos, randint(
                    common.r1_r, common.mids_r-5))
                config.P_LIST.append(pitem)

    for i in config.P_LIST:
        xitem = randint(-3, 3)+i.x_pos
        i.move(xitem)


def create_gap():

    if config.G_LIST == []:
        gitem = obstacle.Gap(randint(config.M.x_pos + 2, common.cols-2))
        config.G_LIST.append(gitem)
    elif randint(0, 10) == 1:
        gitem = obstacle.Gap(randint(config.M.x_pos + 2, common.cols-2))
        config.G_LIST.append(gitem)


def create_fish():

    if config.F_LIST == []:
        fitem = scene.Fish(randint(2, common.cols-2),
                           randint(common.mids_r + 3, common.rows-2))
        config.F_LIST.append(fitem)
    elif randint(0, 10) == 1:
        fitem = scene.Fish(randint(2, common.cols-2),
                           randint(common.mids_r + 3, common.rows-2))
        config.F_LIST.append(fitem)

    for i in config.F_LIST:
        i.move(i.x_pos+1)


def create_star():

    if config.S_LIST == []:
        sitem = scene.Star(randint(2, common.cols-2), randint(2, common.r1_r))
        config.S_LIST.append(sitem)
    elif randint(0, 5) == 1:
        sitem = scene.Star(randint(2, common.cols-2), randint(2, common.r1_r))
        config.S_LIST.append(sitem)


def create_marijuana():

    if config.M_LIST == []:
        try:
            mitem = obstacle.Marijuana(randint(common.mids, common.cols-3))
            config.M_LIST.append(mitem)
        except (config.DeadMario, config.WallHere):
            pass
    elif len(config.M_LIST) <= max(len(config.W_LIST), int(common.cols/20)):
        pos = config.M_LIST[-1].x_pos + randint(5, 10)
        if randint(0, 10) == 1 and pos < common.cols-3:
            try:
                mitem = obstacle.Marijuana(pos)
                config.M_LIST.append(mitem)
            except (config.DeadMario, config.WallHere):
                pass


def create_boss():
    if config.B == "":
        config.B = obstacle.Boss(common.r6, common.mids_r)
    else:
        try:
            check.check(config.B.x_pos, config.B.y_pos, "Boss")
            if randint(0, 5) == 1:
                config.B.shoot(config.M.x_pos)
        except config.MarioAbove:
            config.STAGE = "won"

# the gravity effect is created here
def check_floor():
    if common.value_arr(config.M.x_pos, config.M.y_pos+1) != "0":
        while common.value_arr(config.M.x_pos, config.M.y_pos+1) != "0":
            config.M.move(config.M.x_pos, config.M.y_pos+1)


def create_scene():
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
