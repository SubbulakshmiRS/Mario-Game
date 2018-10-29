import sys
import os
sys.path.append(os.path.abspath('../tests'))
import pytest
import create_scenery
import common
import config

def test_creation():
    """
    Test whether mario is jumping
    """
    create_scenery.create_mario()
    x_pos = config.M.x_pos
    y_pos = config.M.y_pos
    config.M.jump()
    assert common.ARR[config.M.x_pos][config.M.y_pos] == "I"
    assert common.ARR[config.M.x_pos][config.M.y_pos-1] == "O"
    assert common.ARR[config.M.x_pos][config.M.y_pos-2] == "^"
    assert common.ARR[x_pos][y_pos] != "I"
    assert common.ARR[x_pos][y_pos-1] != "O"
    assert common.ARR[x_pos][y_pos-2] != "^"


