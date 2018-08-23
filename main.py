#import sys
#import termios
#import tty
import os
#import time
#from random import randint
#import shutil
#import numpy as np

 # import local files
import create_scenery
import config
import common

char = '' 

while True:
    char=config.get_key(config.get_input())

    # creates the whole scene and creates the gravity effect too 
    create_scenery.create_scene()
    if config.m is not "":
        if (char != config.JUMP):
            create_scenery.check_floor()    
    common.print_all()
    

    if (char == config.QUIT):
        # shut down all [q]
        os.system('cls' if os.name == 'nt' else 'clear')
        exit(0)

    if (char == config.START):
        # create a Person [m]
        create_scenery.create_Mario()

    elif (char == config.BREAK):
        # break the loop [s]
        os.system('cls' if os.name == 'nt' else 'clear')
        break

    elif (char == config.RIGHT):
        # Person moving right[a]
        if config.m is not "":
            config.m.move(config.m.x+1, config.m.y)

    elif (char == config.LEFT):
        # Person moving left[w]
        pass

    elif (char == config.JUMP):
        # Person jumping [d]
        if config.m is not "":
            config.m.jump()

