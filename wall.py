from colorama import Fore, Back, Style

import config
import common
import check

class Wall:
    def __init__(self, x):
        self.symbol = '8'
        self.x = x
        self.y = common.mids_r
        for i in range(0, 4):
            a = self.y-i
            common.set_arr(a, self.y, self.symbol)
            print('\033['+str(a)+';'+str(self.x) +
                  'H\033[31m' + str(self.symbol))
    
    def change(self,symbol,x,y):
        self.x = x
        self.y = y
        self.symbol = symbol

    # wall should not move
    def move(self, x):
        try :
            for i in range(0,4):
                check.check(x,self.y-i,"Wall")
            for i in range(0, 4):
                common.set_arr(x, self.y-i, self.symbol)
                common.reset_arr(self.x, self.y-i)
                print('\033['+str(self.y-i)+';'+str(self.x) +
                      'H\033[30m'+str(self.symbol))
                print('\033['+str(self.y-i)+';'+str(x) +
                      'H\033[31m' + str(self.symbol))
            self.x = x
        except config.Touch_Boundary:
            w_list.remove(self)



        