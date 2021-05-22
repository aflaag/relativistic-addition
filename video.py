# GRAPHS CAN BE FOUND AT https://www.desmos.com/calculator/kgjbfb4nze

from manim import *

def set_color(text, index, interval, color):
    for char in interval:
        text[index][char].set_color(color)

class V(Scene):
    """ Shows the steps for deriving `u`. """
    def construct(self):
        text1 = MathTex("u\'=\\frac{u-v}{1-\\frac{uv}{c^2}}")
        self.play(Write(text1, run_time=1.5))
        self.wait(2)

        text2 = MathTex("(1-\\frac{uv}{c^2})u\'=u-v")
        self.play(ReplacementTransform(text1, text2, run_time=1.5))
        self.wait(2)# GRAPHS CAN BE FOUND AT https://www.desmos.com/calculator/kgjbfb4nze

from manim import *

def set_color(text, index, interval, color):
    for char in interval:
        text[index][char].set_color(color)

class V(Scene):
    """ Shows the steps for deriving `u`. """
    def construct(self):
        text1 = MathTex("u\'=\\frac{u-v}{1-\\frac{uv}{c^2}}")
        self.play(Write(text1, run_time=1.5))
        self.wait(2)

        self.play(
            text1[0][7].animate.set_color(ORANGE),
            text1[0][8].animate.set_color(ORANGE),
            text1[0][9].animate.set_color(ORANGE),
            text1[0][10].animate.set_color(ORANGE),
            text1[0][11].animate.set_color(ORANGE),
            text1[0][12].animate.set_color(ORANGE),
            text1[0][13].animate.set_color(ORANGE)
        )
        self.wait(2)

        text2 = MathTex("(1-\\frac{uv}{c^2})u\'=u-v")

        set_color(text2, 0, [0, 1, 2, 3, 4, 5, 6, 7, 8], ORANGE)

        self.play(FadeTransformPieces(text1, text2, run_time=1.5))
        self.wait(2)

        self.play(text2[0].animate.set_color(WHITE))
        self.wait(2)

        self.play(
            text2[0][9].animate.set_color(ORANGE),
            text2[0][10].animate.set_color(ORANGE)
        )
        self.wait(2)

        text3 = MathTex("u\'-\\frac{uu\'v}{c^2}=u-v")
        
        set_color(text3, 0, [0, 1, 4, 5], ORANGE)

        self.play(FadeTransformPieces(text2, text3, run_time=1.5))
        self.wait(2)

        self.play(text3[0].animate.set_color(WHITE))
        self.wait(2)

        self.play(
            text3[0][0].animate.set_color(ORANGE),
            text3[0][1].animate.set_color(ORANGE),
            text3[0][2].animate.set_color(ORANGE),
            text3[0][3].animate.set_color(ORANGE),
            text3[0][4].animate.set_color(ORANGE),
            text3[0][5].animate.set_color(ORANGE),
            text3[0][6].animate.set_color(ORANGE),
            text3[0][7].animate.set_color(ORANGE),
            text3[0][8].animate.set_color(ORANGE),
            text3[0][9].animate.set_color(ORANGE),

            text3[0][11].animate.set_color(ORANGE),
            text3[0][12].animate.set_color(ORANGE),
            text3[0][13].animate.set_color(ORANGE)
        )
        self.wait(2)

        text4 = MathTex("\\frac{uu\'v}{c^2}-u'=v-u")

        set_color(text4, 0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13], ORANGE)

        self.play(FadeTransformPieces(text3, text4, run_time=1.5))
        self.wait(2)

        self.play(text4[0].animate.set_color(WHITE))
        self.wait(2)

        self.play(
            text4[0][7].animate.set_color(ORANGE),
            text4[0][8].animate.set_color(ORANGE),
            text4[0][9].animate.set_color(ORANGE),

            text4[0][12].animate.set_color(ORANGE),
            text4[0][13].animate.set_color(ORANGE)
        )
        self.wait(2)

        text5 = MathTex("u(\\frac{u\'v}{c^2}+1)=u\'+v")

        set_color(text5, 0, [0, 8, 9, 12, 13], ORANGE)

        self.play(FadeTransformPieces(text4, text5, run_time=1.5))
        self.wait(2)

        self.play(text5.animate.set_color(WHITE))
        self.wait(2)

        self.play(
            text5[0][1].animate.set_color(ORANGE),
            text5[0][2].animate.set_color(ORANGE),
            text5[0][3].animate.set_color(ORANGE),
            text5[0][4].animate.set_color(ORANGE),
            text5[0][5].animate.set_color(ORANGE),
            text5[0][6].animate.set_color(ORANGE),
            text5[0][7].animate.set_color(ORANGE),
            text5[0][8].animate.set_color(ORANGE),
            text5[0][9].animate.set_color(ORANGE),
            text5[0][10].animate.set_color(ORANGE)
        )
        self.wait(2)

        text6 = MathTex("u=\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}")

        set_color(text6, 0, [7, 8, 9, 10, 11, 12, 13, 14], ORANGE)

        self.play(FadeTransformPieces(text5, text6, run_time=1.5))
        self.wait(2)

        self.play(text6.animate.set_color(WHITE))
        self.wait(2)

        self.play(Indicate(text6, color=ORANGE))
        self.wait(2)

class CSubstitution(Scene):
    """ Shows the invariance of `c`. """
    def construct(self):
        text1 = MathTex("u\'=\\frac{u-v}{1-\\frac{uv}{c^2}}")
        self.play(Write(text1, run_time=1.5))
        self.wait(2)

        ueqc = MathTex("u=c", color=RED)
        ueqc.to_edge(UP)
        ueqc.shift(DOWN * 0.6)

        self.play(Write(ueqc, run_time=1))
        self.wait(0.7)

        self.play(
            text1[0][3].animate.set_color(RED),
            text1[0][9].animate.set_color(RED)
        )
        self.wait(2)

        text2 = MathTex("u\'=\\frac{c-v}{1-\\frac{cv}{c^2}}")
        self.play(ReplacementTransform(text1, text2, run_time=1.5))
        self.wait(2)

        self.play(
            text2[0][9].animate.set_color(RED),
            text2[0][13].animate.set_color(RED),
        )
        self.wait(2)

        text3 = MathTex("u\'=\\frac{c-v}{1-\\frac{v}{c}}")
        self.play(FadeTransformPieces(text2, text3, run_time=1.5))
        self.wait(2)

        self.play(
            text3[0][7].animate.set_color(RED),
            text3[0][8].animate.set_color(RED),
            text3[0][9].animate.set_color(RED),
            text3[0][10].animate.set_color(RED),
            text3[0][11].animate.set_color(RED)
        )
        self.wait(2)

        text4 = MathTex("u\'=\\frac{c-v}{\\frac{c-v}{c}}")
        self.play(ReplacementTransform(text3, text4, run_time=1.5))
        self.wait(2)

        self.play(
            text4[0][10].animate.set_color(RED),
            text4[0][11].animate.set_color(RED)
        )
        self.wait(2)

        text5 = MathTex("u\'=\\frac{c-v}{c-v}c")
        self.play(FadeTransformPieces(text4, text5, run_time=1.5))
        self.wait(2)
        
        self.play(
            text5[0][3].animate.set_color(RED),
            text5[0][4].animate.set_color(RED),
            text5[0][5].animate.set_color(RED),
            text5[0][6].animate.set_color(RED),
            text5[0][7].animate.set_color(RED),
            text5[0][8].animate.set_color(RED),
            text5[0][9].animate.set_color(RED)
        )
        self.wait(2)

        text6 = MathTex("u\'=c")
        self.play(FadeTransformPieces(text5, text6, run_time=1.5))
        self.wait(0.8)

        last = MathTex(r"\mathrm{Invarianza\ della\ velocit}", r"\mathrm{\grave a}", r"\ \mathrm{della\ luce}", color=RED)
        last.next_to(text6, UP)

        lower_upper = MathTex("u=c", color=RED)
        lower_upper.next_to(text6, DOWN)

        self.play(Indicate(text6, color=RED), Write(last, run_time=1.5), ReplacementTransform(ueqc, lower_upper, run_time=1.5))
        self.wait(2)

class VerySmallSpeed(Scene):
    """ Shows how to derive the Galilean transformations. """
    def construct(self):
        upper_text = MathTex("u\'=\\frac{u-v}{1-\\frac{uv}{c^2}}")        

        group = VGroup(
            MathTex("\mathrm{Se\\ }"),
            MathTex("u<<c"),
            MathTex("\mathrm{\\ e\\ }"),
            MathTex("v<<c"),
            MathTex("\mathrm{,\\ allora}")
        )
        # the order matters!
        group.arrange(RIGHT)
        group.to_edge(UP)

        self.play(Write(upper_text, run_time=1.5))
        self.wait(2)

        lower_text = MathTex("u\'=\\frac{u-v}{1-\\frac{uv}{c^2}}") 
        lower_text.to_edge(DOWN)

        self.play(
            upper_text[0][9].animate.set_color(BLUE),
            upper_text[0][10].animate.set_color(BLUE)
        )
        self.wait(2)

        set_color(lower_text, 0, [9, 10], BLUE)

        self.play(FadeTransform(upper_text, lower_text, run_time=1.5))
        self.play(Write(group, run_time=1))

        self.play(Indicate(group[1], color=BLUE))
        self.play(Indicate(group[3], color=BLUE))
        self.wait(2)

        approx1 = MathTex("u\'\\approx\\frac{u-v}{1-0}")

        approx1[0][-1].set_color(BLUE)

        self.play(Write(approx1, run_time=1.5))
        self.wait(2)

        approx2 = MathTex("u\'\\approx u-v")
        self.play(FadeTransformPieces(approx1, approx2, run_time=1.5))
        self.wait(2)

        text = MathTex("\mathrm{Trasformazione\\ di\\ Galileo}", color=BLUE)
        text.next_to(approx2, UP)
        self.play(Write(text, run_time=1.5), Indicate(approx2, color=BLUE))
        self.wait(2)

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
        self.wait(2)

        text2 = MathTex("u\'=\\frac{\\Delta x\'}{\\Delta t\'}=\\frac{x_2\'-x_1\'}{t_2\'-t_1\'}")
        text2.to_edge(UP)
        self.play(FadeTransform(text1, text2, run_time=1.5))
        self.wait(2)

