from colorama import Fore, Back, Style
import time

import common
import movement
import check

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


class Mario(Person):
    def __init__(self,symbol,x,y):
        super().__init__(symbol,x,y)

    def move(self,x,y):
        if (x > common.r1 and x < common.r2 ):
            super().move(x,y)
        else :
            movement.move_all_left(x-self.x)
            super().move(self.x,y)


class Enemy(Person):
    def __init__(self,symbol,x,y):
        super().__init__(symbol,x,y)

    def move(self,x,y):
        ret=check.check(x,y)
        if ret in {1,2}:
            return ret

        super().move(x,y)
        return 0