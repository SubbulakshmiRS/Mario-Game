import common
import config
import check

class Thing():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.print_out()

    def move(self,x,y='?',who='?'):
        if who == '?':
            self.refresh_out()
            self.x = x
            if y !='?':
                self.y = y
            self.print_out()
        else :
            self.move_who(x,y,who)

    def move_who(self,x,y,who):
        if who in config.Obstacles :
            try :
                check.check_boundary(x,y)
                self.refresh_out()
                self.x = x
                self.print_out()
            except config.Touch_Boundary:
                if who == "Wall":
                    config.w_list.remove(self)
                elif who == "Platform":
                    config.p_list.remove(self)
                elif who == "Gap":
                    config.g_list.remove(self)                   
                elif who == "Marijuana" :
                    config.m_list.remove(self)
                

    def change(self,x,y):
        self.x = x
        self.y = y



            