class Demonstration2(Scene): # this scene is a mess!
    """ Shows the second part of the demonstration of the relativity addition formula. """
    def construct(self):
        group = VGroup(
            MathTex("\mathrm{Per\\ }"),
            MathTex("x=x\'=0 \mathrm{m}"),
            MathTex("\mathrm{\\ e\\ }"),
            MathTex("t=t\'=0 \mathrm{s}"),
            MathTex("\mathrm{\\ :}")
        )
        # the order matters!
        group.arrange(RIGHT)
        group.to_edge(UP)

        self.play(Write(group, run_time=1.5))
        self.play(Indicate(group[1], color="#7cbf00"))
        self.play(Indicate(group[3], color="#7cbf00"))
        self.wait(2)

        system = MathTex(r"""
\begin{cases}
    x' = \gamma(x-vt) \\
    y' = y \\
    z' = z \\
    t'\, = \gamma \left(t-\frac{vx}{c^2}\right)
\end{cases}
        """)
        self.play(Write(system, run_time=1.5))
        self.wait(2)

        lower_text = VGroup(
            MathTex(r"x'= \gamma (x-vt)", color="#e3af7f"),
            MathTex(r"t'= \gamma (t-\frac{vx}{c^2})", color="#e3af7f")
        )
        lower_text.arrange(DOWN)
        lower_text.to_edge(DOWN)
        lower_text.to_edge(RIGHT)

        rect1 = Rectangle(color="#e3af7f", height=0.6, width=3.1)
        rect2 = Rectangle(color="#e3af7f", height=0.7, width=3.2)
        rect1.shift(UP * 1.1 + RIGHT * 0.1) # upper
        rect2.shift(DOWN * 1.05 + RIGHT * 0.2) # lower

        self.play(Create(rect1, run_time=1.5), Create(rect2, run_time=1.5), Write(lower_text, run_time=1.5))
        self.play(Uncreate(rect1), Uncreate(rect2))
        self.wait(2)

        self.play(Unwrite(system, run_time=1.5))
        self.wait(2)

        forgot = MathTex(r"\frac{\Delta x'}{\Delta t'} = \frac{x_2' - x_1'}{t_2' - t_1'}")

        set_color(forgot, 0, [8, 9, 10, 12, 13, 14, 16, 17, 18, 20, 21, 22], "#e3af7f")

        self.play(Write(forgot, run_time=1.5))
        self.wait(2)
        
        formula3 = MathTex("\\frac{\\Delta x\'}{\\Delta t\'}=\\frac{\\gamma (x_2-vt_2)- \\gamma (x_1-vt_1)}{\\gamma (t_2-\\frac{vx_2}{c^2})- \\gamma (t_1-\\frac{vx_1}{c^2})}")

        set_color(formula3, 0, [8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], "#e3af7f")

        self.play(FadeTransformPieces(forgot, formula3, run_time=1.5))
        self.wait(2)

        self.play(formula3[0].animate.set_color(WHITE))
        self.wait(2)

        self.play(
            formula3[0][8].animate.set_color("#7cbf00"),
            formula3[0][18].animate.set_color("#7cbf00"),
            formula3[0][28].animate.set_color("#7cbf00"),
            formula3[0][41].animate.set_color("#7cbf00")
        )
        self.wait(2)

        no_gammas = MathTex("\\frac{\\Delta x\'}{\\Delta t\'}=\\frac{(x_2-vt_2)-(x_1-vt_1)}{(t_2-\\frac{vx_2}{c^2})-(t_1-\\frac{vx_1}{c^2})}")
        self.play(FadeTransform(formula3, no_gammas, run_time=1.5))
        self.wait(2)

        forgot3 = MathTex("\\frac{\\Delta x\'}{\\Delta t\'}=\\frac{x_2-vt_2-x_1+vt_1}{t_2-\\frac{vx_2}{c^2}-t_1+\\frac{vx_1}{c^2}}")

        self.play(FadeTransform(no_gammas, forgot3, run_time=1.5))
        self.wait(2)

        forgot2 = MathTex(r"u'= \frac{\Delta x'}{\Delta t'}", color="#64bd90")
        forgot2.to_edge(LEFT)
        forgot2.to_edge(DOWN)

        self.play(Write(forgot2, run_time=1.5))
        self.wait(2)

        self.play(
            forgot3[0][0].animate.set_color("#64bd90"),
            forgot3[0][1].animate.set_color("#64bd90"),
            forgot3[0][2].animate.set_color("#64bd90"),
            forgot3[0][3].animate.set_color("#64bd90"),
            forgot3[0][4].animate.set_color("#64bd90"),
            forgot3[0][5].animate.set_color("#64bd90"),
            forgot3[0][6].animate.set_color("#64bd90")
        )
        self.wait(2)

        formula4 = MathTex("u\'=\\frac{x_2-vt_2-x_1+vt_1}{t_2-\\frac{vx_2}{c^2}-t_1+\\frac{vx_1}{c^2}}")

        set_color(formula4, 0, [0, 1], "#64bd90")

        self.play(FadeTransform(forgot3, formula4, run_time=1.5))
        self.wait(2)

        self.play(
            Unwrite((forgot2), run_time=0.7),

            formula4[0][0].animate.set_color(WHITE),
            formula4[0][1].animate.set_color(WHITE),
            formula4[0][3].animate.set_color("#ff8e2b"),
            formula4[0][4].animate.set_color("#ff8e2b"),

            formula4[0][5].animate.set_color("#c29cff"),
            formula4[0][6].animate.set_color("#c29cff"),
            formula4[0][7].animate.set_color("#c29cff"),
            formula4[0][8].animate.set_color("#c29cff"),

            formula4[0][9].animate.set_color("#ff8e2b"),
            formula4[0][10].animate.set_color("#ff8e2b"),
            formula4[0][11].animate.set_color("#ff8e2b"),

            formula4[0][12].animate.set_color("#c29cff"),
            formula4[0][13].animate.set_color("#c29cff"),
            formula4[0][14].animate.set_color("#c29cff"),
            formula4[0][15].animate.set_color("#c29cff"),
            formula4[0][17].animate.set_color("#c29cff"),
            formula4[0][18].animate.set_color("#c29cff"),

            formula4[0][19].animate.set_color("#ff8e2b"),
            formula4[0][20].animate.set_color("#ff8e2b"),
            formula4[0][21].animate.set_color("#ff8e2b"),
            formula4[0][22].animate.set_color("#ff8e2b"),
            formula4[0][23].animate.set_color("#ff8e2b"),
            formula4[0][24].animate.set_color("#ff8e2b"),
            formula4[0][25].animate.set_color("#ff8e2b"),

            formula4[0][26].animate.set_color("#c29cff"),
            formula4[0][27].animate.set_color("#c29cff"),
            formula4[0][28].animate.set_color("#c29cff"),

            formula4[0][29].animate.set_color("#ff8e2b"),
            formula4[0][30].animate.set_color("#ff8e2b"),
            formula4[0][31].animate.set_color("#ff8e2b"),
            formula4[0][32].animate.set_color("#ff8e2b"),
            formula4[0][33].animate.set_color("#ff8e2b"),
            formula4[0][34].animate.set_color("#ff8e2b"),
            formula4[0][35].animate.set_color("#ff8e2b")
        )
        self.wait(2)

        formula5 = MathTex("u\'=\\frac{(x_2-x_1)-v(t_2-t_1)}{(t_2-t_1)-\\frac{v}{c^2}(x_2-x_1)")

        set_color(formula5, 0, [3, 4, 5, 6, 7, 8, 9], "#ff8e2b")

        set_color(formula5, 0, [10, 11, 12, 13, 14, 15, 16, 17, 18], "#c29cff")

        set_color(formula5, 0, [20, 21, 22, 23, 24, 25, 26], "#c29cff")

        set_color(formula5, 0, [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38], "#ff8e2b")

        self.play(FadeTransform(formula4, formula5, run_time=1.5))
        self.wait(2)

        self.play(formula5[0].animate.set_color(WHITE))
        self.wait(2)
        
        missing = MathTex(r"x = ut \Rightarrow \Delta x = u \Delta t", color="#7cbf00")
        missing.next_to(formula5, UP)

        self.play(
            Write(missing, run_time=1.5),

            formula5[0][3].animate.set_color("#7cbf00"),
            formula5[0][4].animate.set_color("#7cbf00"),
            formula5[0][5].animate.set_color("#7cbf00"),
            formula5[0][6].animate.set_color("#7cbf00"),
            formula5[0][7].animate.set_color("#7cbf00"),
            formula5[0][8].animate.set_color("#7cbf00"),
            formula5[0][9].animate.set_color("#7cbf00"),

            formula5[0][32].animate.set_color("#7cbf00"),
            formula5[0][33].animate.set_color("#7cbf00"),
            formula5[0][34].animate.set_color("#7cbf00"),
            formula5[0][35].animate.set_color("#7cbf00"),
            formula5[0][36].animate.set_color("#7cbf00"),
            formula5[0][37].animate.set_color("#7cbf00"),
            formula5[0][38].animate.set_color("#7cbf00"),
        )
        self.wait(2)

        formula6 = MathTex("u\'=\\frac{u(t_2-t_1)-v(t_2-t_1)}{(t_2-t_1)-\\frac{uv}{c^2}(t_2-t_1)")

        set_color(formula6, 0, [3, 4, 5, 6, 7, 8, 9, 10], "#7cbf00")
        
        set_color(formula6, 0, [29, 34, 35, 36, 37, 38, 39, 40], "#7cbf00")

        self.play(FadeTransform(formula5, formula6, run_time=1.5))
        self.wait(2)

        self.play(formula6[0].animate.set_color(WHITE), Unwrite(missing, run_time=0.7))
        self.wait(2)

        self.play(
            formula6[0][4].animate.set_color("#7cbf00"),
            formula6[0][5].animate.set_color("#7cbf00"),
            formula6[0][6].animate.set_color("#7cbf00"),
            formula6[0][7].animate.set_color("#7cbf00"),
            formula6[0][8].animate.set_color("#7cbf00"),
            formula6[0][9].animate.set_color("#7cbf00"),
            formula6[0][10].animate.set_color("#7cbf00"),

            formula6[0][13].animate.set_color("#7cbf00"),
            formula6[0][14].animate.set_color("#7cbf00"),
            formula6[0][15].animate.set_color("#7cbf00"),
            formula6[0][16].animate.set_color("#7cbf00"),
            formula6[0][17].animate.set_color("#7cbf00"),
            formula6[0][18].animate.set_color("#7cbf00"),
            formula6[0][19].animate.set_color("#7cbf00"),

            formula6[0][21].animate.set_color("#7cbf00"),
            formula6[0][22].animate.set_color("#7cbf00"),
            formula6[0][23].animate.set_color("#7cbf00"),
            formula6[0][24].animate.set_color("#7cbf00"),
            formula6[0][25].animate.set_color("#7cbf00"),
            formula6[0][26].animate.set_color("#7cbf00"),
            formula6[0][27].animate.set_color("#7cbf00"),
            
            formula6[0][34].animate.set_color("#7cbf00"),
            formula6[0][35].animate.set_color("#7cbf00"),
            formula6[0][36].animate.set_color("#7cbf00"),
            formula6[0][37].animate.set_color("#7cbf00"),
            formula6[0][38].animate.set_color("#7cbf00"),
            formula6[0][39].animate.set_color("#7cbf00"),
            formula6[0][40].animate.set_color("#7cbf00")
        )
        self.wait(2)

        formula7 = MathTex("u\'=\\frac{(t_2-t_1)(u-v)}{(t_2-t_1)(1-\\frac{uv}{c^2})")

        set_color(formula7, 0, [3, 4, 5, 6, 7, 8, 9, 16, 17, 18, 19, 20, 21, 22], "#7cbf00")

        self.play(ReplacementTransform(formula6, formula7, run_time=1.5))
        self.wait(2)

        formula8 = MathTex("u\'=\\frac{u-v}{1-\\frac{uv}{c^2}")
        self.play(FadeTransformPieces(formula7, formula8, run_time=1.5))
        self.wait(2)

        self.play(Indicate(formula8, color="#7cbf00"))
        self.wait(2)

class Derivative(Scene):
    """ Shows how to calculate the derivative of the function of the relativistic addiotion of velocities. """
    def construct(self):
        center = MathTex("\\frac{d}{du\'} u = \\frac{d}{du\'} \\frac{u\'+v}{\\frac{u\'v}{c^2}+1}")

        set_color(center, 0, [0, 1, 2, 3, 4, 7, 8, 9, 10, 11], "#6df26d")

        upper_text = MathTex("u=\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}")
        self.play(Write(upper_text, run_time=1.5))
        self.wait(2)

        lower_text = MathTex("u=\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}")
        lower_text.to_edge(UP)

        self.play(FadeTransform(upper_text, lower_text, run_time=1.5), Write(center, run_time=1.5))
        self.wait(2)

        idk = MathTex(r"\frac{d}{dx} \frac{f(x)}{g(x)} = \frac{f'(x) g(x) - f(x) g'(x)}{g(x)^2}")
        idk.to_edge(DOWN)

        idk[0].set_color(BLUE)

        self.play(Write(idk, run_time=1.5))
        self.wait(2)

        center2 = MathTex(r"\frac{d}{du'} u = ", r"\frac{ (1+ \frac{u' v}{c^2} ) - (u'+v) \frac{v}{c^2} } {(1+ \frac{u' v} {c^2})^2}")

        center2[1].set_color("#6df26d")

        self.play(ReplacementTransform(center, center2, run_time=1.5))
        self.wait(2)

        self.play(Unwrite(idk, run_time=0.7), center2.animate.set_color(WHITE))
        self.wait(2)

        self.play(
            center2[1][0].animate.set_color("#6df26d"),
            center2[1][1].animate.set_color("#6df26d"),
            center2[1][2].animate.set_color("#6df26d"),
            center2[1][3].animate.set_color("#6df26d"),
            center2[1][4].animate.set_color("#6df26d"),
            center2[1][5].animate.set_color("#6df26d"),
            center2[1][6].animate.set_color("#6df26d"),
            center2[1][7].animate.set_color("#6df26d"),
            center2[1][8].animate.set_color("#6df26d"),
            center2[1][9].animate.set_color("#6df26d"),
            center2[1][10].animate.set_color("#6df26d"),
            center2[1][11].animate.set_color("#6df26d"),
            center2[1][12].animate.set_color("#6df26d"),
            center2[1][13].animate.set_color("#6df26d"),
            center2[1][14].animate.set_color("#6df26d"),
            center2[1][15].animate.set_color("#6df26d"),
            center2[1][16].animate.set_color("#6df26d"),
            center2[1][17].animate.set_color("#6df26d"),
            center2[1][18].animate.set_color("#6df26d"),
            center2[1][19].animate.set_color("#6df26d"),
            center2[1][20].animate.set_color("#6df26d")
        )
        self.wait(2)

        center3 = MathTex(r"\frac{d}{du'} u = \frac{ 1+ \frac{u' v}{c^2} - \frac{u'v}{c^2} - \frac{v^2}{c^2} } {(1+ \frac{u' v} {c^2})^2}")

        set_color(center3, 0, [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], "#6df26d")

        self.play(ReplacementTransform(center2, center3, run_time=1.5))
        self.wait(2)

        self.play(center3.animate.set_color(WHITE))
        self.wait(2)

        self.play(
            center3[0][8].animate.set_color("#6df26d"),
            center3[0][9].animate.set_color("#6df26d"),
            center3[0][10].animate.set_color("#6df26d"),
            center3[0][11].animate.set_color("#6df26d"),
            center3[0][12].animate.set_color("#6df26d"),
            center3[0][13].animate.set_color("#6df26d"),
            center3[0][14].animate.set_color("#6df26d"),
            center3[0][15].animate.set_color("#6df26d"),
            center3[0][16].animate.set_color("#6df26d"),
            center3[0][17].animate.set_color("#6df26d"),
            center3[0][18].animate.set_color("#6df26d"),
            center3[0][19].animate.set_color("#6df26d"),
            center3[0][20].animate.set_color("#6df26d"),
            center3[0][21].animate.set_color("#6df26d")
        )
        self.wait(2)

        center4 = MathTex(r"\frac{d}{du'} u = \frac{ 1 - \frac{v^2}{c^2} } {(1+ \frac{u' v}{c^2})^2}")
        self.play(FadeTransformPieces(center3, center4, run_time=1.5))
        self.wait(2)

        self.play(
            center4[0][9].animate.set_color("#6df26d"),
            center4[0][10].animate.set_color("#6df26d"),
            center4[0][11].animate.set_color("#6df26d"),
            center4[0][12].animate.set_color("#6df26d"),
            center4[0][13].animate.set_color("#6df26d"),

            center4[0][20].animate.set_color("#6df26d"),
            center4[0][21].animate.set_color("#6df26d"),
            center4[0][22].animate.set_color("#6df26d"),
            center4[0][23].animate.set_color("#6df26d")
        )
        self.wait(2)

        idk2 = MathTex(r"\beta = \frac{v}{c} \Rightarrow")

        idk2_part = VGroup(
            MathTex(r"\frac{v^2}{c^2} = \beta ^ 2"),
            MathTex(r"\frac{v}{c^2} = \frac{\beta}{c}")
        )
        idk2_part.arrange(DOWN)
        idk2_part.next_to(idk2, RIGHT)

        idk2.set_color(BLUE)

        idk2_total = VGroup(idk2, idk2_part)
        idk2_total.to_edge(DOWN)
        idk2_total.shift(LEFT)
        idk2_total.set_color(BLUE)

        self.play(Write(idk2_total, run_time=1.5))
        self.wait(2)

        center5 = MathTex(r"\frac{d}{du'} u = \frac{1- \beta ^ 2} {(1 + \frac{\beta}{c} u')^2}")

        set_color(center5, 0, [9, 10, 15, 16, 17], "#6df26d")
        
        self.play(FadeTransformPieces(center4, center5, run_time=1.5))
        self.wait(2)

        self.play(Unwrite(idk2_total, run_time=0.7))
        self.play(center5.animate.set_color(WHITE))
        self.wait(2)

