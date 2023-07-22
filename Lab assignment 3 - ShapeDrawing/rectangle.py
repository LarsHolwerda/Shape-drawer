from shape import Shape
from tkinter import Canvas
from format import FormatInterface

class Rectangle(Shape):

    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x,y)
        self.width: int = width
        self.height: int = height
        

    def visualize(self):
        self.format.draw_polygon([self.x, self.y,
                           self.x + self.width, self.y,
                           self.x + self.width, self.y + self.height,
                           self.x, self.y + self.height,
                           self.x, self.y])