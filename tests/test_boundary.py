import sys
import os
sys.path.append(os.path.abspath('../tests'))
import pytest
from random import randint
import create_scenery
import common
import config
import obstacle

def test_boundary():
    """
    Test whether platform when reaches the boundary , gets deleted
    This is one of the many elements
    """
    pitem = obstacle.Platform( common.COLS-3, randint(common.R1_R, common.MIDS_R-5))
    config.P_LIST.append(pitem)
    pitem.move(pitem.x_pos+1,pitem.y_pos)
    assert config.P_LIST == []