class StudyDerivative(GraphScene):
    """ Studies the graph of the derivative of the function of the relativistic addition of velocities, and then shows it. """
    def construct(self):
        segno = MathTex(r"\frac{d}{du'} u = \frac{1 - \beta^2}{(1 + \frac{\beta}{c} u')^2}", color=GREEN)
        segno.to_edge(UP)

        self.play(Write(segno, run_time=1.5))
        self.wait(2)

        domain = MathTex(r"\mathrm{D_{u } } : \forall u' \mid u' \neq - \frac{c}{\beta}", color="#f2aa00")
        domain.to_edge(UP)
        domain.to_edge(RIGHT)
        domain.shift(DOWN * 0.2)

        self.play(Write(domain, run_time=1.5))
        
        segno2 = MathTex(r"\mathrm{Numeratore:\ } 1 - \beta^2", color="#ddccaa")
        self.play(Write(segno2, run_time=1.5))
        self.wait(2)

        self.play(Unwrite(segno2, run_time=0.6))

        segno3 = MathTex(r"1 - \beta^2 > 0", color="#ddccaa")
        self.play(Write(segno3, run_time=1.5))
        self.wait(2)

        segno4 = MathTex(r"\beta^2 < 1", color="#ddccaa")
        self.play(FadeTransformPieces(segno3, segno4, run_time=1.5))
        self.wait(2)

        segno5 = MathTex(r"-1 < \beta < 1", color="#ddccaa")
        self.play(FadeTransformPieces(segno4, segno5, run_time=1.5))
        self.wait(2)

        segno6 = MathTex(r"-1 < \frac{v}{c} < 1", color="#ddccaa")
        self.play(FadeTransformPieces(segno5, segno6, run_time=1.5))
        self.wait(2)

        segno7 = MathTex(r"-c < v < c", color="#ddccaa")
        self.play(FadeTransformPieces(segno6, segno7, run_time=1.5))
        self.wait(2)

        segno8 = MathTex(r"\Rightarrow 1 - \beta^2 > 0 \ \forall v", color="#ddccaa")
        segno8.next_to(segno7, DOWN)

        self.play(Write(segno8, run_time=1.5))
        self.wait(2)

        self.play(Unwrite(segno7, run_time=0.6), Unwrite(segno8, run_time=0.6))
        self.wait(2)

        den = MathTex(r"\mathrm{Denominatore:\ } (1 + \frac{\beta}{c} u')^2", color="#babaff")

        self.play(Write(den, run_time=1.5))
        self.wait(2)

        self.play(Unwrite(den, run_time=0.6))

        den2 = MathTex(r"(1 + \frac{\beta}{c} u')^2 > 0", color="#babaff")
        self.play(Write(den2, run_time=1.5))
        self.wait(2)

        den3 = MathTex(r"\forall u' \mid 1 + \frac{\beta}{c} u' \neq 0", color="#babaff")
        den3.next_to(den2, DOWN)

        self.play(Write(den3, run_time=1.5))
        self.wait(2)

        den4 = MathTex(r"u' \neq - \frac{c}{ \beta}", color="#babaff")
        self.play(Unwrite(den2, run_time=0.7), ReplacementTransform(den3, den4, run_time=1.5))
        self.wait(2)

        den5 = MathTex(r"u' = - \frac{c}{\beta} \notin \mathrm{D_{u}}", color="#f2aa00")
        den5.next_to(den5, DOWN)

        self.play(Write(den5, run_time=1.5))
        self.wait(2)

        rect = Rectangle(color="#f2aa00", height=2.0, width=4.5)
        rect.to_edge(UP)
        rect.to_edge(RIGHT)
        rect.shift(RIGHT * 0.25 + UP * 0.35)

        self.play(Create(rect))
        self.play(Uncreate(rect))

        den6 = MathTex(r"u' = - \frac{c}{ \beta}", color="#babaff")
        den6.to_edge(RIGHT)

        self.play(FadeTransform(den4, den6), Unwrite(den5))

        self.x_axis_label = "$u\'$"
        self.y_axis_label = "$u$"
        self.x_min = -20
        self.x_max = 20
        self.y_min = -2
        self.y_max = 12
        self.graph_origin = ORIGIN + 3 * DOWN + 1.5 * LEFT
        self.x_axis_config = { "tick_frequency": 5 }
        self.y_axis_config = { "tick_frequency": 2 }

        self.setup_axes(animate=True)

        v = 1
        c = 3

        beta = v / c
        n = 1 - beta ** 2

        derivative = lambda x: n / (1 + beta * x / c) ** 2

        graph_before = self.get_graph(derivative, x_min=-20, x_max=1.1 * - c / beta, y_min=-5, y_max=20, color=GREEN)
        graph_after = self.get_graph(derivative, x_min=0.9 * - c / beta, x_max=20, y_min=-5, y_max=20, color=GREEN)

        asymptote = self.get_vertical_line_to_graph(1.001 * -c / beta, graph_before, color="#babaff")

        self.play(Create(graph_before, run_time=0.75))
        self.play(Create(graph_after, run_time=0.75))
        self.wait(2)

        self.play(Create(asymptote, run_time=1))
        self.wait(2)

class UGraph(GraphScene):
    """ Shows the change of v in the function of the relativistic addition of velocities. """
    def construct(self):
        self.x_axis_label = "$u\'$"
        self.y_axis_label = "$u$"
        self.x_min = -40
        self.x_max = 40
        self.y_min = -40
        self.y_max = 40
        self.graph_origin = ORIGIN
        self.x_axis_config = { "tick_frequency": 10 }
        self.y_axis_config = { "tick_frequency": 10 }

        self.setup_axes(animate=True)

        v = 1
        c = 3

        beta = v / c

        u_func = lambda x: (x + v) / (1 + (x * v) / c ** 2)

        u = MathTex(r"u = \frac{u'+v}{1+\frac{u'v}{c^2}}", color=GREEN)
        u.to_edge(UP)
        u.to_edge(RIGHT)

        graph_before1 = self.get_graph(u_func, x_min=-40, x_max=1.1 * - c / beta, y_min=-40, y_max=40, color=GREEN)
        graph_after1 = self.get_graph(u_func, x_min=0.9 * - c / beta, x_max=40, y_min=-40, y_max=40, color=GREEN)

        self.play(Create(graph_before1, run_time=0.75))
        self.play(Create(graph_after1, run_time=0.75), Write(u, run_time=1))
        self.wait(2)

        v_label = MathTex("v", color=GREEN)
        v_label.to_edge(RIGHT)
        v_label.shift(DOWN * 2 + LEFT * 3)

        c_label = MathTex("c", color=GREEN)
        c_label.next_to(v_label, RIGHT)
        c_label.shift(RIGHT * 1.5 + DOWN * 0.1 + 0.05)

        # it's used v = beta (c) because v is set to 1 and c is set to 3, thus beta corresponds to the ratio 
        on_screen_var = Variable(beta, v_label, num_decimal_places=2)
        on_screen_var.set_color(GREEN)
        
        self.play(Write(on_screen_var, run_time=1.2))
        self.play(Write(c_label, run_time=0.5))
        self.wait(2)

        v = 1.35
        beta = v / c

        var_tracker = on_screen_var.tracker

        graph_before2 = self.get_graph(u_func, x_min=-40, x_max=1.05 * - c / beta, y_min=-80, y_max=80, color=GREEN)
        graph_after2 = self.get_graph(u_func, x_min=0.957 * - c / beta, x_max=40, y_min=-80, y_max=80, color=GREEN)

        self.play(var_tracker.animate.set_value(beta), ReplacementTransform(graph_before1, graph_before2), ReplacementTransform(graph_after1, graph_after2))
        self.wait(2)

        v = 0.6
        beta = v / c

        graph_before3 = self.get_graph(u_func, x_min=-40, x_max=1.05 * - c / beta, y_min=-80, y_max=80, color=GREEN)
        graph_after3 = self.get_graph(u_func, x_min=0.955 * - c / beta, x_max=40, y_min=-80, y_max=80, color=GREEN)
        
        var_tracker = on_screen_var.tracker

        self.play(var_tracker.animate.set_value(beta), ReplacementTransform(graph_before2, graph_before3), ReplacementTransform(graph_after2, graph_after3))
        self.wait(2)

        v = 1.8
        beta = v / c

        graph_before4 = self.get_graph(u_func, x_min=-40, x_max=1.05 * - c / beta, y_min=-80, y_max=80, color=GREEN)
        graph_after4 = self.get_graph(u_func, x_min=0.95 * - c / beta, x_max=40, y_min=-80, y_max=80, color=GREEN)
        
        var_tracker = on_screen_var.tracker

        self.play(var_tracker.animate.set_value(beta), ReplacementTransform(graph_before3, graph_before4), ReplacementTransform(graph_after3, graph_after4))
        self.wait(2)

        v = 1.5
        beta = v / c

        graph_before5 = self.get_graph(u_func, x_min=-40, x_max=1.05 * - c / beta, y_min=-80, y_max=80, color=GREEN)
        graph_after5 = self.get_graph(u_func, x_min=0.95 * - c / beta, x_max=40, y_min=-80, y_max=80, color=GREEN)
        
        var_tracker = on_screen_var.tracker

        self.play(var_tracker.animate.set_value(beta), ReplacementTransform(graph_before4, graph_before5), ReplacementTransform(graph_after4, graph_after5))
        self.wait(2)

class HomographicFunction(GraphScene):
    """ Shows the graph of a general homographic function. """
    def construct(self):
        homo = MathTex(r"\mathrm{Funzione\ omografica}", run_time=1.5, color="#96fffc")
        homo.to_edge(UP)

        fgroup = VGroup(
            MathTex(r"y = \frac{ax + b}{cx + d}", color="#96fffc"),
            MathTex(r"(c \neq 0)", color="#96fffc"),
        )
        # the order matters!
        fgroup.next_to(homo, RIGHT)
        fgroup.arrange(RIGHT)
        fgroup.to_edge(UP)
        fgroup.shift(DOWN)

        self.play(Write(homo, run_time=1.5))
        self.play(Write(fgroup, run_time=1.5))
        self.wait(2)

        fgroup_outer = VGroup(
            MathTex(r"y = \frac{ax + b}{cx + d}", color="#96fffc"),
            MathTex(r"(c \neq 0)", color="#96fffc"),
        )
        # the order matters!
        fgroup_outer.arrange(RIGHT)
        fgroup_outer.to_edge(UP)
        fgroup_outer.to_edge(RIGHT)

        self.play(ReplacementTransform(fgroup, fgroup_outer, run_time=1.5))
        self.wait(2)

        self.x_axis_label = "$x$"
        self.y_axis_label = "$y$"
        self.x_min = -5
        self.x_max = 5
        self.y_min = -10
        self.y_max = 10
        self.graph_origin = ORIGIN + LEFT * 2.2 + DOWN * 0.7
        self.x_axis_config = { "tick_frequency": 1 }
        self.y_axis_config = { "tick_frequency": 2 }

        self.setup_axes(animate=True)
        
        hfunc = lambda x: 1 / x

        graph_1 = self.get_graph(hfunc, x_min=-5, x_max=-0.1, y_min=-0.5, y_max=0.5, color = "#96fffc")
        graph_2 = self.get_graph(hfunc, x_min=0.1, x_max=5, y_min=-0.5, y_max=0.5, color = "#96fffc")
        
        self.play(Create(graph_1), run_time=1)
        self.play(Create(graph_2), run_time=1)
        self.wait(2)

        u_func = MathTex(r"u = \frac{u' + v}{\frac{vu'}{c^2} + 1}", color="#8d88f2")
        u_func.next_to(fgroup_outer, DOWN)
        u_func.shift(DOWN)

        self.play(Write(u_func, run_time=1.5))
        self.wait(2)

        abcd = VGroup(
            MathTex("a", "=", "1"),
            MathTex("b", "=", "v"),
            MathTex("c", "=", "\\frac{v}{c^2}"),
            MathTex("d", "=", "1")
        )
        abcd.arrange(DOWN)
        abcd.next_to(u_func, DOWN)
        abcd.shift(DOWN * 0.5)

        abcd[0][0].set_color("#96fffc")
        abcd[1][0].set_color("#96fffc")
        abcd[2][0].set_color("#96fffc")
        abcd[3][0].set_color("#96fffc")

        abcd[0][2].set_color("#8d88f2")
        abcd[1][2].set_color("#8d88f2")
        abcd[2][2].set_color("#8d88f2")
        abcd[3][2].set_color("#8d88f2")

        self.play(Write(abcd, run_time=1.5))
        self.wait(2)

