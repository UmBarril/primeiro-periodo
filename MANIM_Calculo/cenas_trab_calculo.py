from cmath import sqrt
from re import L
from manim import *
import math
import scipy.special
import numpy as np
# manim -pql .\introducao.py Introducao

class AreaQuadrado(Scene):
    def construct(self):
        ParametricFunction()
        self.camera.background_color = WHITE
        square = Square(color=BLUE, fill_opacity=1)

        self.play(DrawBorderThenFill(square), square.animate.shift(LEFT))
        text=MathTex("base \\times altura", color=BLACK).next_to(square)
        text.set_color(BLACK)
        self.play(Write(text))
        b1 = Brace(square, direction=[0,1])
        self.add(b1)
        self.play(FadeIn(b1))
        self.wait()

class AreaTriangulo(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        triangle = Triangle(color=GREEN, fill_opacity=1)
        triangle.scale(1.5)

        self.play(DrawBorderThenFill(triangle), triangle.animate.shift(LEFT))
        text=MathTex("\\frac{base \\times altura}{2}", color=BLACK).next_to(triangle)
        text.set_color(BLACK)
        self.play(Write(text))
        b1 = Brace(triangle, direction=[0,1])
        self.add(b1)
        self.play(FadeIn(b1))
        self.wait()
        
class AreaPoligono(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        trapPoints=[
            (0,0,0),
            (3,0,0),
            (4,2,0),
            (1,2,0)
        ]
        trapezio = Polygon(*trapPoints, color=RED)
        trapezio.set_fill(RED, opacity=1)
        self.play(DrawBorderThenFill(trapezio))
        trianglePoints = [
            (3,0,0),
            (4,2,0),
            (3,2,0)
        ]
        triangle = Polygon(*trianglePoints)
        triangle.set_stroke(width=4)
        triangle.set_fill(PURPLE, opacity=1)

        white_triangle = triangle.copy()
        white_triangle.set_fill(color=WHITE, opacity=1)
        white_triangle.set_stroke(color=BLACK, width=5)

        texto1 = Text("altura")
        texto1.set_color(color=BLACK)
        texto1.next_to(triangle, 0.8*LEFT)
        texto1.scale(0.5)

        self.play(DrawBorderThenFill(triangle), Create(texto1))
        grupo_texto_triangulo = VGroup(triangle, texto1)
        self.play(grupo_texto_triangulo.animate.shift(LEFT*3), Create(white_triangle))
        self.wait()

class IntroMegaEpica(Scene):
    def construct(self):
        text = Text("Integrais: ")
        text.shift(LEFT*1.5)
        self.play(Write(text))
        text1 = Text("Introdução", slant=ITALIC, color=BLUE)
        text1.next_to(text, RIGHT)
        self.wait(1)
        self.play(Write(text1))
        self.wait(3)
        self.play(text.animate.shift(LEFT * 10), text1.animate.shift(RIGHT * 10))
        self.wait(1)

class FuncoespPrimitivas(Scene):
    def construct(self):
        text = Text("Funções primitivas")
        self.play(Write(text))
        self.wait(2)
        self.play(text.animate.shift(LEFT * 10))
        self.wait(1)

class RevisaoDerivadas(Scene):
    def construct(self):
        desc_der = Text("Definição de Derivada")
        formula_der = MathTex("f'(x)=\\lim_{\\Delta x \\to 0}\\frac{(f(x)+\\Delta x)-f(x)}{\\Delta x}") 
        desc_der.next_to(formula_der, UP)
        grupo1 = Group(formula_der, desc_der)
        self.play(Write(formula_der), Write(desc_der))
        self.wait(10)
        self.play(grupo1.animate.scale(0.5).move_to(LEFT * 3))
        desc_leibniz = Text("Notação de Leibniz")
        formula_leibniz = MathTex(r"\frac{dy}{dx}").scale(1.2)
        desc_leibniz.next_to(formula_leibniz, UP)
        grupo2 = Group(formula_leibniz, desc_leibniz)
        grupo2.shift(RIGHT * 2)
        self.play(Write(formula_leibniz), Write(desc_leibniz))
        self.wait(10)
        self.play(grupo2.animate.scale(0.5).move_to(RIGHT * 3))
        self.wait(5)

        self.play(grupo2.animate.move_to(RIGHT * 15), grupo1.animate.move_to(LEFT * 15))

        desc_potencia = Text("Regra da potência")
        f_regra_potencia = MathTex(r"\frac{d}{dx}(x^n)=nx^{n-1}")
        desc_potencia.next_to(f_regra_potencia, UP)
        grupo3 = Group(desc_potencia, f_regra_potencia)
        self.play(Write(f_regra_potencia), Write(desc_potencia))
        self.wait(15)
        self.play(FadeOut(grupo3))

class IntroducaoIntegrais(Scene):
    def construct(self):
        desc_leibniz = Text("Notação de Leibniz")
        formula_leibniz = MathTex(r"\frac{dy}{dx}").scale(1.2)
        desc_leibniz.next_to(formula_leibniz, UP)
        grupo2 = Group(formula_leibniz, desc_leibniz)
        grupo2.scale(0.5)
        grupo2.shift(RIGHT * 10)
        self.play(grupo2.animate.scale(2).move_to(0))
        self.wait(2)
        self.play(Rotate(grupo2, angle=PI, rate_func=smooth))
        self.wait(1)
        line1 = DashedLine((-1,-1,0), (1,1,0))
        line1.set_stroke(color=RED, width=5)
        line2 = DashedLine((1,-1,0), (-1,1,0))
        line2.set_stroke(color=RED, width=5)
        X_drawing = VGroup(line1,line2)
        X_drawing.scale(2)
        self.play(Create(X_drawing))
        self.wait(5)
        self.play(Group(X_drawing, grupo2).animate.shift(RIGHT*20))
        self.wait(5)
        formula = MathTex(r"\int_a^b ")
        self.play(Write(formula))
        self.wait(5)

class Perguntitas(Scene):
    def construct(self):
        text = Text("O que é integração? ")
        text.move_to(UP*2)
        self.play(Write(text, rate_func=rush_into))
        self.wait(2)
        text2 = Text("Por que foi importante")
        text2continuacao = Text("fazer tal relação com derivadas?")
        text2.next_to(text, DOWN)
        text2.shift(DOWN)
        text2continuacao.next_to(text2, DOWN)
        self.play(Write(text2))
        self.play(Write(text2continuacao))
        self.wait(2)
        self.play(Group(text,text2,text2continuacao).animate.shift(LEFT*20))
        self.wait()


class ArchimedesMethod(Scene):
    def construct(self):
        def draw_lines_to_center(polygon: Polygon):
            vertices_list = polygon.get_vertices()
            group = VGroup(polygon)
            for vertice in vertices_list:
                line = Line(vertice, (0,0,0))
                line.set_color(BLACK)
                group.add(line)
            return group
            
        def get_perimeter(sides):
            return sides * math.sin(PI/sides)

        self.camera.background_color = WHITE
        circle = Circle()
        circle.scale(1)

        first_polygon = RegularPolygon(4) # square
        first_polygon = draw_lines_to_center(first_polygon)

        text = MathTex("\\pi = ")
        number = DecimalNumber(get_perimeter(4), 4)
        text.next_to(circle, RIGHT)
        number.next_to(text, RIGHT)
        lbl_group = VGroup(text, number)

        self.play(Create(circle), Create(first_polygon), Create(lbl_group))
        self.wait(1)

        last_polygon = first_polygon
        max_num_vertices = 20
        for number_of_vertices in range(5, max_num_vertices):
            polygon = RegularPolygon(number_of_vertices)

            number.set_value(get_perimeter(number_of_vertices))
            lined_poly = draw_lines_to_center(polygon)

            self.play(ReplacementTransform(last_polygon, lined_poly))
            self.wait(1)

            last_polygon = lined_poly

class AreaCirculo(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        circle = Circle(color=GREEN, fill_opacity=1)
        circle.scale(1.5)

        self.play(DrawBorderThenFill(circle), circle.animate.shift(LEFT))
        text=MathTex("area = ???", color=BLACK).next_to(circle)
        text.set_color(BLACK)
        self.play(Write(text))

class CrazyShapes(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        circle = Circle().set_fill(color=RED, opacity=1)
        self.play(Create(circle))
        self.wait(2)
        last_form = circle
        what = VGroup()
        colors = [PURPLE, GREEN_B, BLUE_B]
        for shapesnum in range(2):
            vertices = 5 + 2 * shapesnum
            # a = NDArray
            polygon = RegularPolygon(vertices,color=WHITE)
            polygon.set_fill(color=colors[shapesnum],opacity=1)
            polygon.scale(2)
            #polygon.get_fill_rgbas(random.random())
            self.play(ReplacementTransform(last_form, polygon))
            self.wait(1)
            last_form = polygon

        position_list = [
            [0, -2.5, 0],  # bottom right
            [-2, 2, 0],  # top left
            [0, 1, 0],  # middle
            [1, 2, 0],  # top middle
            [2, 0, 0],  # top right
        ]
        polygon = Polygon(*position_list)
        polygon.set_fill(color=colors[shapesnum],opacity=1)
        self.play(ReplacementTransform(last_form, polygon))
        self.wait(2)
        self.play(FadeOut(polygon))

        self.wait(2)

class Grafico(Scene):
    def construct(self):
        backg_plane = NumberPlane(x_range=[7,-7], x_length=5, y_range=[-4,4], y_length=5)
        backg_plane.add_coordinates()
        
        line = Line(start=backg_plane.c2p(0, ))
        self.play(FadeIn(backg_plane))        
        self.play(backg_plane.animate.set_opacity(0.2))

class DefinicaoDerivadass(Scene):
    def construct(self):
        text1 = Text("Uma derivada é: ")
        text = MarkupText(font_size=20, 
            text=f'"a medida da <span fgcolor="{YELLOW}">mudança do valor de uma função</span> em relação ao seu <span fgcolor="{YELLOW}">argumento de entrada</span>"')
        text1.next_to(text, UP*2)
        self.play(Write(text1), Write(text))
        self.wait(10)

class Primitivas(Scene):
    def construct(self):
        text=MathTex(
            r"F(x) = \int f(x)\Delta x"
        )
        self.play(Write(text))
        self.wait(10)
        text2 = MathTex(
            r"\frac{F(x)}{\Delta x} = f(x)?"
        )
        self.play(
            ReplacementTransform(text,text2),
        )
        self.wait(10)
        nsei = MathTex(
            r"A = f{x}\times\Delta x"
        )
        self.play(
            ReplacementTransform(text2,nsei),
        )
        self.wait(10)
        fraction = MathTex(
            r"h = \frac{f(x) - n}{\Delta x}"
        )
        self.play(
            ReplacementTransform(nsei,fraction),
        )
        self.wait(10)
        flinha=MathTex(
            r"F'(x) = f(x)"
        )
        self.play(
            ReplacementTransform(fraction,flinha),
        )
        self.wait(10)
        # 1 prop
        prop1=MathTex(
            r"C\times\int f(x)dx = \int C\times f(x)dx"
        )
        self.play(
            ReplacementTransform(flinha,prop1),
        )
        self.wait(10)
        # 2 prop
        prop2=MathTex(
            r"\int f(x) + g(x)dx=\int f(x)dx + \int g(x)dx"
        )
        self.play(
            ReplacementTransform(prop1,prop2),
        )
        self.wait(10)
        # 3 prop
        prop3=MathTex(
            r"\int f(x) - g(x)dx=\int f(x)dx - \int g(x)dx"
        )
        self.play(
            ReplacementTransform(prop2,prop3),
        )
        self.wait(10)
        # ???
        sla=MathTex(
            r"\int f(x) - g(x)dx + v(x)... -h(x)dx = \int f(x) - \int g(x) + \int v(x) ... - \int h(x)dx"
        )
        self.play(
            ReplacementTransform(prop3,sla),
        )
        self.wait(10)
        # Propriedade de soma e da subtração
        prop_soma=MathTex(
            r"\int (f(x) + g(x))dx =  \int f(x)dx + \int g(x)dx"
        )
        self.play(
            ReplacementTransform(sla,prop_soma),
        )
        self.wait(10)
        prop_sub=MathTex(
            r"\int (f(x) - g(x))dx =  \int f(x)dx - \int g(x)dx"
        )
        self.play(
            ReplacementTransform(prop_soma,prop_sub),
        )
        self.wait(10)



class MovingFrameBox(Scene):
    def construct(self):
        texty=MathTex(
            r"Área = \int_{a}^{b} f(x_{i})\Delta x =", r"\lim_{x\to\infty} \sum_{n=1}^{n}", r"\frac{b-a}{n}",  r"\times f(x_{i})"
        )
        text = texty.copy()
        self.play(Write(text))
        self.wait(5)
        framebox1 = SurroundingRectangle(text[2], buff = .1)
        # framebox2 = SurroundingRectangle(text[3], buff = .1)
        self.play(
            Create(framebox1),
        )
        text2 = MathTex(r"\Delta x=\frac{b-a}{n}")
        self.wait(10)
        self.remove(framebox1)
        self.play(
            ReplacementTransform(text,text2),
        )
        self.wait(15)
        text3 = MathTex(r"Área = \int_{a}^{b} f(x_{i})\Delta x")
        self.play(
            ReplacementTransform(text2,text3),
        )
        self.wait(15)
        text4 = MathTex(r"\lim_{x\to\infty} \sum_{n=1}^{n}", r"\frac{b-a}{n}",  r"\times f(x_{i})")
        self.play(
            ReplacementTransform(text3,text4),
        )
        self.wait(10)
        self.play(
            ReplacementTransform(text4,texty),
        )
        self.wait(5)

class Parabola(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 20], y_range=[-50, 100, 10], axis_config={"include_tip": False}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")
        func = lambda x: x**2
        graph = ax.plot(func, color=MAROON)

        t1 = ValueTracker(10)
        t2 = ValueTracker(10)
        initial_point = [ax.coords_to_point(0, func(5))]
        dot1 = Dot(point=initial_point)
        initial_point = [ax.coords_to_point(0, func(10))]
        dot2 = Dot(point=initial_point)

        dot1.add_updater(
            lambda x: x.move_to(ax.c2p(t1.get_value(), func(t1.get_value())))
            )
        dot2.add_updater(
            lambda x: x.move_to(ax.c2p(t2.get_value(), func(t2.get_value())))
            )

        area = ax.get_area(graph, [func(t1.get_value()), func(t2.get_value())], color=RED, opacity=0.5)

        self.add(ax, labels, graph, dot1, dot2, area)
        # self.play(Create(dot1), Create(dot2), Create(area))
        # self.play(t1.animate.set_value(0))
        # self.play(t1.animate.set_value(10))
        self.wait(5)

# if __name__ == "__main__":
#     ArchimedesMethod().render()