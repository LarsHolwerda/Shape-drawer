from format import FormatInterface

class GrahicFormat(FormatInterface):
    def __init__(self,canvas):
        self.canvas = canvas  
    def draw_circle(self,x,y,radius):
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius)
    def draw_polygon(self,points):
        self.canvas.create_line(points)
