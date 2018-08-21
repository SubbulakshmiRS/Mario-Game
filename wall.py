import config
import common
import check
import thing

class Wall(thing.Thing):
    def __init__(self, x):
        self.symbol = '8'
        self.x = x
        self.y = common.mids_r
        self.check()
        for i in range(0, 4):
            a = self.y-i
            common.set_arr(self.x, a, self.symbol)


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

class Platform(thing.Thing):
    def __init__(self,x,y):
        super().__init__('3',x,y)

    def move(self,x):
        common.reset_arr(self.x-1,self.y)
        common.reset_arr(self.x,self.y)
        common.reset_arr(self.x+1,self.y)

        common.set_arr(x,self.y,self.symbol)
        common.set_arr(x-1,self.y,self.symbol)
        common.set_arr(x+1,self.y,self.symbol)
        self.x=x

class Gap(thing.Thing):
    def __init__(self,x,y):
        super().__init__('4',x,y)
    
    def move(self,x):
        common.reset_arr(self.x,self.y)
        common.set_arr(x,self.y)
        self.x=x


    
