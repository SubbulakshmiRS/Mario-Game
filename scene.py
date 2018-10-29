"""
The scene elements which wont collide with other elements
"""
import config
import common
import thing


class Star(thing.Thing):
    """
    Stars , present in the top quarter
    """
    def __init__(self, x, y):
        super().__init__(x, y)
        self.print_out()

    def move(self, x, y='?', who='?'):
        try:
            self.refresh_out()
            super().move(x,y,"Star")
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
        common.set_arr(self.x_pos, self.y_pos, "*")


class Fish(thing.Thing):
    """
    Fish present under the floor/ground level
    """
    def __init__(self, x, y):
        super().__init__(x, y)
        self.print_out()
    
    def move(self, x, y='?', who='?'):
        try:
            self.refresh_out()
            super().move(x,y,"Fish")
            self.print_out()
        except config.DeletedElement:
            pass

    def refresh_out(self):
        """
        refresh the coordinates
        """
        for i in range(-1, 3):
            for j in range(-1, 2):
                if i == 0:
                    common.reset_arr(self.x_pos+i, self.y_pos+j)
                else:
                    common.reset_arr(self.x_pos+i, self.y_pos)

    def print_out(self):
        """
        update the coordinates
        """
        for i in range(-1, 3):
            for j in range(-1, 2):
                if i == 0:
                    common.set_arr(self.x_pos+i, self.y_pos+j, "@")
                else:
                    common.set_arr(self.x_pos+i, self.y_pos, "@")
