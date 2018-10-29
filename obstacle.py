"""
Objects with potential to collide with each other or Mario
"""
import config
import common
import check
import thing


class Wall(thing.Thing):
    """
    Wall element
    """
    def __init__(self, x):
        super().__init__(x, common.MIDS_R)
        self.print_out()

    def move(self, x, y='?', who='?'):
        try:
            self.refresh_out()
            super().move(x, y, who)
            self.print_out()
        except config.DeletedElement:
            pass

    def refresh_out(self):
        """
        refresh the coordinates
        """
        for j in range(-4, 1):
            for i in range(-1, 2):
                common.reset_arr(self.x_pos+i, self.y_pos+j)

    def print_out(self):
        """
        update the coordinates
        """
        for j in range(-4, 1):
            for i in {-1, +1}:
                common.set_arr(self.x_pos+i, self.y_pos+j, "|")
            common.set_arr(self.x_pos, self.y_pos+j, "-")


class Platform(thing.Thing):
    """
    Platform
    """
    def __init__(self, x, y):
        super().__init__(x, y)
        self.print_out()

    def move(self, x, y='?', who='?'):
        try:
            self.refresh_out()
            super().move(x, y, who)
            self.print_out()
        except config.DeletedElement:
            pass

    def refresh_out(self):
        """
        refresh the coordinates
        """
        for i in range(-2, 3):
            common.reset_arr(self.x_pos+i, self.y_pos)

    def print_out(self):
        """
        update the coordinates
        """
        for i in range(-2, 3):
            common.set_arr(self.x_pos+i, self.y_pos, "0")


class Gap(thing.Thing):
    """
    Gap element
    """
    def __init__(self, x):
        super().__init__(x, common.MIDS_R+1)
        self.print_out()

    def move(self, x, y='?', who='?'):
        try:
            self.refresh_out()
            super().move(x, y, who)
            self.print_out()
        except config.DeletedElement:
            pass

    def refresh_out(self):
        """
        refresh the coordinates
        """
        for i in range(-1, 2):
            common.reset_arr(self.x_pos+i, self.y_pos)

    def print_out(self):
        """
        update the coordinates
        """
        for i in range(-1, 2):
            common.set_arr(self.x_pos+i, self.y_pos, "-")


class Marijuana(thing.Thing):
    """
    Marijuana or the points
    """
    def __init__(self, x):
        self.x_pos = x
        self.y_pos = common.MIDS_R - 4
        check.check(self.x_pos, self.y_pos, "Marijuana")
        self.print_out()

    def move(self, x, y='?', who='?'):
        try:
            self.refresh_out()
            super().move(x, y, who)
            self.print_out()
        except config.DeletedElement:
            pass

    def refresh_out(self):
        """
        refresh the coordinates
        """
        for j in range(0, 2):
            for i in range(-1, 2):
                common.reset_arr(self.x_pos+i, self.y_pos+j)

    def print_out(self):
        """
        update the coordinates
        """
        for j in range(0, 2):
            for i in range(-1, 2):
                common.set_arr(self.x_pos+i, self.y_pos+j, "$")


class Bullet(thing.Thing):
    """
    Bullet for the boss enemy
    """
    def __init__(self, x, y, dir):
        self.dir = dir
        super().__init__(x, y)
        self.print_out()

    def move(self, x, y='?', who='?'):
        try:
            self.refresh_out()
            super().move(x, y, who)
            self.print_out()
        except config.DeletedElement:
            pass

    def refresh_out(self):
        """
        refresh the coordinates
        """
        common.reset_arr(self.x_pos, self.y_pos)

    def print_out(self):
        """
        update the coordinates
        """
        common.set_arr(self.x_pos, self.y_pos, "-")


class Boss(thing.Thing):
    """
    Boss enemy , a smart one
    """
    def __init__(self, x, y):
        super().__init__(x, y)
        self.print_out()

    def move(self, x, y='?', who='?'):
        try:
            self.refresh_out()
            super().move(x, y, who)
            self.print_out()
        except config.DeletedElement:
            pass

    def shoot(self, x):
        dir = 0
        if x > self.x_pos:
            dir = 1
        else:
            dir = -1

        b = Bullet(self.x_pos+dir, self.y_pos, dir)
        config.B_LIST.append(b)

        for i in config.B_LIST:
            i.move(i.x_pos+i.dir)

    def refresh_out(self):
        """
        refresh the coordinates
        """
        for i in range(0, 3):
            for j in range(i-3, 3-i):
                common.reset_arr(self.x_pos+j, self.y_pos+i)

    def print_out(self):
        """
        update the coordinates
        """
        for i in range(0, 3):
            for j in range(i-3, 3-i):
                common.set_arr(self.x_pos+j, self.y_pos-i, "B")
