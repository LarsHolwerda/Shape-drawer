from tkinter import Canvas
from format import FormatInterface

class Shape():
    def __init__(self,x,y):
        self.format : FormatInterface = None
        self.x = x
        self.y = y
    
    