import config
import common
import check
import thing


class Wall(thing.Thing):
    def __init__(self, x):
        super().__init__(x, common.mids_r)

    def refresh_out(self):
        for j in range(-4, 1):
            for i in range(-1, 2):
                common.reset_arr(self.x+i, self.y+j)

    def print_out(self):
        for j in range(-4, 1):
            for i in {-1, +1}:
                common.set_arr(self.x+i, self.y+j, "|")
            common.set_arr(self.x, self.y+j, "-")


class Platform(thing.Thing):
    def __init__(self, x, y):
        super().__init__(x, y)

    def refresh_out(self):
        for i in range(-2, 3):
            common.reset_arr(self.x+i, self.y)

    def print_out(self):
        for i in range(-2, 3):
            common.set_arr(self.x+i, self.y, "0")


class Gap(thing.Thing):
    def __init__(self, x):
        super().__init__(x, common.mids_r+1)

    def refresh_out(self):
        for i in range(-1, 2):
            common.reset_arr(self.x+i, self.y)

    def print_out(self):
        for i in range(-1, 2):
            common.set_arr(self.x+i, self.y, "-")


class Marijuana(thing.Thing):
    def __init__(self, x):
        self.x = x
        self.y = common.mids_r - 4
        check.check(self.x, self.y, "Marijuana")
        self.print_out()

    def refresh_out(self):
        for j in range(0, 2):
            for i in range(-1, 2):
                common.reset_arr(self.x+i, self.y+j)

    def print_out(self):
        for j in range(0, 2):
            for i in range(-1, 2):
                common.set_arr(self.x+i, self.y+j, "$")


class Bullet(thing.Thing):
    def __init__(self, x, y, dir):
        self.dir = dir
        super().__init__(x, y)

    def refresh_out(self):
        common.reset_arr(self.x, self.y)

    def print_out(self):
        common.set_arr(self.x, self.y, "-")


class Boss(thing.Thing):
    def __init__(self, x, y):
        super().__init__(x, y)

    def shoot(self, x):
        dir = 0
        if x > self.x:
            dir = 1
        else:
            dir = -1

        b = Bullet(self.x+dir, self.y, dir)
        config.b_list.append(b)

        for i in config.b_list:
            i.move(i.x+i.dir)

    def refresh_out(self):
        for i in range(0, 3):
            for j in range(i-3, 3-i):
                common.reset_arr(self.x+j, self.y+i)

    def print_out(self):
        for i in range(0, 3):
            for j in range(i-3, 3-i):
                common.set_arr(self.x+j, self.y-i, "B")
