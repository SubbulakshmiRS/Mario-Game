from colorama import Fore, Back, Style
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
        print('\033['+str(self.y)+';'+str(self.x) +
              'H\033[31m' + str(self.symbol))

    def move(self, x, y):
        print('\033['+str(self.y)+';'+str(self.x)+'H\033[30m'+str(self.symbol))
        common.reset_arr(self.x, self.y)
        self.x = x
        self.y = y
        common.set_arr(self.x, self.y, self.symbol)
        print('\033['+str(self.y)+';'+str(self.x) +
              'H\033[31m' + str(self.symbol))

    def jump(self):
        for i in range(0, 2):
            self.move(self.x+2,self.y-2)
            time.sleep(0.05)
            
        for i in range(0, 2):
            self.move(self.x+2,self.y+2)
            time.sleep(0.05)

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

