from tkinter import Tk, Canvas, Frame, Menu, BOTH, filedialog
from rectangle import Rectangle
from circle import Circle
from star import Star
from shape_parser import Parser
from svgformat import SvgFormat
from graphicformat import GrahicFormat


class ShapeDrawing(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.widgets()
        self.shapes = []

    def widgets(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        fileMenu.add_command(label="Clear", command=self.onClear)
        fileMenu.add_command(label="Export", command=self.onExport)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)

        self.master.title("Shape Drawing")
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self)
        self.canvas.pack(fill=BOTH, expand=1)
    
    def onOpen(self):
        file = filedialog.askopenfilename(title="Select file")

        if not file:
            return

        parser = Parser()
        self.shapes = parser.parse_shapes(file)
        self.canvas.delete("all")
        
        graphic_format = GrahicFormat(self.canvas)
        for shape in self.shapes:
            shape.format = graphic_format
            shape.visualize()

    def onClear(self):
        self.canvas.delete("all")
        self.shapes = []

    def onExport(self):
        svg_format = SvgFormat()
        for shape in self.shapes:
            shape.format = svg_format
            shape.visualize()
        svg_format.save()
        print("To do.")

    def onExit(self):
        self.quit()


def main():

    root = Tk()
    root.title("Shape Drawing")
    root.geometry("400x250+300+300")
    app = ShapeDrawing(root)

    root.mainloop()


if __name__ == '__main__':
    main()