class StudyU(Scene):
    """ Shows the whole study of the function of the relativistic addition of velocities. """
    def construct(self):
        function = MathTex("u=\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}", color=GREEN)
        self.play(Write(function, run_time=1.5))
        self.wait(2)

        function_upper = MathTex("u=\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}", color=GREEN)
        function_upper.to_edge(UP)
        function_upper.to_edge(LEFT)

        self.play(ReplacementTransform(function, function_upper, run_time=1.5))
        self.wait(2)

        right_stuff = BulletedList(
            "Algebrica",
            "Razionale",
            "Fratta",
            "II grado"
        )
        right_stuff.set_color("#b291db")
        right_stuff.to_edge(RIGHT)
        right_stuff.to_edge(LEFT)
        right_stuff.scale(0.9)

        self.play(Write(right_stuff, run_time=1.5))
        self.wait(2)

        domain = MathTex("\\mathrm{D_u}:\\forall u\' \mid \\frac{u\'v}{c^2}+1 \\neq 0", color="#86e3e0")
        self.play(Write(domain, run_time=1.5))
        self.wait(2)

        domain2 = MathTex("\\mathrm{D_u}:\\forall u\' \mid \\frac{u\'v}{c^2} \\neq -1", color="#86e3e0")
        self.play(FadeTransformPieces(domain, domain2, run_time=1.5))
        self.wait(2)

        domain3 = MathTex("\\mathrm{D_u}:\\forall u\' \mid u\'v \\neq -c^2", color="#86e3e0")
        self.play(FadeTransformPieces(domain2, domain3, run_time=1.5))
        self.wait(2)

        domain4 = MathTex("\\mathrm{D_u}:\\forall u\' \mid u\' \\neq - \\frac{c^2}{v}", color="#86e3e0")
        self.play(FadeTransformPieces(domain3, domain4, run_time=1.5))
        self.wait(2)

        domain_new = MathTex("\\mathrm{D_u}:\\forall u\' \mid u\' \\neq - \\frac{c^2}{v}", color="#86e3e0")
        domain_new.to_edge(UP)

        self.play(FadeTransformPieces(domain4, domain_new, run_time=1.5))
        self.wait(2)

        systems = VGroup(
            MathTex(r"""
\begin{cases}
    u' = 0 \\
    u = \frac{0+v}{0+1} 
\end{cases}
        """, color="#dbeda4"),
            MathTex(r"""
\begin{cases}
    u = 0 \\
    0 = u'+v
\end{cases}
        """, color="#dbeda4")
        )
        systems.arrange(RIGHT)

        # note: there is a tripe indexing!
        set_color(systems[0], 0, [4, 7, 11], RED)
        set_color(systems[1], 0, [3, 4], RED)

        self.play(Write(systems, run_time=1.5))
        self.wait(2)

        systems2 = VGroup(
            MathTex(r"""
\begin{cases}
    u' = 0 \\
    u = v
\end{cases}
        """, color="#dbeda4"),
            MathTex(r"""
\begin{cases}
    u = 0 \\
    u' = -v
\end{cases}
        """, color="#dbeda4")
        )
        systems2.arrange(RIGHT)

        self.play(ReplacementTransform(systems, systems2, run_time=1.5))
        self.wait(2)

        intersections = VGroup(
            MathTex("(0; v)"),
            MathTex("(-v; 0)")
        )
        intersections.arrange(RIGHT)
        intersections.next_to(systems2, DOWN)
        
        intersections.set_color("#dbeda4")

        self.play(Write(intersections, run_time=1.5))
        self.wait(2)

        intersections_upper = VGroup(
            MathTex("(0; v)"),
            MathTex("(-v; 0)")
        )
        intersections_upper.arrange(RIGHT)
        intersections_upper.to_edge(UP)
        intersections_upper.to_edge(RIGHT)

        intersections_upper.set_color("#dbeda4")

        self.play(Unwrite(systems2, run_time=0.7), ReplacementTransform(intersections, intersections_upper, run_time=1.5))
        self.wait(2)

        original = MathTex("\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}>0", color="#e35235")
        self.play(Write(original, run_time=1.5))
        self.wait(2)

        self.play(Unwrite(original, run_time=0.7))

        num = MathTex(r"u' + v > 0", color="#e35235")
        self.play(Write(num, run_time=1.5))
        self.wait(2)

        num2 = MathTex(r"u' > -v", color="#e35235")
        self.play(FadeTransformPieces(num, num2, run_time=1.5))
        self.wait(2)

        num2_moved = MathTex(r"u' > -v", color="#e35235")
        num2_moved.to_edge(RIGHT)

        self.play(ReplacementTransform(num2, num2_moved, run_time=1.5))
        self.wait(2)

        den = MathTex(r"\frac{u'v}{c^2} + 1 > 0", color="#e35235")
        self.play(Write(den, run_time=1.5))
        self.wait(2)

        den2 = MathTex(r"u' > - \frac{c^2}{v}", color="#e35235")
        self.play(FadeTransformPieces(den, den2, run_time=1.5))
        self.wait(2)

        num_new = MathTex(r"u' > -v", color="#e35235")
        num_new.shift(UP / 2)

        den_new = MathTex(r"u' > - \frac{c^2}{v}", color="#e35235")
        den_new.next_to(num_new, DOWN)

        self.play(ReplacementTransform(num2_moved, num_new, run_time=1.5), ReplacementTransform(den2, den_new, run_time=1.5))
        self.wait(2)

        positive = VGroup(
            MathTex(r"u>0: u'< - \frac{c^2}{v} \vee u'>-v"),
            MathTex(r"u=0: u'=-v"),
            MathTex(r"u<0: - \frac{c^2}{v} <u'<-v")
        )
        positive.arrange(DOWN)
        
        positive.set_color("#e35235")

        self.play(Unwrite(num_new, run_time=0.7), Unwrite(den_new, run_time=0.7))
        
        self.play(Write(positive, run_time=1.5))
        
        self.play(Indicate(positive[0], run_time=0.5, color="#e35235"))
        self.play(Indicate(positive[1], run_time=0.5, color="#e35235"))
        self.play(Indicate(positive[2], run_time=0.5, color="#e35235"))
        self.wait(2)

        # i have a severe naming problem
        positiveness = MathTex(r"u>0: u'< - \frac{c^2}{v} \vee u'>-v", color="#e35235")
        positiveness.to_edge(DOWN)
        positiveness.to_edge(RIGHT)

        self.play(Unwrite(positive, run_time=0.7), Write(positiveness, run_time=1.5))
        self.wait(2)
        

        limit = MathTex("\\lim_{u\' \\rightarrow - \\frac{c^2}{v} } {\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}}", color="#e78c4b")

        rect = SurroundingRectangle(domain_new, color="#e78c4b")
        self.play(Create(rect, run_time=1))
        self.play(Uncreate(rect, run_time=1), Write(limit, run_time=1.5))
        self.wait(2)

        self.play(
            limit[0][11].animate.set_color(BLUE),
            limit[0][12].animate.set_color(BLUE),

            limit[0][16].animate.set_color(BLUE),
            limit[0][17].animate.set_color(BLUE),

        )
        self.wait(2)

        limit2 = MathTex(r"\frac{ - \frac{c^2}{v} + v}{- \frac{c^2v}{vc^2} + 1}", color="#e78c4b")

        set_color(limit2, 0, [0, 1, 2, 3, 4, 8, 9, 10, 13], color=BLUE)

        self.play(FadeTransformPieces(limit, limit2, run_time=1.5))
        self.wait(2)

        self.play(limit2.animate.set_color("#e78c4b"))
        self.wait(2)

        self.play(
            limit2[0][0].animate.set_color(BLUE),
            limit2[0][1].animate.set_color(BLUE),
            limit2[0][2].animate.set_color(BLUE),
            limit2[0][3].animate.set_color(BLUE),
            limit2[0][4].animate.set_color(BLUE),
            limit2[0][5].animate.set_color(BLUE),
            limit2[0][6].animate.set_color(BLUE),

            limit2[0][8].animate.set_color(BLUE),
            limit2[0][9].animate.set_color(BLUE),
            limit2[0][10].animate.set_color(BLUE),
            limit2[0][11].animate.set_color(BLUE),
            limit2[0][12].animate.set_color(BLUE),
            limit2[0][13].animate.set_color(BLUE),
            limit2[0][14].animate.set_color(BLUE),
            limit2[0][15].animate.set_color(BLUE)
        )
        self.wait(2)

        limit3 = MathTex(r"\frac{ \frac{-c^2+v^2}{v}}{-1 + 1}", color="#e78c4b")

        set_color(limit3, 0, [0, 1, 2, 3, 4, 5, 6, 7, 9, 10], BLUE)

        self.play(FadeTransformPieces(limit2, limit3, run_time=1.5))
        self.wait(2)

        self.play(limit3.animate.set_color("#e78c4b"))
        self.wait(2)

        self.play(
            limit3[0][0].animate.set_color(BLUE),
            limit3[0][1].animate.set_color(BLUE),
            limit3[0][2].animate.set_color(BLUE),
            limit3[0][3].animate.set_color(BLUE),
            limit3[0][4].animate.set_color(BLUE),
            limit3[0][5].animate.set_color(BLUE),

            limit3[0][9].animate.set_color(BLUE),
            limit3[0][10].animate.set_color(BLUE),
            limit3[0][11].animate.set_color(BLUE),
            limit3[0][12].animate.set_color(BLUE)
        )
        self.wait(2)

        limit4 = MathTex(r"\frac{v^2-c^2}{0}", color="#e78c4b")

        set_color(limit4, 0, [0, 1, 2, 3, 4, 6], BLUE)

        self.play(FadeTransformPieces(limit3, limit4, run_time=1.5))
        self.wait(2)

        limit6_lower = MathTex(r"\frac{v^2-c^2}{0}", color="#e78c4b")
        limit6_lower.to_edge(RIGHT)
        
        system = MathTex(r"v^2 - c^2 < 0 \mathrm{\ } \forall v", color="#e78c4b")

        self.play(FadeTransformPieces(limit4, limit6_lower, run_time=1.5), Write(system, run_time=1.5))
        self.wait(2)

        system2 = MathTex(r"(v < c \Rightarrow v^2 < c^2 \Rightarrow v^2 - c^2 < 0)", color="#e78c4b")
        system2.next_to(system, DOWN)

        self.play(Write(system2, run_time=1.5))
        self.wait(2)

        results = MathTex("""
\\begin{matrix}
\\\ -: + \infty
\\\ +: - \infty
\\end{matrix}
        """)

        results.set_color("#e78c4b")

        arrow = MathTex("\\Rightarrow", color="#e78c4b")

        results.next_to(arrow)
        
        limit_final = MathTex(r"\frac{v^2-c^2}{0}", color="#e78c4b")
        limit_final.shift(LEFT * 1.3)

        total = VGroup(arrow, results)
        total.next_to(limit_final, RIGHT)

        self.play(Unwrite(system2, run_time=0.7), Unwrite(system, run_time=0.7), ReplacementTransform(limit6_lower, limit_final, run_time=1.5))
        self.wait(2)

        self.play(Write(total, run_time=1.5))
        self.wait(2)

        end = VGroup(
            MathTex(r"u'=- \frac{c^2}{v}"),
            MathTex("\\mathrm{asintoto\\ verticale}")
        )
        end.arrange(DOWN)
        end.set_color("#e78c4b")

        self.play(Unwrite(limit_final, run_time=0.7), Unwrite(total, run_time=0.7))
        self.play(Write(end, run_time=1.5))
        self.wait(2)

        first_limit = MathTex(r"u' = - \frac{c^2}{v}", color="#e78c4b")
        first_limit.to_edge(DOWN)
        first_limit.to_edge(LEFT)

        self.play(ReplacementTransform(end, first_limit, run_time=1.5))
        self.wait(2)

        limith = MathTex(r"\lim_{u' \rightarrow \pm \infty } {\frac{u'+v}{\frac{u'v}{c^2}+1}}", color="#e78c4b")
        self.play(Write(limith, run_time=1.5))
        self.wait(2)

        limith2 = MathTex(r"\lim_{u' \rightarrow \pm \infty } {\frac{u'(1+ \frac{v}{u'})}{u'(\frac{v}{c^2}+\frac{1}{u'})}}", color="#e78c4b")
        self.play(FadeTransformPieces(limith, limith2, run_time=1.5))
        self.wait(2)

        self.play(
            limith2[0][8].animate.set_color(BLUE),
            limith2[0][9].animate.set_color(BLUE),

            limith2[0][19].animate.set_color(BLUE),
            limith2[0][20].animate.set_color(BLUE)
        )
        self.wait(2)

        limith3 = MathTex(r"\lim_{u' \rightarrow \pm \infty } {\frac{1+ \frac{v}{u'}}{\frac{v}{c^2}+\frac{1}{u'}}}", color="#e78c4b")
        self.play(FadeTransformPieces(limith2, limith3, run_time=1.5))
        self.wait(2)

        self.play(
            limith3[0][3].animate.set_color(BLUE),
            limith3[0][4].animate.set_color(BLUE),
            limith3[0][5].animate.set_color(BLUE),
            limith3[0][6].animate.set_color(BLUE),
            limith3[0][7].animate.set_color(BLUE),

            limith3[0][10].animate.set_color(BLUE),
            limith3[0][11].animate.set_color(BLUE),
            limith3[0][12].animate.set_color(BLUE),
            limith3[0][13].animate.set_color(BLUE),

            limith3[0][20].animate.set_color(BLUE),
            limith3[0][21].animate.set_color(BLUE),
            limith3[0][22].animate.set_color(BLUE),
            limith3[0][23].animate.set_color(BLUE)
        )
        self.wait(2)

        limith4 = MathTex(r"\frac{1}{\frac{v}{c^2}}", color="#e78c4b")
        self.play(ReplacementTransform(limith3, limith4, run_time=1.5))
        self.wait(2)

        limith5 = VGroup(
            MathTex(r"u=\frac{c^2}{v}"),
            MathTex("\\mathrm{asintoto\\ orizzontale}")
        )
        limith5.arrange(DOWN)
        limith5.set_color("#e78c4b")

        self.play(Unwrite(limith4, run_time=0.7))
        self.play(Write(limith5, run_time=1.5))
        self.wait(2)

        limith_end = MathTex(r"u=\frac{c^2}{v}", color="#e78c4b")
        limith_end.to_edge(DOWN)
        limith_end.shift(LEFT * 2)

        self.play(ReplacementTransform(limith5, limith_end, run_time=1.5))
        self.wait(2)

class UUPrime2(Scene):
    """ Shows two different reference frames and their relative velocities. """
    def construct(self):
        vech = Vector(direction=RIGHT)
        vech.set_length(3)

        vecv = Vector(direction=UP)
        vecv.set_length(3)
        
        vecv.next_to(vech.get_start(), direction=UP, buff=0) # apparently buff is the distance from the two mobjects

        label = MathTex(r"\mathrm{S}")
        label.next_to(vecv, UP)

        dot = Dot(point=UP)
        dot.shift(RIGHT)

        axes1 = VGroup(vecv, vech, label, dot)
        axes1.scale(0.9)
        
        axes1.move_to(0)
        axes1.shift(LEFT * 1.5)

        axes1[0].set_color("#eba978")
        axes1[1].set_color("#eba978")
        axes1[2].set_color("#eba978")

        self.play(Write(axes1, run_time=1.5))
        self.wait(2)

        u = Vector(direction=RIGHT)
        u.next_to(dot.get_start(), direction=RIGHT, buff=0)

        u_label = MathTex(r"\vec{u}")
        u_label.next_to(u, UP)

        u_thing = VGroup(u, u_label)
        u_thing.set_color("#eba978")

        self.play(Write(u_thing, run_time=1))
        self.wait(2)

        self.play(Unwrite(u_thing, run_time=0.7))
        self.wait(2)

        vech2 = Vector(direction=RIGHT)
        vech2.set_length(3)

        vecv2 = Vector(direction=UP)
        vecv2.set_length(3)
        
        vecv2.next_to(vech2.get_start(), direction=UP, buff=0) # apparently buff is the distance from the two mobjects

        label2 = MathTex(r"\mathrm{S'}")
        label2.next_to(vecv2, UP)

        axes2 = VGroup(vecv2, vech2, label2)
        axes2.scale(0.9)
        
        axes2.move_to(0)
        axes2.shift(UP / 2 + LEFT / 2)

        axes2.set_color("#e65c5c")

        self.play(Write(axes2, run_time=1.5))
        self.wait(2)

        u2 = Vector(direction=RIGHT)
        u2.next_to(dot.get_start(), direction=RIGHT, buff=0)

        u_label2 = MathTex(r"\vec{u'}")
        u_label2.next_to(u2, UP)

        u_thing2 = VGroup(u2, u_label2)
        u_thing2.set_color("#e65c5c")

        self.play(Write(u_thing2, run_time=1))
        self.wait(2)

        self.play(Unwrite(u_thing2, run_time=0.7))
        self.wait(2)

        v_vec = Vector(direction=RIGHT, color=GREEN)
        v_vec.set_length(1)

        v_vec.shift(LEFT * 1.8)

        v_label = MathTex(r"\vec{v}", color=GREEN)
        v_label.next_to(v_vec, UP)

        v = VGroup(v_vec, v_label)

        self.play(Write(v, run_time=1))
        self.wait(2)

        vech3 = Vector(direction=RIGHT)
        vech3.set_length(3)

        vecv3 = Vector(direction=UP)
        vecv3.set_length(3)
        
        vecv3.next_to(vech3.get_start(), direction=UP, buff=0) # apparently buff is the distance from the two mobjects

        label3 = MathTex(r"\mathrm{S'}")
        label3.next_to(vecv3, UP)

        axes3 = VGroup(vecv3, vech3, label3)
        axes3.scale(0.9)
        
        axes3.move_to(0)
        axes3.shift(UP / 2 + RIGHT * 3)

        axes3.set_color("#e65c5c")

        v_vec2 = Vector(direction=RIGHT, color=GREEN)
        v_vec2.set_length(1)

        v_vec2.shift(RIGHT * 1.75)
        
        v_label2 = MathTex(r"\vec{v}", color=GREEN)
        v_label2.next_to(v_vec2, UP)

        v2 = VGroup(v_vec2, v_label2)

        self.play(ReplacementTransform(axes2, axes3, run_time=1.5), ReplacementTransform(v, v2, run_time=1.5))
        self.wait(2)

        title = MathTex(r"\mathrm{Trasformazioni\ di\ Galileo}", color="#99c3e8")
        title.to_edge(UP)

        transformation = MathTex(r"""
\begin{cases}
    x' = x - vt \\
    y' = y \\
    z' = z \\
    t' = t
\end{cases}
        """)
        transformation.set_color("#99c3e8")

        set_color(transformation, 0, [12, 15, 19, 23, 27], "#eba978")
        set_color(transformation, 0, [9, 10, 16, 17, 20, 21, 24, 25], "#e65c5c")
        set_color(transformation, 0, [14], GREEN)

        self.play(Unwrite(axes1, run_time=0.7), Unwrite(axes3, run_time=0.7), Unwrite(v2, run_time=0.7))
        self.wait(2)

        self.play(Write(title, run_time=1.5), Write(transformation, run_time=1.5))
        self.wait(2)

        transformation2 = MathTex(r"""
\begin{cases}
    x' = x - vt \\
    y' = y \\
    z' = z \\
    t' = t
\end{cases}
        """)
        transformation2.set_color("#99c3e8")
        transformation2.shift(LEFT * 4)

        set_color(transformation2, 0, [12, 15, 19, 23, 27], "#eba978")
        set_color(transformation2, 0, [9, 10, 16, 17, 20, 21, 24, 25], "#e65c5c")
        set_color(transformation2, 0, [14], GREEN)

        self.play(ReplacementTransform(transformation, transformation2, run_time=1.5))
        self.wait(2)

        t3 = MathTex(r"u' = u - v")
        t3.set_color("#99c3e8")
        t3.shift(RIGHT * 3)

        set_color(t3, 0, [0, 1], "#e65c5c")
        set_color(t3, 0, [3], "#eba978")
        set_color(t3, 0, [5], GREEN)

        self.play(Write(t3, run_time=1.5))
        self.wait(2)

        t4 = MathTex(r"u' = u - v")
        t4.set_color("#99c3e8")
        t4.shift(RIGHT * 3 + UP * 1.5)

        set_color(t4, 0, [0, 1], "#e65c5c")
        set_color(t4, 0, [3], "#eba978")
        set_color(t4, 0, [5], GREEN)

        ex = VGroup(
            MathTex(r"u=\frac{2}{3}c"),
            MathTex(r"v=-\frac{2}{3}c")
        )
        ex.arrange(DOWN)
        ex.shift(DOWN * 0.5 + LEFT)

        ex[0][0].set_color("#eba978")
        ex[1][0].set_color(GREEN)

        self.play(ReplacementTransform(t3, t4, run_time=1.5))
        self.play(Write(ex, run_time=1.5))
        self.wait(2)

        end = MathTex(r"\Rightarrow", r"u'=\frac{4}{3}c")
        end.next_to(ex, RIGHT)
        
        end[0].set_color("#99c3e8")
        end[1].set_color("#e65c5c")

        self.play(Write(end, run_time=1.5))
        self.wait(2)

        imp = VGroup(
            MathTex(r"u' > c"),
            MathTex(r"\mathrm{Impossibile}")
        )
        imp.arrange(DOWN)
        imp.next_to(end, RIGHT)
        imp.shift(RIGHT)
        
        imp.set_color("#f2aa00")

        self.play(Write(imp, run_time=1.5))
        self.wait(2)

        axiom = MathTex(r"\mathrm{Secondo\ assioma\ della\ relativit}", r"\mathrm{\grave a}", r"\mathrm{\ ristretta}", color="#f2aa00")
        axiom.to_edge(DOWN)

        self.play(Write(axiom, run_time=1.5))
        self.wait(2)

