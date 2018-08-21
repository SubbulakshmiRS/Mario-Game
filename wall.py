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
            common.set_arr(self.x, a, self.symbol)
    
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
            self.x = x
        except config.Touch_Boundary:
            w_list.remove(self)



        