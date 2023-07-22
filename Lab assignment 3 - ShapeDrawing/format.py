from abc import ABC, abstractmethod

class FormatInterface(ABC):
    @abstractmethod
    def draw_circle(self, x,y,radius):
        pass
    @abstractmethod
    def draw_polygon(self,points):
        pass