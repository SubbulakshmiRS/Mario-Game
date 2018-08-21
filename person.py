import time

import common
import movement
import check
import config

class Person:
    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.x = x
        self.y = y
        common.set_arr(x, y, symbol)

    def move(self, x, y):
        common.reset_arr(self.x, self.y)
        self.x = x
        self.y = y
        common.set_arr(self.x, self.y, self.symbol)

    def jump(self):
        self.move(self.x+1,self.y-1)

    def change(self,symbol,x,y):
        self.x = x
        self.y = y
        self.symbol = symbol


class Mario(Person):
    def __init__(self,symbol,x,y):
        super().__init__(symbol,x,y)

    def move(self,x,y):
        if (x > common.r3 and x < common.r4 ):
            check.check_life(x,y,"Mario")
            super().move(x,y)
        else :
            movement.move_all_left(x-self.x)
            check.check_life(self.x,y,"Mario")
            super().move(self.x,y)


class Enemy(Person):
    def __init__(self,symbol,x,y):
        super().__init__(symbol,x,y)

    def move(self,x,y):
        try :
            check.check(x,y,"Enemy")
            super().move(x,y)
        except config.Touch_Boundary:
            config.e_list.remove(self)
        except config.Wall_Here:
            pass
        except config.Dead_Mario:
            super().move(x,y)
            raise config.Dead_Mario from None 

