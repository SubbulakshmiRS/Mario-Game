import config
import common
import check
import thing


class Wall(thing.Thing):
    def __init__(self, x):
        super().__init__(x, common.mids_r)

    # move is needed for move_all_left
    def move(self, x):
        super().move(x, self.y, "Wall")

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

    def move(self, x):
        super().move(x, self.y, "Platform")

    def refresh_out(self):
        for i in range(-2, 3):
            common.reset_arr(self.x+i, self.y)

    def print_out(self):
        for i in range(-2, 3):
            common.set_arr(self.x+i, self.y, "0")


class Gap(thing.Thing):
    def __init__(self, x):
        super().__init__(x, common.mids_r+1)

    def move(self, x):
        super().move(x, self.y, "Gap")

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

    # needed for move_all_left
    def move(self, x):
        super().move(x, self.y, "Marijuana")

    def refresh_out(self):
        for j in range(0, 2):
            for i in range(-1, 2):
                common.reset_arr(self.x+i, self.y+j)

    def print_out(self):
        for j in range(0, 2):
            for i in range(-1, 2):
                common.set_arr(self.x+i, self.y+j, "*")