class Question(Scene):
    """ Shows the problem at the beginning of the presentation. """
    def construct(self):
        q = MathTex(r"u \leftrightarrow u'", color=GREEN)

        mark = MathTex(r"?", color=YELLOW)
        mark.scale(1.4)

        g = VGroup(q, mark)
        g.arrange(DOWN)

        self.play(Write(g, run_time=1.5))
        self.wait(2)

        self.play(Unwrite(g, run_time=0.7))
        self.wait(2)

class Einstein(Scene):
    """ Shows the two axioms of the special relativity. """
    def construct(self):
        axioms = BulletedList(
            "Le leggi della fisica sono le stesse in tutti i sistemi di riferimento inerziali",
            "La luce si propaga nel vuoto a velocità costante c, indipendentemente dallo stato di moto della sorgente o dell’osservatore"
        )
        axioms.scale(0.7)

        self.play(Write(axioms, run_time=2.5))
        self.wait(5)

        self.play(Unwrite(axioms, run_time=2.5))
        self.wait(2)

        text3 = MathTex("u\'-\\frac{uu\'v}{c^2}=u-v")
        self.play(ReplacementTransform(text2, text3, run_time=1.5))
        self.wait(2)

        text4 = MathTex("\\frac{uu\'v}{c^2}-u'=v-u")
        self.play(ReplacementTransform(text3, text4, run_time=1.5))
        self.wait(2)

        text5 = MathTex("u(\\frac{u\'v}{c^2}+1)=u\'+v")
        self.play(ReplacementTransform(text4, text5, run_time=1.5))
        self.wait(2)

        text6 = MathTex("u=\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}")
        self.play(ReplacementTransform(text5, text6, run_time=1.5))
        self.wait(2)

class CSubstitution(Scene):
    """ Shows the invariance of `c`. """
    def construct(self):
        text1 = MathTex("u\'=\\frac{u-v}{1-\\frac{uv}{c^2}}")
        self.play(Write(text1, run_time=1.5))
        self.wait(2)

        ueqc = MathTex("u=c", color=RED)
        ueqc.to_edge(UP)
        ueqc.shift(DOWN * 0.6)

        self.play(Write(ueqc, run_time=1))
        self.wait(0.7)

        self.play(
            text1[0][3].animate.set_color(RED),
            text1[0][9].animate.set_color(RED)
        )
        self.wait(2)

        text2 = MathTex("u\'=\\frac{c-v}{1-\\frac{cv}{c^2}}")
        self.play(ReplacementTransform(text1, text2, run_time=1.5))
        self.wait(2)

        self.play(
            text2[0][9].animate.set_color(RED),
            text2[0][13].animate.set_color(RED),
        )
        self.wait(2)

        text3 = MathTex("u\'=\\frac{c-v}{1-\\frac{v}{c}}")
        self.play(FadeTransformPieces(text2, text3, run_time=1.5))
        self.wait(2)

        self.play(
            text3[0][7].animate.set_color(RED),
            text3[0][8].animate.set_color(RED),
            text3[0][9].animate.set_color(RED),
            text3[0][10].animate.set_color(RED),
            text3[0][11].animate.set_color(RED)
        )
        self.wait(2)

        text4 = MathTex("u\'=\\frac{c-v}{\\frac{c-v}{c}}")
        self.play(ReplacementTransform(text3, text4, run_time=1.5))
        self.wait(2)

        self.play(
            text4[0][10].animate.set_color(RED),
            text4[0][11].animate.set_color(RED)
        )
        self.wait(2)

        text5 = MathTex("u\'=\\frac{c-v}{c-v}c")
        self.play(FadeTransformPieces(text4, text5, run_time=1.5))
        self.wait(2)
        
        self.play(
            text5[0][3].animate.set_color(RED),
            text5[0][4].animate.set_color(RED),
            text5[0][5].animate.set_color(RED),
            text5[0][6].animate.set_color(RED),
            text5[0][7].animate.set_color(RED),
            text5[0][8].animate.set_color(RED),
            text5[0][9].animate.set_color(RED)
        )
        self.wait(2)

        text6 = MathTex("u\'=c")
        self.play(FadeTransformPieces(text5, text6, run_time=1.5))
        self.wait(0.8)

        last = MathTex(r"\mathrm{Invarianza\ della\ velocit}", r"\mathrm{\grave a}", r"\ \mathrm{della\ luce}", color=RED)
        last.next_to(text6, UP)

        lower_upper = MathTex("u=c", color=RED)
        lower_upper.next_to(text6, DOWN)

        self.play(Indicate(text6, color=RED), Write(last, run_time=1.5), ReplacementTransform(ueqc, lower_upper, run_time=1.5))
        self.wait(2)

class VerySmallSpeed(Scene):
    """ Shows how to derive the Galilean transformation. """
    def construct(self):
        upper_text = MathTex("u\'=\\frac{u-v}{1-\\frac{uv}{c^2}}")        

        group = VGroup(
            MathTex("\mathrm{Se\\ }"),
            MathTex("u<<c"),
            MathTex("\mathrm{\\ e\\ }"),
            MathTex("v<<c"),
            MathTex("\mathrm{,\\ allora}")
        )
        # the order matters!
        group.arrange(RIGHT)
        group.to_edge(UP)

        self.play(Write(upper_text, run_time=1.5))
        self.wait(2)

        lower_text = MathTex("u\'=\\frac{u-v}{1-\\frac{uv}{c^2}}") 
        lower_text.to_edge(DOWN)

        self.play(
            upper_text[0][9].animate.set_color(BLUE),
            upper_text[0][10].animate.set_color(BLUE)
        )
        self.wait(2)

        set_color(lower_text, 0, [9, 10], BLUE)

        self.play(FadeTransform(upper_text, lower_text, run_time=1.5))
        self.play(Write(group, run_time=1))

        self.play(Indicate(group[1], color=BLUE))
        self.play(Indicate(group[3], color=BLUE))
        self.wait(2)

        approx1 = MathTex("u\'\\approx\\frac{u-v}{1-0}")

        approx1[0][-1].set_color(BLUE)

        self.play(Write(approx1, run_time=1.5))
        self.wait(2)

        approx2 = MathTex("u\'\\approx u-v")
        self.play(FadeTransformPieces(approx1, approx2, run_time=1.5))
        self.wait(2)

        text = MathTex("\mathrm{Trasformazione\\ di\\ Galileo}", color=BLUE)
        text.next_to(approx2, UP)
        self.play(Write(text, run_time=1.5), Indicate(approx2, color=BLUE))
        self.wait(2)

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
        self.wait(2)

        text2 = MathTex("u\'=\\frac{\\Delta x\'}{\\Delta t\'}=\\frac{x_2\'-x_1\'}{t_2\'-t_1\'}")
        text2.to_edge(UP)
        self.play(FadeTransform(text1, text2, run_time=1.5))
        self.wait(2)

