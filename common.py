import shutil
import numpy as np
import os
import sys
import config
import time


#boundary varibales 
cols = shutil.get_terminal_size().columns 
rows = shutil.get_terminal_size().lines
mids = int(cols/2)
r1 = int(mids/2)
r2 = int((mids + cols)/2)
r3 = int((3*cols)/8)
r4 = int((5*cols)/8)
r5 = int(cols/8)
r6 = int((7*cols)/8)
mids_r = int(rows/2)
r1_r = int(rows/4)


#array representing the whole terminal
ARR= np.full((cols+1,rows+1)," ",dtype=np.unicode)

def set_arr(x, y, symbol):
    ARR[x][y] = symbol


def reset_arr(x, y):
    ARR[x][y] = " "


def value_arr(x, y):
    return(ARR[x][y])

def print_all():
    os.system('cls' if os.name == 'nt' else 'clear')
    for j in range(1,rows+1):
        for i in range(1,cols+1):
            sys.stdout.write(ARR[i][j])
            sys.stdout.flush()
        if j < rows:
            sys.stdout.write("\n")
    
    print("MARIO GAME BY R.S.SUBBULAKSHMI\t\t\tPOINTS: "+str(config.points)+"\t\t\tLIVES: "+str(config.lives)+"\n")   

    
    
def restart_all():
    os.system('cls' if os.name == 'nt' else 'clear')
    global ARR
    ARR= np.full((cols+1,rows+1)," ",dtype=np.unicode)
    config.m = ""
    config.e_list = []
    config.w_list = []
    config.p_list = []
    config.g_list = []
    config.m_list = []
    print_all()
    time.sleep(0.2)

def game_over():
    restart_all()
