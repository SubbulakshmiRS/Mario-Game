import shutil
import numpy as np
import os
import sys

#boundary varibales 
cols = shutil.get_terminal_size().columns 
rows = shutil.get_terminal_size().lines
mids = int(cols/2)
r1 = int(mids/2)
r2 = int((mids + cols)/2)
r3 = int((3*cols)/8)
r4 = int((5*cols)/8)
mids_r = int(rows/2)
r1_r = int(rows/4)

#array representing the whole terminal
ARR = np.zeros((cols+1, rows+1))

def set_arr(x, y, symbol):
    ARR[x][y] = symbol


def reset_arr(x, y):
    ARR[x][y] = 0


def value_arr(x, y):
    return(ARR[x][y])

def print_all():
    os.system('cls' if os.name == 'nt' else 'clear')
    for j in range(1,rows+1):
        for i in range(1,cols+1):
            if ARR[i][j] != 0 :
                sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (j, i, str(int(ARR[i][j]))))
                sys.stdout.flush()
    