class Demonstration2(Scene): # this scene is a mess!
    """ Shows the second part of the demonstration of the relativity addition formula. """
    def construct(self):
        group = VGroup(
            MathTex("\mathrm{Per\\ }"),
            MathTex("x=x\'=0 \mathrm{m}"),
            MathTex("\mathrm{\\ e\\ }"),
            MathTex("t=t\'=0 \mathrm{s}"),
            MathTex("\mathrm{\\ :}")
        )
        # the order matters!
        group.arrange(RIGHT)
        group.to_edge(UP)

        self.play(Write(group, run_time=1.5))
        self.play(Indicate(group[1], color="#7cbf00"))
        self.play(Indicate(group[3], color="#7cbf00"))
        self.wait(2)

        system = MathTex(r"""
\begin{cases}
    x' = \gamma(x-vt) \\
    y' = y \\
    z' = z \\
    t'\, = \gamma \left(t-\frac{vx}{c^2}\right)
\end{cases}
        """)
        self.play(Write(system, run_time=1.5))
        self.wait(2)

        lower_text = VGroup(
            MathTex(r"x'= \gamma (x-vt)", color="#e3af7f"),
            MathTex(r"t'= \gamma (t-\frac{vx}{c^2})", color="#e3af7f")
        )
        lower_text.arrange(DOWN)
        lower_text.to_edge(DOWN)
        lower_text.to_edge(RIGHT)

        rect1 = Rectangle(color="#e3af7f", height=0.6, width=3.1)
        rect2 = Rectangle(color="#e3af7f", height=0.7, width=3.2)
        rect1.shift(UP * 1.1 + RIGHT * 0.1) # upper
        rect2.shift(DOWN * 1.05 + RIGHT * 0.2) # lower

        self.play(Create(rect1, run_time=1.5), Create(rect2, run_time=1.5), Write(lower_text, run_time=1.5))
        self.play(Uncreate(rect1), Uncreate(rect2))
        self.wait(2)

        self.play(Unwrite(system, run_time=1.5))
        self.wait(2)

        forgot = MathTex(r"\frac{\Delta x'}{\Delta t'} = \frac{x_2' - x_1'}{t_2' - t_1'}")

        set_color(forgot, 0, [8, 9, 10, 12, 13, 14, 16, 17, 18, 20, 21, 22], "#e3af7f")

        self.play(Write(forgot, run_time=1.5))
        self.wait(2)
        
        formula3 = MathTex("\\frac{\\Delta x\'}{\\Delta t\'}=\\frac{\\gamma (x_2-vt_2)- \\gamma (x_1-vt_1)}{\\gamma (t_2-\\frac{vx_2}{c^2})- \\gamma (t_1-\\frac{vx_1}{c^2})}")

        set_color(formula3, 0, [8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], "#e3af7f")

        self.play(FadeTransformPieces(forgot, formula3, run_time=1.5))
        self.wait(2)

        self.play(formula3[0].animate.set_color(WHITE))
        self.wait(2)

        self.play(
            formula3[0][8].animate.set_color("#7cbf00"),
            formula3[0][18].animate.set_color("#7cbf00"),
            formula3[0][28].animate.set_color("#7cbf00"),
            formula3[0][41].animate.set_color("#7cbf00")
        )
        self.wait(2)

        no_gammas = MathTex("\\frac{\\Delta x\'}{\\Delta t\'}=\\frac{(x_2-vt_2)-(x_1-vt_1)}{(t_2-\\frac{vx_2}{c^2})-(t_1-\\frac{vx_1}{c^2})}")
        self.play(FadeTransform(formula3, no_gammas, run_time=1.5))
        self.wait(2)

        forgot3 = MathTex("\\frac{\\Delta x\'}{\\Delta t\'}=\\frac{x_2-vt_2-x_1+vt_1}{t_2-\\frac{vx_2}{c^2}-t_1+\\frac{vx_1}{c^2}}")

        self.play(FadeTransform(no_gammas, forgot3, run_time=1.5))
        self.wait(2)

        forgot2 = MathTex(r"u'= \frac{\Delta x'}{\Delta t'}", color="#64bd90")
        forgot2.to_edge(LEFT)
        forgot2.to_edge(DOWN)

        self.play(Write(forgot2, run_time=1.5))
        self.wait(2)

        self.play(
            forgot3[0][0].animate.set_color("#64bd90"),
            forgot3[0][1].animate.set_color("#64bd90"),
            forgot3[0][2].animate.set_color("#64bd90"),
            forgot3[0][3].animate.set_color("#64bd90"),
            forgot3[0][4].animate.set_color("#64bd90"),
            forgot3[0][5].animate.set_color("#64bd90"),
            forgot3[0][6].animate.set_color("#64bd90")
        )
        self.wait(2)

        formula4 = MathTex("u\'=\\frac{x_2-vt_2-x_1+vt_1}{t_2-\\frac{vx_2}{c^2}-t_1+\\frac{vx_1}{c^2}}")

        set_color(formula4, 0, [0, 1], "#64bd90")

        self.play(FadeTransform(forgot3, formula4, run_time=1.5))
        self.wait(2)

        self.play(
            Unwrite((forgot2), run_time=0.7),

            formula4[0][0].animate.set_color(WHITE),
            formula4[0][1].animate.set_color(WHITE),
            formula4[0][3].animate.set_color("#ff8e2b"),
            formula4[0][4].animate.set_color("#ff8e2b"),

            formula4[0][5].animate.set_color("#c29cff"),
            formula4[0][6].animate.set_color("#c29cff"),
            formula4[0][7].animate.set_color("#c29cff"),
            formula4[0][8].animate.set_color("#c29cff"),

            formula4[0][9].animate.set_color("#ff8e2b"),
            formula4[0][10].animate.set_color("#ff8e2b"),
            formula4[0][11].animate.set_color("#ff8e2b"),

            formula4[0][12].animate.set_color("#c29cff"),
            formula4[0][13].animate.set_color("#c29cff"),
            formula4[0][14].animate.set_color("#c29cff"),
            formula4[0][15].animate.set_color("#c29cff"),
            formula4[0][17].animate.set_color("#c29cff"),
            formula4[0][18].animate.set_color("#c29cff"),

            formula4[0][19].animate.set_color("#ff8e2b"),
            formula4[0][20].animate.set_color("#ff8e2b"),
            formula4[0][21].animate.set_color("#ff8e2b"),
            formula4[0][22].animate.set_color("#ff8e2b"),
            formula4[0][23].animate.set_color("#ff8e2b"),
            formula4[0][24].animate.set_color("#ff8e2b"),
            formula4[0][25].animate.set_color("#ff8e2b"),

            formula4[0][26].animate.set_color("#c29cff"),
            formula4[0][27].animate.set_color("#c29cff"),
            formula4[0][28].animate.set_color("#c29cff"),

            formula4[0][29].animate.set_color("#ff8e2b"),
            formula4[0][30].animate.set_color("#ff8e2b"),
            formula4[0][31].animate.set_color("#ff8e2b"),
            formula4[0][32].animate.set_color("#ff8e2b"),
            formula4[0][33].animate.set_color("#ff8e2b"),
            formula4[0][34].animate.set_color("#ff8e2b"),
            formula4[0][35].animate.set_color("#ff8e2b")
        )
        self.wait(2)

        formula5 = MathTex("u\'=\\frac{(x_2-x_1)-v(t_2-t_1)}{(t_2-t_1)-\\frac{v}{c^2}(x_2-x_1)")

        set_color(formula5, 0, [3, 4, 5, 6, 7, 8, 9], "#ff8e2b")

        set_color(formula5, 0, [10, 11, 12, 13, 14, 15, 16, 17, 18], "#c29cff")

        set_color(formula5, 0, [20, 21, 22, 23, 24, 25, 26], "#c29cff")

        set_color(formula5, 0, [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38], "#ff8e2b")

        self.play(FadeTransform(formula4, formula5, run_time=1.5))
        self.wait(2)

        self.play(formula5[0].animate.set_color(WHITE))
        self.wait(2)
        
        missing = MathTex(r"x = ut \Rightarrow \Delta x = u \Delta t", color="#7cbf00")
        missing.next_to(formula5, UP)

        self.play(
            Write(missing, run_time=1.5),

            formula5[0][3].animate.set_color("#7cbf00"),
            formula5[0][4].animate.set_color("#7cbf00"),
            formula5[0][5].animate.set_color("#7cbf00"),
            formula5[0][6].animate.set_color("#7cbf00"),
            formula5[0][7].animate.set_color("#7cbf00"),
            formula5[0][8].animate.set_color("#7cbf00"),
            formula5[0][9].animate.set_color("#7cbf00"),

            formula5[0][32].animate.set_color("#7cbf00"),
            formula5[0][33].animate.set_color("#7cbf00"),
            formula5[0][34].animate.set_color("#7cbf00"),
            formula5[0][35].animate.set_color("#7cbf00"),
            formula5[0][36].animate.set_color("#7cbf00"),
            formula5[0][37].animate.set_color("#7cbf00"),
            formula5[0][38].animate.set_color("#7cbf00"),
        )
        self.wait(2)

        formula6 = MathTex("u\'=\\frac{u(t_2-t_1)-v(t_2-t_1)}{(t_2-t_1)-\\frac{uv}{c^2}(t_2-t_1)")

        set_color(formula6, 0, [3, 4, 5, 6, 7, 8, 9, 10], "#7cbf00")
        
        set_color(formula6, 0, [29, 34, 35, 36, 37, 38, 39, 40], "#7cbf00")

        self.play(FadeTransform(formula5, formula6, run_time=1.5))
        self.wait(2)

        self.play(formula6[0].animate.set_color(WHITE), Unwrite(missing, run_time=0.7))
        self.wait(2)

        self.play(
            formula6[0][4].animate.set_color("#7cbf00"),
            formula6[0][5].animate.set_color("#7cbf00"),
            formula6[0][6].animate.set_color("#7cbf00"),
            formula6[0][7].animate.set_color("#7cbf00"),
            formula6[0][8].animate.set_color("#7cbf00"),
            formula6[0][9].animate.set_color("#7cbf00"),
            formula6[0][10].animate.set_color("#7cbf00"),

            formula6[0][13].animate.set_color("#7cbf00"),
            formula6[0][14].animate.set_color("#7cbf00"),
            formula6[0][15].animate.set_color("#7cbf00"),
            formula6[0][16].animate.set_color("#7cbf00"),
            formula6[0][17].animate.set_color("#7cbf00"),
            formula6[0][18].animate.set_color("#7cbf00"),
            formula6[0][19].animate.set_color("#7cbf00"),

            formula6[0][21].animate.set_color("#7cbf00"),
            formula6[0][22].animate.set_color("#7cbf00"),
            formula6[0][23].animate.set_color("#7cbf00"),
            formula6[0][24].animate.set_color("#7cbf00"),
            formula6[0][25].animate.set_color("#7cbf00"),
            formula6[0][26].animate.set_color("#7cbf00"),
            formula6[0][27].animate.set_color("#7cbf00"),
            
            formula6[0][34].animate.set_color("#7cbf00"),
            formula6[0][35].animate.set_color("#7cbf00"),
            formula6[0][36].animate.set_color("#7cbf00"),
            formula6[0][37].animate.set_color("#7cbf00"),
            formula6[0][38].animate.set_color("#7cbf00"),
            formula6[0][39].animate.set_color("#7cbf00"),
            formula6[0][40].animate.set_color("#7cbf00")
        )
        self.wait(2)

        formula7 = MathTex("u\'=\\frac{(t_2-t_1)(u-v)}{(t_2-t_1)(1-\\frac{uv}{c^2})")

        set_color(formula7, 0, [3, 4, 5, 6, 7, 8, 9, 16, 17, 18, 19, 20, 21, 22], "#7cbf00")

        self.play(ReplacementTransform(formula6, formula7, run_time=1.5))
        self.wait(2)

        formula8 = MathTex("u\'=\\frac{u-v}{1-\\frac{uv}{c^2}")
        self.play(FadeTransformPieces(formula7, formula8, run_time=1.5))
        self.wait(2)

        self.play(Indicate(formula8, color="#7cbf00"))
        self.wait(2)

class Derivative(Scene):
    """ Shows how to calculate the derivative of the function of the relativistic addiotion of velocities. """
    def construct(self):
        center = MathTex("\\frac{d}{du\'} u = \\frac{d}{du\'} \\frac{u\'+v}{\\frac{u\'v}{c^2}+1}")

        upper_text = MathTex("u=\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}")
        self.play(Write(upper_text, run_time=1.5))
        self.wait(2)

        lower_text = MathTex("u=\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}")
        lower_text.to_edge(UP)

        self.play(FadeTransform(upper_text, lower_text, run_time=1.5), Write(center, run_time=1.5))
        self.wait(2)

        center2 = MathTex(r"\frac{d}{du'} u = \frac{ (1+ \frac{u' v}{c^2} ) - (u'+v) \frac{v}{c^2} } {(1+ \frac{u' v} {c^2})^2}")
        self.play(ReplacementTransform(center, center2, run_time=1.5))
        self.wait(2)

        center3 = MathTex(r"\frac{d}{du'} u = \frac{ 1+ \frac{u' v}{c^2} - \frac{u'v}{c^2} - \frac{v^2}{c^2} } {(1+ \frac{u' v} {c^2})^2}")
        self.play(FadeTransform(center2, center3, run_time=1.5))
        self.wait(2)

        center4 = MathTex(r"\frac{d}{du'} u = \frac{ 1 - \beta^2 } {(1+ \frac{\beta}{c} u')^2}")
        self.play(ReplacementTransform(center3, center4, run_time=1.5))
        self.wait(2)

class StudyDerivative(GraphScene):
    """ Studies the graph of the derivative of the function of the relativistic addition of velocities, and then shows it. """
    def construct(self):
        segno = MathTex(r"\frac{d}{du'} u = \frac{1 - \beta^2}{(1 + \frac{\beta}{c} u')^2}", color=GREEN)
        segno.to_edge(UP)

        self.play(Write(segno, run_time=1.5))
        self.wait(2)

        domain = MathTex(r"\mathrm{D_{u } } : \forall u' \mid u' \neq - \frac{c}{\beta}", color="#f2aa00")
        domain.to_edge(UP)
        domain.to_edge(RIGHT)
        domain.shift(DOWN * 0.2)

        self.play(Write(domain, run_time=1.5))
        
        segno2 = MathTex(r"\mathrm{Numeratore:\ } 1 - \beta^2", color="#ddccaa")
        self.play(Write(segno2, run_time=1.5))
        self.wait(2)

        self.play(Unwrite(segno2, run_time=0.6))

        segno3 = MathTex(r"1 - \beta^2 > 0", color="#ddccaa")
        self.play(Write(segno3, run_time=1.5))
        self.wait(2)

        segno4 = MathTex(r"\beta^2 < 1", color="#ddccaa")
        self.play(FadeTransformPieces(segno3, segno4, run_time=1.5))
        self.wait(2)

        segno5 = MathTex(r"-1 < \beta < 1", color="#ddccaa")
        self.play(FadeTransformPieces(segno4, segno5, run_time=1.5))
        self.wait(2)

        segno6 = MathTex(r"-1 < \frac{v}{c} < 1", color="#ddccaa")
        self.play(FadeTransformPieces(segno5, segno6, run_time=1.5))
        self.wait(2)

        segno7 = MathTex(r"-c < v < c", color="#ddccaa")
        self.play(FadeTransformPieces(segno6, segno7, run_time=1.5))
        self.wait(2)

        segno8 = MathTex(r"\Rightarrow 1 - \beta^2 > 0 \ \forall v", color="#ddccaa")
        segno8.next_to(segno7, DOWN)

        self.play(Write(segno8, run_time=1.5))
        self.wait(2)

        self.play(Unwrite(segno7, run_time=0.6), Unwrite(segno8, run_time=0.6))
        self.wait(2)

        den = MathTex(r"\mathrm{Denominatore:\ } (1 + \frac{\beta}{c} u')^2", color="#babaff")

        self.play(Write(den, run_time=1.5))
        self.wait(2)

        self.play(Unwrite(den, run_time=0.6))

        den2 = MathTex(r"(1 + \frac{\beta}{c} u')^2 > 0", color="#babaff")
        self.play(Write(den2, run_time=1.5))
        self.wait(2)

        den3 = MathTex(r"\forall u' \mid 1 + \frac{\beta}{c} u' \neq 0", color="#babaff")
        den3.next_to(den2, DOWN)

        self.play(Write(den3, run_time=1.5))
        self.wait(2)

        den4 = MathTex(r"u' \neq - \frac{c}{ \beta}", color="#babaff")
        self.play(Unwrite(den2, run_time=0.7), ReplacementTransform(den3, den4, run_time=1.5))
        self.wait(2)

        den5 = MathTex(r"u' = - \frac{c}{\beta} \notin \mathrm{D_{u}}", color="#f2aa00")
        den5.next_to(den5, DOWN)

        self.play(Write(den5, run_time=1.5))
        self.wait(2)

        rect = Rectangle(color="#f2aa00", height=2.0, width=4.5)
        rect.to_edge(UP)
        rect.to_edge(RIGHT)
        rect.shift(RIGHT * 0.25 + UP * 0.35)

        self.play(Create(rect))
        self.play(Uncreate(rect))

        den6 = MathTex(r"u' = - \frac{c}{ \beta}", color="#babaff")
        den6.to_edge(RIGHT)

        self.play(FadeTransform(den4, den6), Unwrite(den5))

        self.x_axis_label = "$u\'$"
        self.y_axis_label = "$u$"
        self.x_min = -20
        self.x_max = 20
        self.y_min = -2
        self.y_max = 12
        self.graph_origin = ORIGIN + 3 * DOWN + 1.5 * LEFT
        self.x_axis_config = { "tick_frequency": 5 }
        self.y_axis_config = { "tick_frequency": 2 }

        self.setup_axes(animate=True)

        v = 1
        c = 3

        beta = v / c
        n = 1 - beta ** 2

        derivative = lambda x: n / (1 + beta * x / c) ** 2

        graph_before = self.get_graph(derivative, x_min=-20, x_max=1.1 * - c / beta, y_min=-5, y_max=20, color=GREEN)
        graph_after = self.get_graph(derivative, x_min=0.9 * - c / beta, x_max=20, y_min=-5, y_max=20, color=GREEN)

        asymptote = self.get_vertical_line_to_graph(1.001 * -c / beta, graph_before, color="#babaff")

        self.play(Create(graph_before, run_time=0.75))
        self.play(Create(graph_after, run_time=0.75))
        self.wait(2)

        self.play(Create(asymptote, run_time=1))
        self.wait(2)

