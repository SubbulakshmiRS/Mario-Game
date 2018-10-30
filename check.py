"""
All checks are done in this module
"""
import config
import common

# for raising all errors due to movement of different elements of the game


def check_life(x_pos, y_pos, who):
    """
    The ways to kill Mario
    """
    if who == "Wall":
        if common.value_arr(x_pos-1, y_pos) in {"^", "O", "I"}:
            raise config.DeadMario
    elif who == "Enemy":
        if (common.value_arr(x_pos, y_pos) in {"<", ">"}):
            raise config.EnemyHere
        elif common.value_arr(x_pos, y_pos) == "|":
            raise config.WallHere
        elif common.value_arr(x_pos, y_pos+1) != "0":
            raise config.GapHere
        elif common.value_arr(x_pos, y_pos-1) in {"^", "O", "I"}:
            raise config.MarioAbove
    elif who == "Mario":
        if common.value_arr(x_pos, y_pos) not in {" ", "I", "O", "^", "$"}:
            raise config.DeadMario
    elif who == "Marijuana":
        for j in range(0, 2):
            for i in range(-2, 3):
                if common.value_arr(x_pos+i, y_pos+j) in {"^", "O", "I"}:
                    raise config.DeadMario
        for i in range(-2, 3):
            for j in range(0, 2):
                if common.value_arr(x_pos+i, y_pos+j) in {"|", "-"}:
                    raise config.WallHere
    elif who == "Boss":
        if common.value_arr(x_pos, y_pos-4) == "I":
            raise config.MarioAbove

# specifically_pos for when the elements are created or when they_pos move near the boundary_pos


def check_boundary(x_pos, y_pos):
    """
    Way to kill any element
    """
    if x_pos <= 4 or x_pos >= (common.COLS-4) or y_pos <= 4 or y_pos >= (common.ROWS-4):
        raise config.TouchBoundary


def check(x_pos, y_pos, who):
    """
    Check - umbrella function
    """
    check_life(x_pos, y_pos, who)
    check_boundary(x_pos, y_pos)
