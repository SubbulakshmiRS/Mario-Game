import sys
import os
sys.path.append(os.path.abspath('../tests'))
import pytest
import create_scenery
import common
import config
import obstacle

def test_drop():
    """ 
    Test whether Mario drops when above a gap
    """
    create_scenery.create_mario()
    x_pos = config.M.x_pos
    y_pos = config.M.y_pos
    gitem = obstacle.Gap(x_pos+1)
    try :
        config.M.move(x_pos+1,y_pos)
        assert config.M.y_pos == y_pos+1
    except config.DeadMario:
        assert False
    

    
