import time

import common
import movement
import check
import config
import thing

class Person(thing.Thing):
    def __init__(self, x, y):
        super().__init__(x,y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def jump(self):
        self.move(self.x+1,self.y-1)


class Mario(Person):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.print_out()

    def move(self,x,y):
        if (x > common.r3 and x < common.r4 ):
            check.check_life(x,y,"Mario")
            self.refresh_out()
            super().move(x,y)
            self.print_out()

        else :
            movement.move_all_left(x-self.x)
            check.check_life(self.x,y,"Mario")
            self.refresh_out()
            super().move(self.x,y)
            self.print_out()

        try :
            self.check()
        except config.Gap_Here:
            try:
                self.drop()
            except config.Gap_Here:
                raise config.Dead_Mario from None

    def print_out(self):
        common.set_arr(self.x,self.y,"I")
        common.set_arr(self.x,self.y-1,"O")
        common.set_arr(self.x,self.y-2,"^")

    def refresh_out(self):
        for i in {-2,-1,0}:
            common.reset_arr(self.x,self.y+i)



class Enemy(Person):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.print_out()

    def move(self,x,y):
        try :
            check.check(x,y,"Enemy")
            self.refresh_out()
            super().move(x,y)
            self.print_out()
            self.check()
        except config.Gap_Here:
            try :
                self.drop()
            except config.Gap_Here:
                config.e_list.remove(self)
                self.refresh_out()
        except config.Touch_Boundary:
            config.e_list.remove(self)
            self.refresh_out()  
        except config.Wall_Here:
            pass
        except config.Dead_Mario:
            self.refresh_out()
            config.m.refresh_out()
            super().move(x,y)
            self.print_out()
            raise config.Dead_Mario from None

    def refresh_out(self):
        common.reset_arr(self.x,self.y)
        common.reset_arr(self.x+1,self.y)

    def print_out(self):
        common.set_arr(self.x,self.y,">")
        common.set_arr(self.x+1,self.y,"<")


