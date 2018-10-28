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
            config.e_list.append(eitem)
        except (config.Enemy_Here, config.Gap_Here):
            pass

    for i in config.e_list:
        try:
            i.move(i.x-2, i.y)
        except config.Wall_Here:
            pass
        except config.Enemy_Here:
            config.e_list.remove(i)


def create_mario():
    """
    Create Mario from fixed coordinates for the given screen space
    """
    config.m = person.Mario(common.r3, common.mids_r)


def create_wall():
    if config.w_list == []:
        pos = randint(config.m.x+4, common.r2)
        if common.value_arr(pos, common.mids_r) == " " and \
            common.value_arr(pos, common.mids_r+1) == "0":
            try:
                witem = obstacle.Wall(pos)
                config.w_list.append(witem)
            except config.Gap_Here:
                pass

    elif len(config.w_list) < int((3*common.cols)/80):
        if randint(0, 10) == 5:
            # create a obstacle
            pos = config.w_list[-1].x + randint(10, 20)
            if pos < common.cols - 3:
                try:
                    witem = obstacle.Wall(pos)
                    config.w_list.append(witem)
                except config.Gap_Here:
                    pass

    else:
        pass


def create_platform():

    if config.p_list == []:
        pitem = obstacle.Platform(
            randint(config.m.x+2, common.cols-5), randint(common.r1_r, common.mids_r-5))
        config.p_list.append(pitem)
    elif len(config.p_list) < int(common.cols/20):
        if randint(0, 5) == 1:
            pos = config.p_list[-1].x + randint(7, 15)
            if pos < (common.cols - 3):
                pitem = obstacle.Platform(pos, randint(
                    common.r1_r, common.mids_r-5))
                config.p_list.append(pitem)

    for i in config.p_list:
        xitem = randint(-3, 3)+i.x
        i.move(xitem)


def create_gap():

    if config.g_list == []:
        gitem = obstacle.Gap(randint(config.m.x + 2, common.cols-2))
        config.g_list.append(gitem)
    elif randint(0, 10) == 1:
        gitem = obstacle.Gap(randint(config.m.x + 2, common.cols-2))
        config.g_list.append(gitem)


def create_fish():

    if config.f_list == []:
        fitem = scene.Fish(randint(2, common.cols-2),
                           randint(common.mids_r + 3, common.rows-2))
        config.f_list.append(fitem)
    elif randint(0, 10) == 1:
        fitem = scene.Fish(randint(2, common.cols-2),
                           randint(common.mids_r + 3, common.rows-2))
        config.f_list.append(fitem)

    for i in config.f_list:
        i.move(i.x+1)


def create_star():

    if config.s_list == []:
        sitem = scene.Star(randint(2, common.cols-2), randint(2, common.r1_r))
        config.s_list.append(sitem)
    elif randint(0, 5) == 1:
        sitem = scene.Star(randint(2, common.cols-2), randint(2, common.r1_r))
        config.s_list.append(sitem)


def create_marijuana():

    if config.m_list == []:
        try:
            mitem = obstacle.Marijuana(randint(common.mids, common.cols-3))
            config.m_list.append(mitem)
        except (config.Dead_Mario, config.Wall_Here):
            pass
    elif len(config.m_list) <= max(len(config.w_list), int(common.cols/20)):
        pos = config.m_list[-1].x + randint(5, 10)
        if randint(0, 10) == 1 and pos < common.cols-3:
            try:
                mitem = obstacle.Marijuana(pos)
                config.m_list.append(mitem)
            except (config.Dead_Mario, config.Wall_Here):
                pass


def create_boss():
    if config.b == "":
        config.b = obstacle.Boss(common.r6, common.mids_r)
    else:
        try:
            check.check(config.b.x, config.b.y, "Boss")
            if randint(0, 5) == 1:
                config.b.shoot(config.m.x)
        except config.Mario_Above:
            config.stage = "won"

# the gravity effect is created here
def check_floor():
    if common.value_arr(config.m.x, config.m.y+1) != "0":
        while common.value_arr(config.m.x, config.m.y+1) != "0":
            config.m.move(config.m.x, config.m.y+1)


def create_scene():
    create_floor()
    if config.m != "":
        if config.level == 1:
            create_wall()
            create_enemy()
            create_gap()
            create_platform()
            create_marijuana()
            create_star()
            create_fish()
        elif config.level == 2:
            create_boss()
            create_platform()
            create_star()