class UGraph(GraphScene):
    """ Shows the change of v in the function of the relativistic addition of velocities. """
    def construct(self):
        self.x_axis_label = "$u\'$"
        self.y_axis_label = "$u$"
        self.x_min = -40
        self.x_max = 40
        self.y_min = -40
        self.y_max = 40
        self.graph_origin = ORIGIN
        self.x_axis_config = { "tick_frequency": 10 }
        self.y_axis_config = { "tick_frequency": 10 }

        self.setup_axes(animate=True)

        v = 1
        c = 3

        beta = v / c

        u_func = lambda x: (x + v) / (1 + (x * v) / c ** 2)

        u = MathTex(r"u = \frac{u'+v}{1+\frac{u'v}{c^2}}", color=GREEN)
        u.to_edge(UP)
        u.to_edge(RIGHT)

        graph_before1 = self.get_graph(u_func, x_min=-40, x_max=1.1 * - c / beta, y_min=-40, y_max=40, color=GREEN)
        graph_after1 = self.get_graph(u_func, x_min=0.9 * - c / beta, x_max=40, y_min=-40, y_max=40, color=GREEN)

        self.play(Create(graph_before1, run_time=0.75))
        self.play(Create(graph_after1, run_time=0.75), Write(u, run_time=1))
        self.wait(2)

        v_label = MathTex("v", color=GREEN)
        v_label.to_edge(RIGHT)
        v_label.shift(DOWN * 2 + LEFT * 3)

        c_label = MathTex("c", color=GREEN)
        c_label.next_to(v_label, RIGHT)
        c_label.shift(RIGHT * 1.5 + DOWN * 0.1 + 0.05)

        # it's used v = beta (c) because v is set to 1 and c is set to 3, thus beta corresponds to the ratio 
        on_screen_var = Variable(beta, v_label, num_decimal_places=2)
        on_screen_var.set_color(GREEN)
        
        self.play(Write(on_screen_var, run_time=1.2))
        self.play(Write(c_label, run_time=0.5))
        self.wait(2)

        v = 1.35
        beta = v / c

        var_tracker = on_screen_var.tracker

        graph_before2 = self.get_graph(u_func, x_min=-40, x_max=1.05 * - c / beta, y_min=-80, y_max=80, color=GREEN)
        graph_after2 = self.get_graph(u_func, x_min=0.957 * - c / beta, x_max=40, y_min=-80, y_max=80, color=GREEN)

        self.play(var_tracker.animate.set_value(beta), ReplacementTransform(graph_before1, graph_before2), ReplacementTransform(graph_after1, graph_after2))
        self.wait(2)

        v = 0.6
        beta = v / c

        graph_before3 = self.get_graph(u_func, x_min=-40, x_max=1.05 * - c / beta, y_min=-80, y_max=80, color=GREEN)
        graph_after3 = self.get_graph(u_func, x_min=0.955 * - c / beta, x_max=40, y_min=-80, y_max=80, color=GREEN)
        
        var_tracker = on_screen_var.tracker

        self.play(var_tracker.animate.set_value(beta), ReplacementTransform(graph_before2, graph_before3), ReplacementTransform(graph_after2, graph_after3))
        self.wait(2)

        v = 1.8
        beta = v / c

        graph_before4 = self.get_graph(u_func, x_min=-40, x_max=1.05 * - c / beta, y_min=-80, y_max=80, color=GREEN)
        graph_after4 = self.get_graph(u_func, x_min=0.95 * - c / beta, x_max=40, y_min=-80, y_max=80, color=GREEN)
        
        var_tracker = on_screen_var.tracker

        self.play(var_tracker.animate.set_value(beta), ReplacementTransform(graph_before3, graph_before4), ReplacementTransform(graph_after3, graph_after4))
        self.wait(2)

        v = 1.5
        beta = v / c

        graph_before5 = self.get_graph(u_func, x_min=-40, x_max=1.05 * - c / beta, y_min=-80, y_max=80, color=GREEN)
        graph_after5 = self.get_graph(u_func, x_min=0.95 * - c / beta, x_max=40, y_min=-80, y_max=80, color=GREEN)
        
        var_tracker = on_screen_var.tracker

        self.play(var_tracker.animate.set_value(beta), ReplacementTransform(graph_before4, graph_before5), ReplacementTransform(graph_after4, graph_after5))
        self.wait(2)

class HomographicFunction(GraphScene):
    """ Shows the graph of a general homographic function. """
    def construct(self):
        homo = MathTex(r"\mathrm{Funzione\ omografica}", run_time=1.5, color="#96fffc")
        homo.to_edge(UP)

        fgroup = VGroup(
            MathTex(r"y = \frac{ax + b}{cx + d}", color="#96fffc"),
            MathTex(r"(c \neq 0)", color="#96fffc"),
        )
        # the order matters!
        fgroup.next_to(homo, RIGHT)
        fgroup.arrange(RIGHT)
        fgroup.to_edge(UP)
        fgroup.shift(DOWN)

        self.play(Write(homo, run_time=1.5))
        self.play(Write(fgroup, run_time=1.5))
        self.wait(2)

        fgroup_outer = VGroup(
            MathTex(r"y = \frac{ax + b}{cx + d}", color="#96fffc"),
            MathTex(r"(c \neq 0)", color="#96fffc"),
        )
        # the order matters!
        fgroup_outer.arrange(RIGHT)
        fgroup_outer.to_edge(UP)
        fgroup_outer.to_edge(RIGHT)

        self.play(ReplacementTransform(fgroup, fgroup_outer, run_time=1.5))
        self.wait(2)

        self.x_axis_label = "$x$"
        self.y_axis_label = "$y$"
        self.x_min = -5
        self.x_max = 5
        self.y_min = -10
        self.y_max = 10
        self.graph_origin = ORIGIN + LEFT * 2.2 + DOWN * 0.7
        self.x_axis_config = { "tick_frequency": 1 }
        self.y_axis_config = { "tick_frequency": 2 }

        self.setup_axes(animate=True)
        
        hfunc = lambda x: 1 / x

        graph_1 = self.get_graph(hfunc, x_min=-5, x_max=-0.1, y_min=-0.5, y_max=0.5, color = "#96fffc")
        graph_2 = self.get_graph(hfunc, x_min=0.1, x_max=5, y_min=-0.5, y_max=0.5, color = "#96fffc")
        
        self.play(Create(graph_1), run_time=1)
        self.play(Create(graph_2), run_time=1)
        self.wait(2)

        u_func = MathTex(r"u = \frac{u' + v}{\frac{vu'}{c^2} + 1}", color="#8d88f2")
        u_func.next_to(fgroup_outer, DOWN)
        u_func.shift(DOWN)

        self.play(Write(u_func, run_time=1.5))
        self.wait(2)

        abcd = VGroup(
            MathTex("a", "=", "1"),
            MathTex("b", "=", "v"),
            MathTex("c", "=", "\\frac{v}{c^2}"),
            MathTex("d", "=", "1")
        )
        abcd.arrange(DOWN)
        abcd.next_to(u_func, DOWN)
        abcd.shift(DOWN * 0.5)

        abcd[0][0].set_color("#96fffc")
        abcd[1][0].set_color("#96fffc")
        abcd[2][0].set_color("#96fffc")
        abcd[3][0].set_color("#96fffc")

        abcd[0][2].set_color("#8d88f2")
        abcd[1][2].set_color("#8d88f2")
        abcd[2][2].set_color("#8d88f2")
        abcd[3][2].set_color("#8d88f2")

        self.play(Write(abcd, run_time=1.5))
        self.wait(2)

class StudyU(Scene):
    """ Shows the whole study of the function of the relativistic addition of velocities. """
    def construct(self):
        function = MathTex("u=\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}", color=GREEN)
        self.play(Write(function, run_time=1.5))
        self.wait(2)

        function_upper = MathTex("u=\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}", color=GREEN)
        function_upper.to_edge(UP)
        function_upper.to_edge(LEFT)

        self.play(ReplacementTransform(function, function_upper, run_time=1.5))
        self.wait(2)

        right_stuff = BulletedList(
            "Algebrica",
            "Razionale",
            "Fratta",
            "II grado"
        )
        right_stuff.set_color("#b291db")
        right_stuff.to_edge(RIGHT)
        right_stuff.to_edge(LEFT)
        right_stuff.scale(0.9)

        self.play(Write(right_stuff, run_time=1.5))
        self.wait(2)

        domain = MathTex("\\mathrm{D_u}:\\forall u\' \mid \\frac{u\'v}{c^2}+1 \\neq 0", color="#86e3e0")
        self.play(Write(domain, run_time=1.5))
        self.wait(2)

        domain2 = MathTex("\\mathrm{D_u}:\\forall u\' \mid \\frac{u\'v}{c^2} \\neq -1", color="#86e3e0")
        self.play(FadeTransformPieces(domain, domain2, run_time=1.5))
        self.wait(2)

        domain3 = MathTex("\\mathrm{D_u}:\\forall u\' \mid u\'v \\neq -c^2", color="#86e3e0")
        self.play(FadeTransformPieces(domain2, domain3, run_time=1.5))
        self.wait(2)

        domain4 = MathTex("\\mathrm{D_u}:\\forall u\' \mid u\' \\neq - \\frac{c^2}{v}", color="#86e3e0")
        self.play(FadeTransformPieces(domain3, domain4, run_time=1.5))
        self.wait(2)

        domain_new = MathTex("\\mathrm{D_u}:\\forall u\' \mid u\' \\neq - \\frac{c^2}{v}", color="#86e3e0")
        domain_new.to_edge(UP)

        self.play(FadeTransformPieces(domain4, domain_new, run_time=1.5))
        self.wait(2)

        systems = VGroup(
            MathTex(r"""
\begin{cases}
    u' = 0 \\
    u = \frac{0+v}{0+1} 
\end{cases}
        """, color="#dbeda4"),
            MathTex(r"""
\begin{cases}
    u = 0 \\
    0 = u'+v
\end{cases}
        """, color="#dbeda4")
        )
        systems.arrange(RIGHT)

        # note: there is a tripe indexing!
        set_color(systems[0], 0, [4, 7, 11], RED)
        set_color(systems[1], 0, [3, 4], RED)

        self.play(Write(systems, run_time=1.5))
        self.wait(2)

        systems2 = VGroup(
            MathTex(r"""
\begin{cases}
    u' = 0 \\
    u = v
\end{cases}
        """, color="#dbeda4"),
            MathTex(r"""
\begin{cases}
    u = 0 \\
    u' = -v
\end{cases}
        """, color="#dbeda4")
        )
        systems2.arrange(RIGHT)

        self.play(ReplacementTransform(systems, systems2, run_time=1.5))
        self.wait(2)

        intersections = VGroup(
            MathTex("(0; v)"),
            MathTex("(-v; 0)")
        )
        intersections.arrange(RIGHT)
        intersections.next_to(systems2, DOWN)
        
        intersections.set_color("#dbeda4")

        self.play(Write(intersections, run_time=1.5))
        self.wait(2)

        intersections_upper = VGroup(
            MathTex("(0; v)"),
            MathTex("(-v; 0)")
        )
        intersections_upper.arrange(RIGHT)
        intersections_upper.to_edge(UP)
        intersections_upper.to_edge(RIGHT)

        intersections_upper.set_color("#dbeda4")

        self.play(Unwrite(systems2, run_time=0.7), ReplacementTransform(intersections, intersections_upper, run_time=1.5))
        self.wait(2)

        original = MathTex("\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}>0", color="#e35235")
        self.play(Write(original, run_time=1.5))
        self.wait(2)

        self.play(Unwrite(original, run_time=0.7))

        num = MathTex(r"u' + v > 0", color="#e35235")
        self.play(Write(num, run_time=1.5))
        self.wait(2)

        num2 = MathTex(r"u' > -v", color="#e35235")
        self.play(FadeTransformPieces(num, num2, run_time=1.5))
        self.wait(2)

        num2_moved = MathTex(r"u' > -v", color="#e35235")
        num2_moved.to_edge(RIGHT)

        self.play(ReplacementTransform(num2, num2_moved, run_time=1.5))
        self.wait(2)

        den = MathTex(r"\frac{u'v}{c^2} + 1 > 0", color="#e35235")
        self.play(Write(den, run_time=1.5))
        self.wait(2)

        den2 = MathTex(r"u' > - \frac{c^2}{v}", color="#e35235")
        self.play(FadeTransformPieces(den, den2, run_time=1.5))
        self.wait(2)

        num_new = MathTex(r"u' > -v", color="#e35235")
        num_new.shift(UP / 2)

        den_new = MathTex(r"u' > - \frac{c^2}{v}", color="#e35235")
        den_new.next_to(num_new, DOWN)

        self.play(ReplacementTransform(num2_moved, num_new, run_time=1.5), ReplacementTransform(den2, den_new, run_time=1.5))
        self.wait(2)

        positive = VGroup(
            MathTex(r"u>0: u'< - \frac{c^2}{v} \vee u'>-v"),
            MathTex(r"u=0: u'=-v"),
            MathTex(r"u<0: - \frac{c^2}{v} <u'<-v")
        )
        positive.arrange(DOWN)
        
        positive.set_color("#e35235")

        self.play(Unwrite(num_new, run_time=0.7), Unwrite(den_new, run_time=0.7))
        
        self.play(Write(positive, run_time=1.5))
        
        self.play(Indicate(positive[0], run_time=0.5, color="#e35235"))
        self.play(Indicate(positive[1], run_time=0.5, color="#e35235"))
        self.play(Indicate(positive[2], run_time=0.5, color="#e35235"))
        self.wait(2)

        # i have a severe naming problem
        positiveness = MathTex(r"u>0: u'< - \frac{c^2}{v} \vee u'>-v", color="#e35235")
        positiveness.to_edge(DOWN)
        positiveness.to_edge(RIGHT)

        self.play(Unwrite(positive, run_time=0.7), Write(positiveness, run_time=1.5))
        self.wait(2)
        

        limit = MathTex("\\lim_{u\' \\rightarrow - \\frac{c^2}{v} } {\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}}", color="#e78c4b")

        rect = SurroundingRectangle(domain_new, color="#e78c4b")
        self.play(Create(rect, run_time=1))
        self.play(Uncreate(rect, run_time=1), Write(limit, run_time=1.5))
        self.wait(2)

        self.play(
            limit[0][11].animate.set_color(BLUE),
            limit[0][12].animate.set_color(BLUE),

            limit[0][16].animate.set_color(BLUE),
            limit[0][17].animate.set_color(BLUE),

        )
        self.wait(2)

        limit2 = MathTex(r"\frac{ - \frac{c^2}{v} + v}{- \frac{c^2v}{vc^2} + 1}", color="#e78c4b")

        set_color(limit2, 0, [0, 1, 2, 3, 4, 8, 9, 10, 13], color=BLUE)

        self.play(FadeTransformPieces(limit, limit2, run_time=1.5))
        self.wait(2)

        self.play(limit2.animate.set_color("#e78c4b"))
        self.wait(2)

        self.play(
            limit2[0][0].animate.set_color(BLUE),
            limit2[0][1].animate.set_color(BLUE),
            limit2[0][2].animate.set_color(BLUE),
            limit2[0][3].animate.set_color(BLUE),
            limit2[0][4].animate.set_color(BLUE),
            limit2[0][5].animate.set_color(BLUE),
            limit2[0][6].animate.set_color(BLUE),

            limit2[0][8].animate.set_color(BLUE),
            limit2[0][9].animate.set_color(BLUE),
            limit2[0][10].animate.set_color(BLUE),
            limit2[0][11].animate.set_color(BLUE),
            limit2[0][12].animate.set_color(BLUE),
            limit2[0][13].animate.set_color(BLUE),
            limit2[0][14].animate.set_color(BLUE),
            limit2[0][15].animate.set_color(BLUE)
        )
        self.wait(2)

        limit3 = MathTex(r"\frac{ \frac{-c^2+v^2}{v}}{-1 + 1}", color="#e78c4b")

        set_color(limit3, 0, [0, 1, 2, 3, 4, 5, 6, 7, 9, 10], BLUE)

        self.play(FadeTransformPieces(limit2, limit3, run_time=1.5))
        self.wait(2)

        self.play(limit3.animate.set_color("#e78c4b"))
        self.wait(2)

        self.play(
            limit3[0][0].animate.set_color(BLUE),
            limit3[0][1].animate.set_color(BLUE),
            limit3[0][2].animate.set_color(BLUE),
            limit3[0][3].animate.set_color(BLUE),
            limit3[0][4].animate.set_color(BLUE),
            limit3[0][5].animate.set_color(BLUE),

            limit3[0][9].animate.set_color(BLUE),
            limit3[0][10].animate.set_color(BLUE),
            limit3[0][11].animate.set_color(BLUE),
            limit3[0][12].animate.set_color(BLUE)
        )
        self.wait(2)

        limit4 = MathTex(r"\frac{v^2-c^2}{0}", color="#e78c4b")

        set_color(limit4, 0, [0, 1, 2, 3, 4, 6], BLUE)

        self.play(FadeTransformPieces(limit3, limit4, run_time=1.5))
        self.wait(2)

        limit6_lower = MathTex(r"\frac{v^2-c^2}{0}", color="#e78c4b")
        limit6_lower.to_edge(RIGHT)
        
        system = MathTex(r"v^2 - c^2 < 0 \mathrm{\ } \forall v", color="#e78c4b")

        self.play(FadeTransformPieces(limit4, limit6_lower, run_time=1.5), Write(system, run_time=1.5))
        self.wait(2)

        system2 = MathTex(r"(v < c \Rightarrow v^2 < c^2 \Rightarrow v^2 - c^2 < 0)", color="#e78c4b")
        system2.next_to(system, DOWN)

        self.play(Write(system2, run_time=1.5))
        self.wait(2)

        results = MathTex("""
\\begin{matrix}
\\\ -: + \infty
\\\ +: - \infty
\\end{matrix}
        """)

        results.set_color("#e78c4b")

        arrow = MathTex("\\Rightarrow", color="#e78c4b")

        results.next_to(arrow)
        
        limit_final = MathTex(r"\frac{v^2-c^2}{0}", color="#e78c4b")
        limit_final.shift(LEFT * 1.3)

        total = VGroup(arrow, results)
        total.next_to(limit_final, RIGHT)

        self.play(Unwrite(system2, run_time=0.7), Unwrite(system, run_time=0.7), ReplacementTransform(limit6_lower, limit_final, run_time=1.5))
        self.wait(2)

        self.play(Write(total, run_time=1.5))
        self.wait(2)

        end = VGroup(
            MathTex(r"u'=- \frac{c^2}{v}"),
            MathTex("\\mathrm{asintoto\\ verticale}")
        )
        end.arrange(DOWN)
        end.set_color("#e78c4b")

        self.play(Unwrite(limit_final, run_time=0.7), Unwrite(total, run_time=0.7))
        self.play(Write(end, run_time=1.5))
        self.wait(2)

        first_limit = MathTex(r"u' = - \frac{c^2}{v}", color="#e78c4b")
        first_limit.to_edge(DOWN)
        first_limit.to_edge(LEFT)

        self.play(ReplacementTransform(end, first_limit, run_time=1.5))
        self.wait(2)

        limith = MathTex(r"\lim_{u' \rightarrow \pm \infty } {\frac{u'+v}{\frac{u'v}{c^2}+1}}", color="#e78c4b")
        self.play(Write(limith, run_time=1.5))
        self.wait(2)

        limith2 = MathTex(r"\lim_{u' \rightarrow \pm \infty } {\frac{u'(1+ \frac{v}{u'})}{u'(\frac{v}{c^2}+\frac{1}{u'})}}", color="#e78c4b")
        self.play(FadeTransformPieces(limith, limith2, run_time=1.5))
        self.wait(2)

        self.play(
            limith2[0][8].animate.set_color(BLUE),
            limith2[0][9].animate.set_color(BLUE),

            limith2[0][19].animate.set_color(BLUE),
            limith2[0][20].animate.set_color(BLUE)
        )
        self.wait(2)

        limith3 = MathTex(r"\lim_{u' \rightarrow \pm \infty } {\frac{1+ \frac{v}{u'}}{\frac{v}{c^2}+\frac{1}{u'}}}", color="#e78c4b")
        self.play(FadeTransformPieces(limith2, limith3, run_time=1.5))
        self.wait(2)

        self.play(
            limith3[0][3].animate.set_color(BLUE),
            limith3[0][4].animate.set_color(BLUE),
            limith3[0][5].animate.set_color(BLUE),
            limith3[0][6].animate.set_color(BLUE),
            limith3[0][7].animate.set_color(BLUE),

            limith3[0][10].animate.set_color(BLUE),
            limith3[0][11].animate.set_color(BLUE),
            limith3[0][12].animate.set_color(BLUE),
            limith3[0][13].animate.set_color(BLUE),

            limith3[0][20].animate.set_color(BLUE),
            limith3[0][21].animate.set_color(BLUE),
            limith3[0][22].animate.set_color(BLUE),
            limith3[0][23].animate.set_color(BLUE)
        )
        self.wait(2)

        limith4 = MathTex(r"\frac{1}{\frac{v}{c^2}}", color="#e78c4b")
        self.play(ReplacementTransform(limith3, limith4, run_time=1.5))
        self.wait(2)

        limith5 = VGroup(
            MathTex(r"u=\frac{c^2}{v}"),
            MathTex("\\mathrm{asintoto\\ orizzontale}")
        )
        limith5.arrange(DOWN)
        limith5.set_color("#e78c4b")

        self.play(Unwrite(limith4, run_time=0.7))
        self.play(Write(limith5, run_time=1.5))
        self.wait(2)

        limith_end = MathTex(r"u=\frac{c^2}{v}", color="#e78c4b")
        limith_end.to_edge(DOWN)
        limith_end.shift(LEFT * 2)

        self.play(ReplacementTransform(limith5, limith_end, run_time=1.5))
        self.wait(2)

