from manim import *

# \%%manim -qm -v WARNING SquareToCircle
# manim -pql .\teste.py SquareToCircle
# https://docs.manim.community/en/stable/tutorials/quickstart.html


class SquareToCircle(Scene):
    def construct(self):
        #circle = Circle()
        #circle.set_fill(RED, opacity=0.5)
        square = Triangle()
        square.flip(RIGHT)
        square.scale(3)
        square.rotate(PI) #TAU
        square.set_fill(BLUE, opacity=1.0)

        poly = Polygon(10)
        SVGMobject()

        # a = FRAME_HEIGHT
        # plane = ComplexPlane([10,10,1,1])
        plane = ComplexPlane()
        plane.set_color(RED)
        # plane.set_height(FRAME_HEIGHT)
        #plane.shift(self.plane_center)
        self.add(plane)

        self.play(Create(square))
        self.wait(2)
        #self.play(Transform(square, circle))
        #self.play(FadeOut(square))

class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number,  **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (int(alpha * (self.end - self.start)))
        self.mobject.set_value(value)


class CountingScene(Scene):
    def construct(self):
        # Create Decimal Number and add it to scene
        number = DecimalNumber().set_color(WHITE).scale(5)
        # Add an updater to keep the DecimalNumber centered as its value changes
        number.add_updater(lambda number: number.move_to(ORIGIN))

        self.add(number)

        self.wait()

        # Play the Count Animation to count from 0 to 100 in 4 seconds
        self.play(Count(number, 0, 50), run_time=5, rate_func=linear)

        self.wait():w
