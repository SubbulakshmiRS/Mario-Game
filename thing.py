import common
import config

class Thing():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.print_out()

    def move(self,x,y=self.y):
        self.refresh_out()
        self.x=x
        self.y=y
        self.print_out()
    
    def move(self,x,y,who):
        if who in config.Obstacles :
            try :
                check.check_boundary(x,y)
                super().move(x)
            except config.Touch_Boundary:
                if who == "Wall":
                    w_list.remove(self)
                elif who == "Platform":
                    p_list.remove(self)
                elif who == "Gap":
                    g_list.remove(self)                   
                else:
                    m_list.remove(self)


    def check(self):
        if (self.y >= common.mids_r and common.value_arr(self.x,self.y+1) != '0' ):
            raise config.Gap_Here

    def change(self,x,y):
        self.x = x
        self.y = y



            