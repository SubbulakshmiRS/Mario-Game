import config
import common
import thing


class Star(thing.Thing):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.print_out()

    def move(self, x, y='?', who='?'):
        try:
            self.refresh_out()
            super().move(x, self.y_pos, "Star")
            self.print_out()
        except config.DeletedElement:
            pass

    def refresh_out(self):
        common.reset_arr(self.x_pos, self.y_pos)

    def print_out(self):
        common.set_arr(self.x_pos, self.y_pos, "*")


class Fish(thing.Thing):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.print_out()

    def move(self, x, y='?', who='?'):
        try:
            self.refresh_out()
            super().move(x, self.y_pos, "Fish")
            self.print_out()
        except config.DeletedElement:
            pass

    def refresh_out(self):
        for i in range(-1, 3):
            for j in range(-1, 2):
                if i == 0:
                    common.reset_arr(self.x_pos+i, self.y_pos+j)
                else:
                    common.reset_arr(self.x_pos+i, self.y_pos)

    def print_out(self):
        for i in range(-1, 3):
            for j in range(-1, 2):
                if i == 0:
                    common.set_arr(self.x_pos+i, self.y_pos+j, "@")
                else:
                    common.set_arr(self.x_pos+i, self.y_pos, "@")
