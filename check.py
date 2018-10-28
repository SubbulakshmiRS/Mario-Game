import config
import common

# for raising all errors due to movement of different elements of the game


def check_life(x, y, who):
    if who is "Wall":
        if common.value_arr(x-1, y) in {"^", "O", "I"}:
            raise config.DeadMario
    elif who is "Enemy":
        if (common.value_arr(x, y) in {"<", ">"}):
            raise config.EnemyHere
        elif common.value_arr(x, y) == "|":
            raise config.WallHere
        elif common.value_arr(x, y+1) != "0":
            raise config.GapHere
        elif common.value_arr(x, y-1) in {"^", "O", "I"}:
            raise config.MarioAbove
    elif who is "Mario":
        if common.value_arr(x, y) not in {" ", "I", "O", "^", "$"}:
            raise config.DeadMario
    elif who is "Marijuana":
        for j in range(0, 2):
            for i in range(-2, 3):
                if common.value_arr(x+i, y+j) in {"^", "O", "I"}:
                    raise config.DeadMario
        for i in range(-2, 3):
            for j in range(0, 2):
                if common.value_arr(x+i, y+j) in {"|", "-"}:
                    raise config.WallHere
    elif who is "Boss":
        if common.value_arr(x, y-4) == "I":
            raise config.MarioAbove

# specifically for when the elements are created or when they move near the boundary


def check_boundary(x, y):
    if x == 1 or x == common.cols or y == 1 or y == common.rows:
        raise config.TouchBoundary


def check(x, y, who):
    check_life(x, y, who)
    check_boundary(x, y)
