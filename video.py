from manim import *

class V(Scene):
    """ Shows the steps for deriving `u`. """
    def construct(self):
        text1 = MathTex("u\'=\\frac{u-v}{1-\\frac{uv}{c^2}}")
        self.play(Write(text1, run_time=1.5))
        self.wait()

        text2 = MathTex("(1-\\frac{uv}{c^2})u\'=u-v")
        self.play(ReplacementTransform(text1, text2, run_time=1.5))
        self.wait()

        text3 = MathTex("u\'-\\frac{uu\'v}{c^2}=u-v")
        self.play(ReplacementTransform(text2, text3, run_time=1.5))
        self.wait()

        text4 = MathTex("\\frac{uu\'v}{c^2}-u'=v-u")
        self.play(ReplacementTransform(text3, text4, run_time=1.5))
        self.wait()

        text5 = MathTex("u(\\frac{u\'v}{c^2}+1)=u\'+v")
        self.play(ReplacementTransform(text4, text5, run_time=1.5))
        self.wait()

        text6 = MathTex("u=\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}")
        self.play(ReplacementTransform(text5, text6, run_time=1.5))
        self.wait()

class CSubstitution(Scene):
    """ Shows the invariance of `c`. """
    def construct(self):
        text1 = MathTex("u\'=\\frac{u-v}{1-\\frac{uv}{c^2}}")
        self.play(Write(text1, run_time=1.5))
        self.wait()

        text2 = MathTex("u\'=\\frac{c-v}{1-\\frac{cv}{c^2}}")
        self.play(ReplacementTransform(text1, text2, run_time=1.5))
        self.wait()

        text3 = MathTex("u\'=\\frac{c-v}{1-\\frac{v}{c}}")
        self.play(ReplacementTransform(text2, text3, run_time=1.5))
        self.wait()

        text4 = MathTex("u\'=\\frac{c-v}{\\frac{c-v}{c}}")
        self.play(ReplacementTransform(text3, text4, run_time=1.5))
        self.wait()

        text5 = MathTex("u\'=\\frac{c-v}{c-v}c")
        self.play(ReplacementTransform(text4, text5, run_time=1.5))
        self.wait()

        text6 = MathTex("u\'=c")
        self.play(ReplacementTransform(text5, text6, run_time=1.5))
        self.wait()

class VerySmallSpeed(Scene):
    """ Shows how to derive the Galilean transformation. """
    def construct(self):
        upper_text = MathTex("u\'=\\frac{u-v}{1-\\frac{uv}{c^2}}")        

        group = VGroup(
            Text("Se "),
            MathTex("v<<c"),
            Text(" e "),
            MathTex("u<<c"),
            Text(", allora")
        )
        # the order matters!
        group.arrange(RIGHT)
        group.to_edge(UP)

        self.play(Write(upper_text, run_time=1.5))
        self.wait()

        lower_text = MathTex("u\'=\\frac{u-v}{1-\\frac{uv}{c^2}}") 
        lower_text.to_edge(DOWN)

        self.play(FadeTransform(upper_text, lower_text), Create(group, run_time=1))
        self.wait()

        approx1 = MathTex("u\'\\approx\\frac{u-v}{1-0}")
        self.play(Write(approx1, run_time=1.5))
        self.wait()

        approx2 = MathTex("u\'\\approx u-v")
        self.play(ReplacementTransform(approx1, approx2, run_time=1.5))
        self.wait()

        text = Text("Trasformazione di Galileo")
        text.next_to(approx2, UP)
        self.play(Write(text, run_time=1.5))

