import sys
import os
sys.path.append(os.path.abspath('../tests'))
import pytest
import create_scenery
import common
import config

def test_collision():
    """ 
    Test whether mario is colliding with the enemy
    """
    create_scenery.create_mario()
    x_pos = config.M.x_pos
    y_pos = config.M.y_pos
    while(config.E_LIST == []):
        create_scenery.create_enemy()
    assert config.E_LIST[0].y_pos == y_pos
    while(config.E_LIST[0].x_pos > (2+x_pos)):
        config.E_LIST[0].move(config.E_LIST[0]-2,config.E_LIST[0])
    try :
        config.M.move(x_pos+2,y_pos)
        assert False
    except config.DeadMario:
        assert True


    
