import common
import thing

class Star(thing.Thing):
    def __init__(self, x,y):
        super().__init__(x, y)

    def move(self, x):
        super().move(x, self.y, "Star")

    def refresh_out(self):
            common.reset_arr(self.x, self.y)

    def print_out(self):
            common.set_arr(self.x, self.y, "*")

class Fish(thing.Thing):
    def __init__(self, x,y):
        super().__init__(x, y)

    def move(self, x):
        super().move(x, self.y, "Fish")

    def refresh_out(self):
        for i in range(-1,3):
                for j in range(-1,2):
                    if i == 0 :
                        common.reset_arr(self.x+i, self.y+j)
                    else :
                        common.reset_arr(self.x+i, self.y)

    def print_out(self):
        for i in range(-1,3):
                for j in range(-1,2):
                    if i == 0 :
                        common.set_arr(self.x+i, self.y+j,"@")
                    else :
                        common.set_arr(self.x+i, self.y,"@")