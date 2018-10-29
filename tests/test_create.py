import sys
import os
sys.path.append(os.path.abspath('../tests'))
import pytest
import create_scenery
import common
import config

def test_enemy():
    """
    Test whether enemy is getting created
    """
    while config.E_LIST == []:
        create_scenery.create_enemy()
    assert common.ARR[config.E_LIST[0].x_pos][config.E_LIST[0].y_pos] == ">"
    assert common.ARR[config.E_LIST[0].x_pos+1][config.E_LIST[0].y_pos] == "<"

def test_wall():
    """
    Test whether wall is getting created
    """
    
    create_scenery.create_wall()
    x_pos=config.W_LIST[0].x_pos
    y_pos=config.W_LIST[0].y_pos
    for j in range(-4, 1):
        for i in {-1, +1}:
            assert common.ARR[x_pos+i][y_pos+j] == "|"
        assert common.ARR[x_pos][y_pos+j] == "-"

def test_platform():
    """
    Test whether platform is getting created
    """
    
    create_scenery.create_platform()
    x_pos=config.P_LIST[0].x_pos
    y_pos=config.P_LIST[0].y_pos
    for i in range(-2, 3):
        assert common.ARR[x_pos+i][y_pos] == "0"

def test_gap():
    """
    Test whether gap is getting created
    """
    
    create_scenery.create_gap()
    x_pos=config.G_LIST[0].x_pos
    y_pos=config.G_LIST[0].y_pos
    for i in range(-1, 2):
        assert common.ARR[x_pos+i][y_pos] == "-"

def test_marijuana():
    """
    Test whether marijuana is getting created
    """
    
    create_scenery.create_marijuana()
    x_pos=config.M_LIST[0].x_pos
    y_pos=config.M_LIST[0].y_pos
    for j in range(0, 2):
        for i in range(-1, 2):
            assert common.ARR[x_pos+i][y_pos+j] == "*"



