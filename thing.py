import config
import check

# the core class - for checking the boundary

class Thing():
    """
    Core class for all elements of the board
    """
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, x_pos, y_pos='?', who='?'):
        """
        Move
        """
        # polymorphism
        if who == '?':
            who = self.__class__.__name__
        if y_pos != '?':
            self.y_pos = y_pos
        self.x_pos = x_pos

        if who in config.ELEMENTS:
            try:
                check.check_boundary(self.x_pos+4, self.y_pos)
            except config.TouchBoundary:
                if who == "Wall":
                    config.W_LIST.remove(self)
                elif who == "Platform":
                    config.P_LIST.remove(self)
                elif who == "Gap":
                    config.G_LIST.remove(self)
                elif who == "Marijuana":
                    config.M_LIST.remove(self)
                elif who == "Fish":
                    config.F_LIST.remove(self)
                elif who == "Star":
                    config.S_LIST.remove(self)
                elif who == "Boss":
                    config.B = ""
                elif who == "Bullet":
                    config.B_LIST.remove(self)
                raise config.DeletedElement

    def change(self, x_pos, y_pos):
        """
        change center coordinates of that element
        """
        self.x_pos = x_pos
        self.y_pos = y_pos
