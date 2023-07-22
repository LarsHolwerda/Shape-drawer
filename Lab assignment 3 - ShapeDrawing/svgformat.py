from format import FormatInterface

class SvgFormat(FormatInterface):
  def __init__(self):
    self.begin = """<?xml version="1.0" standalone="no"?>
    <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
    "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
    <svg xmlns="http://www.w3.org/2000/svg" version="1.1">"""
    self.end = """</svg>"""
    self.figures = ""
  def draw_circle(self, x,y,radius):
    circle = f"""<circle cx="{x}" cy="{y}" r="{radius}" stroke-width="1" fill="none" stroke="black" />"""
    self.figures += circle
  def draw_polygon(self,points):
    polygon = f"""<polyline points="{" ".join([str(elem) for elem in points])}" style="fill:none;stroke:black;stroke-width:1" />"""
    self.figures += polygon
  def save(self):
    with open("shapes.svg", "w") as svg_file:
      svg_file.write(self.begin + self.figures + self.end)
