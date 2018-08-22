import common
import config

class Thing():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def check(self):
        if (self.y >= common.mids_r and common.value_arr(self.x,self.y+1) != '0' ):
            raise config.Gap_Here

    def change(self,x,y):
        self.x = x
        self.y = y

    def drop(self):
        if common.value_arr(self.x,self.y+1) != '0':
            if self.y > (common.mids_r + 3):
                raise config.Gap_Here
            else:
                self.move(self.x,self.y+1)

            