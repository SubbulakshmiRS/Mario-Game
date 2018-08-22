import config
import common
import check
import thing

class Wall(thing.Thing):
    def __init__(self, x):
        self.x = x
        self.y = common.mids_r
        self.check()
        self.print_out()

    # wall should not move
    def move(self, x):
        try :
            check.check(x,self.y,"Wall")
            self.refresh_out()
            self.x = x
            self.print_out()
        except config.Touch_Boundary:
            w_list.remove(self)

    def refresh_out(self):
        for j in {-4,-3,-2,-1,0}:
            for i in {-1,+1}:
                common.reset_arr(self.x+i,self.y+j)
            common.reset_arr(self.x,self.y+j)

    
    def print_out(self):
        for j in {-4,-3,-2,-1,0}:
            for i in {-1,+1}:
                common.set_arr(self.x+i,self.y+j,"|")
            common.set_arr(self.x,self.y+j,"-")


class Platform(thing.Thing):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.print_out()

    def move(self,x):
        self.refresh_out()
        self.x=x
        self.print_out()

    def refresh_out(self):
        for i in {-2,-1,0,1,2}:
            common.reset_arr(self.x+i,self.y)

    def print_out(self):
        for i in {-2,-1,0,1,2}:
            common.set_arr(self.x+i,self.y,"0")


class Gap(thing.Thing):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.print_out()
    
    def move(self,x):
        self.refresh_out()
        self.x=x
        self.print_out()

    def refresh_out(self):
        for i in {-1,0,1}:
            common.reset_arr(self.x+i,self.y)

    def print_out(self):
        for i in {-1,0,1}:
            common.set_arr(self.x+i,self.y,"-")


class Marijuana(thing.Thing):
    def __init__(self,x):
        y=common.mids_r-4
        super().__init__(x,y)
        check.check(self.x,self.y,"Marijuana")
        self.print_out()

    def move(self,x):
        self.refresh_out()
        self.x=x
        self.print_out()

    def refresh_out(self):
        for j in range(0,2):
            for i in range(-2,3):
                common.reset_arr(self.x+i,self.y+j)

    def print_out(self):
        for j in range(0,2):
            for i in range(-1,2):
                common.set_arr(self.x+i,self.y+j,"*")
            for i in {-2,2}:
                common.set_arr(self.x+i,self.y+j,"0")

    

    