class UUPrime2(Scene):
    def construct(self):
        vech = Vector(direction=RIGHT)
        vech.set_length(3)

        vecv = Vector(direction=UP)
        vecv.set_length(3)
        
        vecv.next_to(vech.get_start(), direction=UP, buff=0) # apparently buff is the distance from the two mobjects

        label = MathTex(r"\mathrm{S}")
        label.next_to(vecv, UP)

        dot = Dot(point=UP)
        dot.shift(RIGHT)

        axes1 = VGroup(vecv, vech, label, dot)
        axes1.scale(0.9)
        
        axes1.move_to(0)
        axes1.shift(LEFT * 1.5)

        axes1[0].set_color("#eba978")
        axes1[1].set_color("#eba978")
        axes1[2].set_color("#eba978")

        self.play(Write(axes1, run_time=1.5))
        self.wait(2)

        u = Vector(direction=RIGHT)
        u.next_to(dot.get_start(), direction=RIGHT, buff=0)

        u_label = MathTex(r"\vec{u}")
        u_label.next_to(u, UP)

        u_thing = VGroup(u, u_label)
        u_thing.set_color("#eba978")

        self.play(Write(u_thing, run_time=1))
        self.wait(2)

        self.play(Unwrite(u_thing, run_time=0.7))
        self.wait(2)

        vech2 = Vector(direction=RIGHT)
        vech2.set_length(3)

        vecv2 = Vector(direction=UP)
        vecv2.set_length(3)
        
        vecv2.next_to(vech2.get_start(), direction=UP, buff=0) # apparently buff is the distance from the two mobjects

        label2 = MathTex(r"\mathrm{S'}")
        label2.next_to(vecv2, UP)

        axes2 = VGroup(vecv2, vech2, label2)
        axes2.scale(0.9)
        
        axes2.move_to(0)
        axes2.shift(UP / 2 + LEFT / 2)

        axes2.set_color("#e65c5c")

        self.play(Write(axes2, run_time=1.5))
        self.wait(2)

        u2 = Vector(direction=RIGHT)
        u2.next_to(dot.get_start(), direction=RIGHT, buff=0)

        u_label2 = MathTex(r"\vec{u'}")
        u_label2.next_to(u2, UP)

        u_thing2 = VGroup(u2, u_label2)
        u_thing2.set_color("#e65c5c")

        self.play(Write(u_thing2, run_time=1))
        self.wait(2)

        self.play(Unwrite(u_thing2, run_time=0.7))
        self.wait(2)

        v_vec = Vector(direction=RIGHT, color=GREEN)
        v_vec.set_length(1)

        v_vec.shift(LEFT * 1.8)

        v_label = MathTex(r"\vec{v}", color=GREEN)
        v_label.next_to(v_vec, UP)

        v = VGroup(v_vec, v_label)

        self.play(Write(v, run_time=1))
        self.wait(2)

        vech3 = Vector(direction=RIGHT)
        vech3.set_length(3)

        vecv3 = Vector(direction=UP)
        vecv3.set_length(3)
        
        vecv3.next_to(vech3.get_start(), direction=UP, buff=0) # apparently buff is the distance from the two mobjects

        label3 = MathTex(r"\mathrm{S'}")
        label3.next_to(vecv3, UP)

        axes3 = VGroup(vecv3, vech3, label3)
        axes3.scale(0.9)
        
        axes3.move_to(0)
        axes3.shift(UP / 2 + RIGHT * 3)

        axes3.set_color("#e65c5c")

        v_vec2 = Vector(direction=RIGHT, color=GREEN)
        v_vec2.set_length(1)

        v_vec2.shift(RIGHT * 1.75)
        
        v_label2 = MathTex(r"\vec{v}", color=GREEN)
        v_label2.next_to(v_vec2, UP)

        v2 = VGroup(v_vec2, v_label2)

        self.play(ReplacementTransform(axes2, axes3, run_time=1.5), ReplacementTransform(v, v2, run_time=1.5))
        self.wait(2)

        title = MathTex(r"\mathrm{Trasformazioni\ di\ Galileo}", color="#99c3e8")
        title.to_edge(UP)

        transformation = MathTex(r"""
\begin{cases}
    x' = x - vt \\
    y' = y \\
    z' = z \\
    t' = t
\end{cases}
        """)
        transformation.set_color("#99c3e8")

        set_color(transformation, 0, [12, 15, 19, 23, 27], "#eba978")
        set_color(transformation, 0, [9, 10, 16, 17, 20, 21, 24, 25], "#e65c5c")
        set_color(transformation, 0, [14], GREEN)

        self.play(Unwrite(axes1, run_time=0.7), Unwrite(axes3, run_time=0.7), Unwrite(v2, run_time=0.7))
        self.wait(2)

        self.play(Write(title, run_time=1.5), Write(transformation, run_time=1.5))
        self.wait(2)

        transformation2 = MathTex(r"""
\begin{cases}
    x' = x - vt \\
    y' = y \\
    z' = z \\
    t' = t
\end{cases}
        """)
        transformation2.set_color("#99c3e8")
        transformation2.shift(LEFT * 4)

        set_color(transformation2, 0, [12, 15, 19, 23, 27], "#eba978")
        set_color(transformation2, 0, [9, 10, 16, 17, 20, 21, 24, 25], "#e65c5c")
        set_color(transformation2, 0, [14], GREEN)

        self.play(ReplacementTransform(transformation, transformation2, run_time=1.5))
        self.wait(2)

        t3 = MathTex(r"u' = u - v")
        t3.set_color("#99c3e8")
        t3.shift(RIGHT * 3)

        set_color(t3, 0, [0, 1], "#e65c5c")
        set_color(t3, 0, [3], "#eba978")
        set_color(t3, 0, [5], GREEN)

        self.play(Write(t3, run_time=1.5))
        self.wait(2)

        t4 = MathTex(r"u' = u - v")
        t4.set_color("#99c3e8")
        t4.shift(RIGHT * 3 + UP * 1.5)

        set_color(t4, 0, [0, 1], "#e65c5c")
        set_color(t4, 0, [3], "#eba978")
        set_color(t4, 0, [5], GREEN)

        ex = VGroup(
            MathTex(r"u=\frac{2}{3}c"),
            MathTex(r"v=-\frac{2}{3}c")
        )
        ex.arrange(DOWN)
        ex.shift(DOWN * 0.5 + LEFT)

        ex[0][0].set_color("#eba978")
        ex[1][0].set_color(GREEN)

        self.play(ReplacementTransform(t3, t4, run_time=1.5))
        self.play(Write(ex, run_time=1.5))
        self.wait(2)

        end = MathTex(r"\Rightarrow", r"u'=\frac{4}{3}c")
        end.next_to(ex, RIGHT)
        
        end[0].set_color("#99c3e8")
        end[1].set_color("#e65c5c")

        self.play(Write(end, run_time=1.5))
        self.wait(2)

        imp = VGroup(
            MathTex(r"u' > c"),
            MathTex(r"\mathrm{Impossibile}")
        )
        imp.arrange(DOWN)
        imp.next_to(end, RIGHT)
        imp.shift(RIGHT)
        
        imp.set_color("#f2aa00")

        self.play(Write(imp, run_time=1.5))
        self.wait(2)

        axiom = MathTex(r"\mathrm{Secondo\ assioma\ della\ relativit}", r"\mathrm{\grave a}", r"\mathrm{\ ristretta}", color="#f2aa00")
        axiom.to_edge(DOWN)

        self.play(Write(axiom, run_time=1.5))
        self.wait(2)

class Question(Scene):
    def construct(self):
        q = MathTex(r"u \leftrightarrow u'", color=GREEN)

        mark = MathTex(r"?", color=YELLOW)
        mark.scale(1.4)

        g = VGroup(q, mark)
        g.arrange(DOWN)

        self.play(Write(g, run_time=1.5))
        self.wait(2)

        self.play(Unwrite(g, run_time=0.7))
        self.wait(2)

class Einstein(Scene):
    def construct(self):
        axioms = BulletedList(
            "Le leggi della fisica sono le stesse in tutti i sistemi di riferimento inerziali",
            "La luce si propaga nel vuoto a velocità costante c, indipendentemente dallo stato di moto della sorgente o dell’osservatore"
        )
        axioms.scale(0.7)

        self.play(Write(axioms, run_time=2.5))
        self.wait(5)

        self.play(Unwrite(axioms, run_time=2.5))
        self.wait(2)
