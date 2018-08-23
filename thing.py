import common
import config
import check

#the core class - for checking the boundary 
class Thing():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.print_out()

    def move(self,x,y='?',who='?'):
        #polymorphism
        if who == '?':
            self.refresh_out()
            self.x = x
            if y !='?':
                self.y = y
            self.print_out()
        else :
            self.move_who(x+4,y,who)

    def move_who(self,x,y,who):
        if who in config.Elements :
            try :
                check.check_boundary(x,y)
                self.refresh_out()
                self.x = x-4
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
                elif who == "Fish":
                    config.f_list.remove(self)
                elif who == "Star":
                    config.s_list.remove(self)
                elif who == "Boss":
                    config.b = ""
                elif who == "Bullet" :
                    config.b_list.remove(self)

                

    def change(self,x,y):
        self.x = x
        self.y = y



            