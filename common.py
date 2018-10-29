"""
Common screen related variables and functions
"""
import shutil
import os
import sys
import time
import numpy as np
import config
import sound


# boundary varibales
COLS = shutil.get_terminal_size().columns
ROWS = shutil.get_terminal_size().lines
MIDS = int(COLS/2)
R1 = int(MIDS/2)
R2 = int((MIDS + COLS)/2)
R3 = int((3*COLS)/8)
R4 = int((5*COLS)/8)
R5 = int(COLS/8)
R6 = int((7*COLS)/8)
MIDS_R = int(ROWS/2)
R1_R = int(ROWS/5)

# array representing the whole terminal
ARR = np.full((COLS+1, ROWS+1), " ", dtype=np.unicode)

def set_arr(x_pos, y_pos, symbol):
    """
    set screen
    """
    ARR[x_pos][y_pos] = symbol


def reset_arr(x_pos, y_pos):
    """
    reset screen
    """
    ARR[x_pos][y_pos] = " "


def value_arr(x_pos, y_pos):
    """
    get value of screen at x_pos,y_pos
    """
    return ARR[x_pos][y_pos]


def print_all():
    """
    print out the whole screen
    """
    os.system("tput reset")
    for j in range(1, ROWS+1):
        for i in range(1, COLS+1):
            sys.stdout.write(ARR[i][j])
            sys.stdout.flush()
        if j < ROWS:
            sys.stdout.write("\n")

    print("MARIO GAME BY R.S.SUBBULAKSHMI\t\t\tPOINTS: "+str(config.POINTS) +
          "\t\t\tLIVES: "+str(config.LIVES)+"\t\t\tLEVEL: " + str(config.LEVEL)+"\n")

# deletes all the copies of data present and ARR is also cleaned out


def restart_all():
    """
    for next level or when Mario dies
    """
    os.system("tput reset")
    global ARR
    ARR = np.full((COLS+1, ROWS+1), " ", dtype=np.unicode)
    config.M = ""
    config.E_LIST = []
    config.W_LIST = []
    config.P_LIST = []
    config.G_LIST = []
    config.M_LIST = []
    config.time_start = 0
    print_all()
    time.sleep(0.2)

# game over because of quiting or winning the game or losing the game


def game_over():
    """
    Game over
    """
    sound.play_sound("nsmb_game_over.wav")
    restart_all()
    os.system("tput reset")
    print("MARIO GAME BY R.S.SUBBULAKSHMI\t\t\tPOINTS: "+str(config.POINTS) +
          "\t\t\tLIVES: "+str(config.LIVES)+"\t\t\tLEVEL: " + str(config.LEVEL)+"\n")
    if config.STAGE == "won":
        print("WON WON WON !!!\n")
    elif config.STAGE == "quit":
        print("QUIT !\n")
    else:
        print("LOST SORRY !\n")