class Demonstration(GraphScene):
    """ Shows the first part of the demonstration of the relativity addition formula. """
    def construct(self):
        self.x_axis_label = "$t$"
        self.y_axis_label = "$x$"
        
        self.setup_axes(animate=True)

        parabola = lambda x: -1/4 * x ** 2 + 4 * x - 10

        graph = self.get_graph(parabola, x_min=5, x_max=8, color=RED)

        # i wasn't able to draw horizontal lines
        t1 = self.get_vertical_line_to_graph(5, graph, color=WHITE)
        t2 = self.get_vertical_line_to_graph(8, graph, color=WHITE)

        self.play(Create(graph), Create(t1), Create(t2))

        sec = self.get_secant_slope_group(5, graph, dx=3) # 3 = 5 - 8, dx starts from x

        text1 = MathTex("u=\\frac{\\Delta x}{\\Delta t}=\\frac{x_2-x_1}{t_2-t_1}")
        text1.to_edge(UP)

        self.play(Write(text1, run_time=2), Create(sec, run_time=2))
        self.wait()

        text2 = MathTex("u\'=\\frac{\\Delta x\'}{\\Delta t\'}=\\frac{x_2\'-x_1\'}{t_2\'-t_1\'}")
        text2.to_edge(UP)
        self.play(ReplacementTransform(text1, text2, run_time=1.5))
        self.wait()

class Demonstration2(Scene):
    """ Shows the second part of the demonstration of the relativity addition formula. """
    def construct(self):
        group = VGroup(
            Text("Per"),
            MathTex("x=x\'=0m"),
            Text(" e "),
            MathTex("t=t\'=0s"),
            Text(" :")
        )
        # the order matters!
        group.arrange(RIGHT)
        group.to_edge(UP)

        self.play(Create(group, run_time=1.5))
        self.wait()

        system = MathTex("""
\\left\{\\begin{matrix} x\'=\\gamma (x-vt)
\\\ y\'=y
\\\ z\'=z
\\\ t\'=\\gamma (t-\\frac{vx}{c^2})
\\end{matrix}\\right.
        """)
        self.play(Write(system, run_time=1.5))
        self.wait()

        formula = MathTex("\\frac{x\'}{t\'}=\\frac{\\gamma (x-vt)}{\\gamma (t-\\frac{vx}{c^2})}")
        self.play(ReplacementTransform(system, formula, run_time=1.5))
        self.wait()

        formula2 = MathTex("\\frac{x\'}{t\'}=\\frac{x-vt}{t-\\frac{vx}{c^2}}")
        self.play(ReplacementTransform(formula, formula2, run_time=1.5))
        self.wait()

        formula3 = MathTex("\\frac{\\Delta x\'}{\\Delta t\'}=\\frac{(x_2-vt_2)-(x_1-vt_1)}{(t_2-\\frac{vx_2}{c^2})-(t_1-\\frac{vx_1}{c^2})}")
        self.play(ReplacementTransform(formula2, formula3, run_time=1.5))
        self.wait()

        formula4 = MathTex("u\'=\\frac{x_2-vt_2-x_1+vt_1}{t_2-\\frac{vx_2}{c^2}-t_1+\\frac{vx_1}{c^2}}")
        self.play(ReplacementTransform(formula3, formula4, run_time=1.5))
        self.wait()

        formula5 = MathTex("u\'=\\frac{(x_2-x_1)-v(t_2-t_1)}{(t_2-t_1)-\\frac{v}{c^2}(x_2-x_1)")
        self.play(ReplacementTransform(formula4, formula5, run_time=1.5))
        self.wait()

        formula6 = MathTex("u\'=\\frac{u(t_2-t_1)-v(t_2-t_1)}{(t_2-t_1)-\\frac{uv}{c^2}(t_2-t_1)")
        self.play(ReplacementTransform(formula5, formula6, run_time=1.5))
        self.wait()

        formula7 = MathTex("u\'=\\frac{(t_2-t_1)(u-v)}{(t_2-t_1)(1-\\frac{uv}{c^2})")
        self.play(ReplacementTransform(formula6, formula7, run_time=1.5))
        self.wait()

        formula8 = MathTex("u\'=\\frac{u-v}{1-\\frac{uv}{c^2}")
        self.play(ReplacementTransform(formula7, formula8, run_time=1.5))
        self.wait()
