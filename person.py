import time

import common
import movement
import check
import config
import thing
import sound

# for mario and enemy , this is the core class
# inheritance


class Person(thing.Thing):
    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y
        # private functions specific for enemy and Mario
        self.__check()

    def move(self, x, y='?', who='?'):
        self.refresh_out()
        super().move(x, y, who)
        self.print_out()
        self.__check()

    def jump(self):
        self.move(self.x_pos+3, self.y_pos-3)

    # drop is for gravity effect - mario and enemy - when they fall into a pit/gap
    def __check(self):
        if self.y_pos > common.mids_r and common.value_arr(self.x_pos, self.y_pos+1) != '0':
            if self.y_pos > (common.mids_r + 3):
                raise config.GapHere
            else:
                self.move(self.x_pos, self.y_pos+1)


class Mario(Person):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.print_out()

    def move(self, x, y):
        # when Mario hits the Marijuana
        if common.value_arr(x, y) == "$":
            sound.PlaySound("mb_sc.wav")
            for i in config.M_LIST:
                if (i.x_pos == x or i.x_pos == x+1 or i.x_pos == x-1) and (i.y_pos == y or i.y_pos == y+1 or i.y_pos == y-1):
                    config.POINTS += 20
                    config.M_LIST.remove(i)
        try:

            if (x > common.r3 and x < common.r4):
                check.check_life(x, y, "Mario")
                super().move(x, y)

            else:
                movement.move_all(x-self.x_pos)
                check.check_life(self.x_pos, y, "Mario")
                super().move(self.x_pos, y, "Mario")

        except config.GapHere:
            raise config.DeadMario from None

    def print_out(self):
        common.set_arr(self.x_pos, self.y_pos, "I")
        common.set_arr(self.x_pos, self.y_pos-1, "O")
        common.set_arr(self.x_pos, self.y_pos-2, "^")

    def refresh_out(self):
        for i in range(-2, 1):
            common.reset_arr(self.x_pos, self.y_pos+i)


class Enemy(Person):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.print_out()

    # over-riding
    def move(self, x, y):
        try:
            check.check(x, y, "Enemy")
            super().move(x, y)
        except (config.GapHere, config.TouchBoundary):
            config.E_LIST.remove(self)
            self.refresh_out()
        except config.WallHere:
            pass
        except config.MarioAbove:
            # enemy getting killed because of mario jumping on it
            sound.PlaySound("mb_touch.wav")
            config.E_LIST.remove(self)
            self.refresh_out()
            config.POINTS += 10

        except config.DeadMario:
            config.M.refresh_out()
            super().move(x, y)
            raise config.DeadMario from None

    def refresh_out(self):
        common.reset_arr(self.x_pos, self.y_pos)
        common.reset_arr(self.x_pos+1, self.y_pos)

    def print_out(self):
        common.set_arr(self.x_pos, self.y_pos, ">")
        common.set_arr(self.x_pos+1, self.y_pos, "<")
