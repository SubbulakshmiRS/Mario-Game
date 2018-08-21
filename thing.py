import common
import config

class Thing():
    def __init__(self,symbol,x,y):
        self.symbol=symbol
        self.x=x
        self.y=y

    def check(self):
        if (self.y == common.mids_r and common.value_arr(self.x,self.y+1) != 3 ):
            raise config.Gap_Here

    def change(self,symbol,x,y):
        self.x = x
        self.y = y
        self.symbol = symbol
            