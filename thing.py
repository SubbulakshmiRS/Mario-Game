import common
import config
import check
import time

# the core class - for checking the boundary


class Thing():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.print_out()

    def move(self, x, y='?', who='?'):
        # polymorphism
        self.refresh_out()
        if who == '?':
            who = self.__class__.__name__
        if y != '?':
            self.y = y
        self.x = x

        if who == "Mario":
            self.print_out()
        elif who in config.Elements:
            try:
                check.check_boundary(self.x+4, self.y)
                self.print_out()
            except config.Touch_Boundary:
                if who == "Wall":
                    config.w_list.remove(self)
                elif who == "Platform":
                    config.p_list.remove(self)
                elif who == "Gap":
                    config.g_list.remove(self)
                elif who == "Marijuana":
                    config.m_list.remove(self)
                elif who == "Fish":
                    config.f_list.remove(self)
                elif who == "Star":
                    config.s_list.remove(self)
                elif who == "Boss":
                    config.b = ""
                elif who == "Bullet":
                    config.b_list.remove(self)

    def change(self, x, y):
        self.x = x
        self.y = y
