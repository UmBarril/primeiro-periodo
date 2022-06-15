# manim -pql .\introducao.py Introducao

# manim -qm Introducao
from manim import *

config.media_width = "75%"
config.verbosity = "WARNING"

class Introducao(Scene):
    def construct(self):
        # pt 1
        rectangle = Rectangle(GREEN)
        rectangle.set_fill(GREEN)
        
        # pt 2
        triangle = Triangle()
        triangle.set_fill(YELLOW, opacity=1)
        
        # pt 3
        polygon = RegularPolygon(5)

        self.add(rectangle)
        self.play(Create(rectangle))
        self.wait(2)
        #self.add(triangle)
        self.play(Transform(rectangle, triangle))
        self.wait(2)

        position_list = [
            [4, 1, 0],  # middle right
            [4, -2.5, 0],  # bottom right
            [0, -2.5, 0],  # bottom left
            [0, 3, 0],  # top left
            [2, 1, 0],  # middle
            [4, 3, 0],  # top right
        ]
        real_pol = Polygon(*position_list, color=PURPLE_B)
        #self.add(real_pol)
        self.play(Transform(triangle, real_pol))