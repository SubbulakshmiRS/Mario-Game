import shutil
import numpy as np

#boundary varibales 
cols = shutil.get_terminal_size().columns
rows = shutil.get_terminal_size().lines
mids = int(cols/2)
r1 = int(mids/2)
r2 = int((mids + cols)/2)
mids_r = int(rows/2)
r1_r = int(rows/4)

#array representing the whole terminal
ARR = np.zeros((cols, rows))

def set_arr(x, y, symbol):
    ARR[x-1][y-1] = symbol


def reset_arr(x, y):
    ARR[x-1][y-1] = 0


def value_arr(x, y):
    return(ARR[x-1][y-1])