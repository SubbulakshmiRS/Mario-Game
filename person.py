import time

import common
import movement
import check
import config
import thing


class Person(thing.Thing):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__check()
        self.print_out()

    def jump(self):
        #print("babe")
        self.move(self.x+1, self.y-1)

    def drop(self):
        if self.y >= common.mids_r and common.value_arr(self.x, self.y+1) != '0':
            if self.y > (common.mids_r + 3):
                raise config.Gap_Here
            else:
                self.move(self.x, self.y+1)

    def __check(self):
        if (self.y >= common.mids_r and common.value_arr(self.x, self.y+1) != '0'):
            raise config.Gap_Here


class Mario(Person):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self, x, y):
        if (x > common.r3 and x < common.r4):
            check.check_life(x, y, "Mario")
            super().move(x, y)

        else:
            movement.move_all_left(x-self.x)
            check.check_life(self.x, y, "Mario")
            super().move(self.x, y,"Mario")

        try:
            self.drop()
        except config.Gap_Here:
            raise config.Dead_Mario from None

    def print_out(self):
        common.set_arr(self.x, self.y, "I")
        common.set_arr(self.x, self.y-1, "O")
        common.set_arr(self.x, self.y-2, "^")

    def refresh_out(self):
        for i in range(-2, 1):
            common.reset_arr(self.x, self.y+i)


class Enemy(Person):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self, x, y):
        try:
            check.check(x, y, "Enemy")
            super().move(x, y)
            self.drop()
        except (config.Gap_Here, config.Touch_Boundary):
            config.e_list.remove(self)
            self.refresh_out()
        except config.Wall_Here:
            pass
        except config.Dead_Mario:
            config.m.refresh_out()
            super().move(x, y)
            raise config.Dead_Mario from None

    def refresh_out(self):
        common.reset_arr(self.x, self.y)
        common.reset_arr(self.x+1, self.y)

    def print_out(self):
        common.set_arr(self.x, self.y, ">")
        common.set_arr(self.x+1, self.y, "<")
