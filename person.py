import time

import common
import movement
import check
import config
import thing
import sound

#for mario and enemy , this is the core class
#inheritance 
class Person(thing.Thing):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #private functions specific for enemy and Mario
        self.__check()
        self.print_out()

    def move(self,x,y='?',who='?'):
        super().move(x,y,who)
        self.__check()

    def jump(self):
        self.move(self.x+3, self.y-3)

    #drop is for gravity effect - mario and enemy - when they fall into a pit/gap
    def __check(self):
        if self.y > common.mids_r and common.value_arr(self.x, self.y+1) != '0':
            if self.y > (common.mids_r + 3):
                raise config.Gap_Here
            else:
                self.move(self.x, self.y+1)


class Mario(Person):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self, x, y):
        #when Mario hits the Marijuana
        if common.value_arr(x,y) == "$":
            sound.PlaySound("mb_sc.wav")
            for i in config.m_list:
                if (i.x == x or i.x == x+1 or i.x == x-1 ) and (i.y == y or i.y == y+1 or i.y == y-1):
                    config.points += 20
                    config.m_list.remove(i)
        try:
            
            if (x > common.r3 and x < common.r4):
                check.check_life(x, y, "Mario")
                super().move(x, y)
                time.sleep(1)

            else:
                movement.move_all(x-self.x)
                check.check_life(self.x, y, "Mario")
                super().move(self.x, y,"Mario")

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

    #over-riding
    def move(self, x, y):
        try:
            check.check(x, y, "Enemy")
            super().move(x, y)
        except (config.Gap_Here, config.Touch_Boundary):
            config.e_list.remove(self)
            self.refresh_out()
        except config.Wall_Here:
            pass
        except config.Mario_Above:
            #enemy getting killed because of mario jumping on it
            sound.PlaySound("mb_touch.wav")
            config.e_list.remove(self)
            self.refresh_out()
            config.points += 10

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
