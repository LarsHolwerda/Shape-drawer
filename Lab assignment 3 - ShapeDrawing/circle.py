from shape import Shape
from tkinter import Canvas
from format import FormatInterface

#from svgformat import Svgformat
#from pythonformat import Pythonformat

class Circle(Shape):

    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x,y)
        self.radius: int = radius
        

    def visualize(self):
        self.format.draw_circle(self.x,self.y,self.radius)

    