import time

import common
import movement
import check
import config
import thing

class Person(thing.Thing):
    def __init__(self, symbol, x, y):
        super().__init__(symbol,x,y)
        common.set_arr(x, y, symbol)

    def move(self, x, y):
        common.reset_arr(self.x, self.y)
        self.x = x
        self.y = y
        common.set_arr(self.x, self.y, self.symbol)

    def jump(self):
        self.move(self.x+1,self.y-1)


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

        try :
            self.check()
        except config.Gap_Here:
            raise config.Dead_Mario from None


class Enemy(Person):
    def __init__(self,symbol,x,y):
        super().__init__(symbol,x,y)

    def move(self,x,y):

        try :
            check.check(x,y,"Enemy")
            super().move(x,y)
            self.check()
        except (config.Touch_Boundary ,config.Gap_Here):
            config.e_list.remove(self)
            common.reset_arr(x,y)
        except config.Wall_Here:
            pass
        except config.Dead_Mario:
            super().move(x,y)
            raise config.Dead_Mario from None 

