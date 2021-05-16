# GRAPHS CAN BE FOUND AT https://www.desmos.com/calculator/kgjbfb4nze

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

        ueqc = MathTex("u=c", color=RED)
        ueqc.to_edge(UP)
        ueqc.shift(DOWN * 0.6)

        self.play(Write(ueqc, run_time=1))
        self.wait(0.7)

        self.play(
            text1[0][3].animate.set_color(RED),
            text1[0][9].animate.set_color(RED)
        )
        self.wait()

        text2 = MathTex("u\'=\\frac{c-v}{1-\\frac{cv}{c^2}}")
        self.play(ReplacementTransform(text1, text2, run_time=1.5))
        self.wait()

        self.play(
            text2[0][9].animate.set_color(RED),
            text2[0][13].animate.set_color(RED),
        )
        self.wait()

        text3 = MathTex("u\'=\\frac{c-v}{1-\\frac{v}{c}}")
        self.play(FadeTransform(text2, text3, run_time=1.5))
        self.wait()

        self.play(
            text3[0][7].animate.set_color(RED),
            text3[0][8].animate.set_color(RED),
            text3[0][9].animate.set_color(RED),
            text3[0][10].animate.set_color(RED),
            text3[0][11].animate.set_color(RED)
        )
        self.wait()

        text4 = MathTex("u\'=\\frac{c-v}{\\frac{c-v}{c}}")
        self.play(ReplacementTransform(text3, text4, run_time=1.5))
        self.wait()

        self.play(
            text4[0][10].animate.set_color(RED),
            text4[0][11].animate.set_color(RED)
        )
        self.wait()

        text5 = MathTex("u\'=\\frac{c-v}{c-v}c")
        self.play(ReplacementTransform(text4, text5, run_time=1.5))
        self.wait()
        
        self.play(
            text5[0][3].animate.set_color(RED),
            text5[0][4].animate.set_color(RED),
            text5[0][5].animate.set_color(RED),
            text5[0][6].animate.set_color(RED),
            text5[0][7].animate.set_color(RED),
            text5[0][8].animate.set_color(RED),
            text5[0][9].animate.set_color(RED)
        )
        self.wait()

        text6 = MathTex("u\'=c")
        self.play(ReplacementTransform(text5, text6, run_time=1.5))
        self.wait(0.8)

        last = MathTex(r"\mathrm{Invarianza\ della\ velocit}", r"\mathrm{\grave a}", r"\ \mathrm{della\ luce}", color=RED)
        last.next_to(text6, UP)

        lower_upper = MathTex("u=c", color=RED)
        lower_upper.next_to(text6, DOWN)

        self.play(Indicate(text6, color=RED), Write(last, run_time=1.5), ReplacementTransform(ueqc, lower_upper, run_time=1.5))
        self.wait()

class VerySmallSpeed(Scene):
    """ Shows how to derive the Galilean transformation. """
    def construct(self):
        upper_text = MathTex("u\'=\\frac{u-v}{1-\\frac{uv}{c^2}}")        

        group = VGroup(
            MathTex("\mathrm{Se\\ }"),
            MathTex("v<<c"),
            MathTex("\mathrm{\\ e\\ }"),
            MathTex("u<<c"),
            MathTex("\mathrm{,\\ allora}")
        )
        # the order matters!
        group.arrange(RIGHT)
        group.to_edge(UP)

        self.play(Write(upper_text, run_time=1.5))
        self.wait()

        lower_text = MathTex("u\'=\\frac{u-v}{1-\\frac{uv}{c^2}}") 
        lower_text.to_edge(DOWN)

        self.play(
            upper_text[0][9].animate.set_color(BLUE),
            upper_text[0][10].animate.set_color(BLUE)
        )
        self.wait()

        lower_text[0][9].set_color(BLUE)
        lower_text[0][10].set_color(BLUE)

        self.play(FadeTransform(upper_text, lower_text, run_time=1.5))
        self.play(Write(group, run_time=1))

        self.play(Indicate(group[1], color=BLUE))
        self.play(Indicate(group[3], color=BLUE))
        self.wait()

        approx1 = MathTex("u\'\\approx\\frac{u-v}{1-0}")

        approx1[0][-1].set_color(BLUE)

        self.play(Write(approx1, run_time=1.5))
        self.wait()

        approx2 = MathTex("u\'\\approx u-v")
        self.play(ReplacementTransform(approx1, approx2, run_time=1.5))
        self.wait()

        text = MathTex("\mathrm{Trasformazione\\ di\\ Galileo}", color=BLUE)
        text.next_to(approx2, UP)
        self.play(Write(text, run_time=1.5), Indicate(approx2, color=BLUE))
        self.wait()

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
        self.play(FadeTransform(text1, text2, run_time=1.5))
        self.wait()

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

        lower_text = VGroup(
            MathTex(r"x'= \gamma (x-vt)", color="#e3af7f"),
            MathTex(r"t'= \gamma (t-\frac{vx}{c^2})", color="#e3af7f")
        )
        lower_text.arrange(DOWN)
        lower_text.to_edge(DOWN)
        lower_text.to_edge(RIGHT)

        rect1 = Rectangle(color="#e3af7f", height=0.55, width=3.1)
        rect2 = Rectangle(color="#e3af7f", height=0.65, width=3.0)
        rect1.shift(UP + DOWN * 0.1 + RIGHT * 0.2) # upper
        rect2.shift(DOWN * 1 + UP * 0.1 + RIGHT * 0.2) # lower

        self.play(Create(rect1, run_time=1.5), Create(rect2, run_time=1.5), Write(lower_text, run_time=1.5))
        self.play(Uncreate(rect1), Uncreate(rect2))
        self.wait()

        self.play(Unwrite(system, run_time=1.5))
        self.wait()

        forgot = MathTex(r"\frac{\Delta x'}{\Delta t'} = \frac{x_2' - x_1'}{t_2' - t_1'}")

        forgot[0][8].set_color("#e3af7f")
        forgot[0][9].set_color("#e3af7f")
        forgot[0][10].set_color("#e3af7f")

        forgot[0][12].set_color("#e3af7f")
        forgot[0][13].set_color("#e3af7f")
        forgot[0][14].set_color("#e3af7f")

        forgot[0][16].set_color("#e3af7f")
        forgot[0][17].set_color("#e3af7f")
        forgot[0][18].set_color("#e3af7f")

        forgot[0][20].set_color("#e3af7f")
        forgot[0][21].set_color("#e3af7f")
        forgot[0][22].set_color("#e3af7f")


        self.play(Write(forgot, run_time=1.5))
        self.wait()
        
        formula3 = MathTex("\\frac{\\Delta x\'}{\\Delta t\'}=\\frac{\\gamma (x_2-vt_2)- \\gamma (x_1-vt_1)}{\\gamma (t_2-\\frac{vx_2}{c^2})- \\gamma (t_1-\\frac{vx_1}{c^2})}")

        formula3[0][8].set_color("#e3af7f")
        formula3[0][9].set_color("#e3af7f")
        formula3[0][10].set_color("#e3af7f")
        formula3[0][11].set_color("#e3af7f")
        formula3[0][12].set_color("#e3af7f")
        formula3[0][13].set_color("#e3af7f")
        formula3[0][14].set_color("#e3af7f")
        formula3[0][15].set_color("#e3af7f")
        formula3[0][16].set_color("#e3af7f")

        formula3[0][18].set_color("#e3af7f")
        formula3[0][19].set_color("#e3af7f")
        formula3[0][20].set_color("#e3af7f")
        formula3[0][21].set_color("#e3af7f")
        formula3[0][22].set_color("#e3af7f")
        formula3[0][23].set_color("#e3af7f")
        formula3[0][24].set_color("#e3af7f")
        formula3[0][25].set_color("#e3af7f")
        formula3[0][26].set_color("#e3af7f")

        formula3[0][28].set_color("#e3af7f")
        formula3[0][29].set_color("#e3af7f")
        formula3[0][30].set_color("#e3af7f")
        formula3[0][31].set_color("#e3af7f")
        formula3[0][32].set_color("#e3af7f")
        formula3[0][33].set_color("#e3af7f")
        formula3[0][34].set_color("#e3af7f")
        formula3[0][35].set_color("#e3af7f")
        formula3[0][36].set_color("#e3af7f")
        formula3[0][37].set_color("#e3af7f")
        formula3[0][38].set_color("#e3af7f")
        formula3[0][39].set_color("#e3af7f")

        formula3[0][41].set_color("#e3af7f")
        formula3[0][42].set_color("#e3af7f")
        formula3[0][43].set_color("#e3af7f")
        formula3[0][44].set_color("#e3af7f")
        formula3[0][45].set_color("#e3af7f")
        formula3[0][46].set_color("#e3af7f")
        formula3[0][47].set_color("#e3af7f")
        formula3[0][48].set_color("#e3af7f")
        formula3[0][49].set_color("#e3af7f")
        formula3[0][50].set_color("#e3af7f")
        formula3[0][51].set_color("#e3af7f")
        formula3[0][52].set_color("#e3af7f")

        self.play(ReplacementTransform(forgot, formula3, run_time=1.5))
        self.wait()

        self.play(formula3[0].animate.set_color(WHITE))
        self.wait()

        self.play(
            formula3[0][8].animate.set_color("#7cbf00"),
            formula3[0][18].animate.set_color("#7cbf00"),
            formula3[0][28].animate.set_color("#7cbf00"),
            formula3[0][41].animate.set_color("#7cbf00")
        )
        self.wait()

        no_gammas = MathTex("\\frac{\\Delta x\'}{\\Delta t\'}=\\frac{(x_2-vt_2)-(x_1-vt_1)}{(t_2-\\frac{vx_2}{c^2})-(t_1-\\frac{vx_1}{c^2})}")
        self.play(FadeTransform(formula3, no_gammas, run_time=1.5))
        self.wait()

        forgot3 = MathTex("\\frac{\\Delta x\'}{\\Delta t\'}=\\frac{x_2-vt_2-x_1+vt_1}{t_2-\\frac{vx_2}{c^2}-t_1+\\frac{vx_1}{c^2}}")

        self.play(FadeTransform(no_gammas, forgot3, run_time=1.5))
        self.wait()

        forgot2 = MathTex(r"u'= \frac{\Delta x'}{\Delta t'}", color="#64bd90")
        forgot2.to_edge(LEFT)
        forgot2.to_edge(DOWN)

        self.play(Write(forgot2, run_time=1.5))
        self.wait()

        self.play(
            forgot3[0][0].animate.set_color("#64bd90"),
            forgot3[0][1].animate.set_color("#64bd90"),
            forgot3[0][2].animate.set_color("#64bd90"),
            forgot3[0][3].animate.set_color("#64bd90"),
            forgot3[0][4].animate.set_color("#64bd90"),
            forgot3[0][5].animate.set_color("#64bd90"),
            forgot3[0][6].animate.set_color("#64bd90")
        )
        self.wait()

        formula4 = MathTex("u\'=\\frac{x_2-vt_2-x_1+vt_1}{t_2-\\frac{vx_2}{c^2}-t_1+\\frac{vx_1}{c^2}}")

        formula4[0][0].set_color("#64bd90")
        formula4[0][1].set_color("#64bd90")

        self.play(FadeTransform(forgot3, formula4, run_time=1.5))
        self.wait()

        self.play(
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
        self.wait()

        formula5 = MathTex("u\'=\\frac{(x_2-x_1)-v(t_2-t_1)}{(t_2-t_1)-\\frac{v}{c^2}(x_2-x_1)")

        formula5[0][3].set_color("#ff8e2b")
        formula5[0][4].set_color("#ff8e2b")
        formula5[0][5].set_color("#ff8e2b")
        formula5[0][6].set_color("#ff8e2b")
        formula5[0][7].set_color("#ff8e2b")
        formula5[0][8].set_color("#ff8e2b")
        formula5[0][9].set_color("#ff8e2b")

        formula5[0][10].set_color("#c29cff")
        formula5[0][11].set_color("#c29cff")
        formula5[0][12].set_color("#c29cff")
        formula5[0][13].set_color("#c29cff")
        formula5[0][14].set_color("#c29cff")
        formula5[0][15].set_color("#c29cff")
        formula5[0][16].set_color("#c29cff")
        formula5[0][17].set_color("#c29cff")
        formula5[0][18].set_color("#c29cff")

        formula5[0][20].set_color("#c29cff")
        formula5[0][21].set_color("#c29cff")
        formula5[0][22].set_color("#c29cff")
        formula5[0][23].set_color("#c29cff")
        formula5[0][24].set_color("#c29cff")
        formula5[0][25].set_color("#c29cff")
        formula5[0][26].set_color("#c29cff")

        formula5[0][27].set_color("#ff8e2b")
        formula5[0][28].set_color("#ff8e2b")
        formula5[0][29].set_color("#ff8e2b")
        formula5[0][30].set_color("#ff8e2b")
        formula5[0][31].set_color("#ff8e2b")
        formula5[0][32].set_color("#ff8e2b")
        formula5[0][33].set_color("#ff8e2b")
        formula5[0][34].set_color("#ff8e2b")
        formula5[0][35].set_color("#ff8e2b")
        formula5[0][36].set_color("#ff8e2b")
        formula5[0][37].set_color("#ff8e2b")
        formula5[0][38].set_color("#ff8e2b")

        self.wait()

        self.play(FadeTransform(formula4, formula5, run_time=1.5))
        self.wait()

        self.play(formula5[0].animate.set_color(WHITE))
        self.wait()
        
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

            formula5[0][32].animate.set_color("#7cbf00"), # TODO: HERE
            formula5[0][33].animate.set_color("#7cbf00"),
            formula5[0][34].animate.set_color("#7cbf00"),
            formula5[0][35].animate.set_color("#7cbf00"),
            formula5[0][36].animate.set_color("#7cbf00"),
            formula5[0][37].animate.set_color("#7cbf00"),
            formula5[0][38].animate.set_color("#7cbf00"),
        )
        self.wait()

        formula6 = MathTex("u\'=\\frac{u(t_2-t_1)-v(t_2-t_1)}{(t_2-t_1)-\\frac{uv}{c^2}(t_2-t_1)")

        formula6[0][3].set_color("#7cbf00")
        formula6[0][4].set_color("#7cbf00")
        formula6[0][5].set_color("#7cbf00")
        formula6[0][6].set_color("#7cbf00")
        formula6[0][7].set_color("#7cbf00")
        formula6[0][8].set_color("#7cbf00")
        formula6[0][9].set_color("#7cbf00")
        formula6[0][10].set_color("#7cbf00")

        # TODO: HERE
        formula6[0][29].set_color("#7cbf00")
        formula6[0][34].set_color("#7cbf00")
        formula6[0][35].set_color("#7cbf00")
        formula6[0][36].set_color("#7cbf00")
        formula6[0][37].set_color("#7cbf00")
        formula6[0][38].set_color("#7cbf00")
        formula6[0][39].set_color("#7cbf00")
        formula6[0][40].set_color("#7cbf00")

        self.play(FadeTransform(formula5, formula6, run_time=1.5))
        self.wait()

        self.play(formula6[0].animate.set_color(WHITE), Unwrite(missing, run_time=1.5))
        self.wait()

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
        self.wait()

        formula7 = MathTex("u\'=\\frac{(t_2-t_1)(u-v)}{(t_2-t_1)(1-\\frac{uv}{c^2})")

        formula7[0][3].set_color("#7cbf00")
        formula7[0][4].set_color("#7cbf00")
        formula7[0][5].set_color("#7cbf00")
        formula7[0][6].set_color("#7cbf00")
        formula7[0][7].set_color("#7cbf00")
        formula7[0][8].set_color("#7cbf00")
        formula7[0][9].set_color("#7cbf00")
        formula7[0][16].set_color("#7cbf00")
        formula7[0][17].set_color("#7cbf00")
        formula7[0][18].set_color("#7cbf00")
        formula7[0][19].set_color("#7cbf00")
        formula7[0][20].set_color("#7cbf00")
        formula7[0][21].set_color("#7cbf00")
        formula7[0][22].set_color("#7cbf00")

        self.play(ReplacementTransform(formula6, formula7, run_time=1.5))
        self.wait()

        formula8 = MathTex("u\'=\\frac{u-v}{1-\\frac{uv}{c^2}")
        self.play(ReplacementTransform(formula7, formula8, run_time=1.5))
        self.wait()

        self.play(Indicate(formula8, color="#7cbf00"))
        self.wait()

class Limit(Scene):
    """ Shows how to derive the vertical asymptote of the function of the relativistic addition of velocities. """
    def construct(self):
        domain = MathTex("\\mathrm{D}:\\forall u\' \mid \\frac{u\'v}{c^2}+1 \\neq 0")

        upper_text = MathTex("u=\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}")
        self.play(Write(upper_text, run_time=1.5))
        self.wait()

        lower_text = MathTex("u=\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}")
        lower_text.to_edge(UP)
        lower_text.to_edge(LEFT)

        self.play(FadeTransform(upper_text, lower_text, run_time=1.5), Write(domain, run_time=1.5))
        self.wait()

        domain2 = MathTex("\\mathrm{D}:\\forall u\' \mid \\frac{u\'v}{c^2} \\neq -1")
        self.play(FadeTransform(domain, domain2, run_time=1.5))
        self.wait()

        domain3 = MathTex("\\mathrm{D}:\\forall u\' \mid u\'v \\neq -c^2")
        self.play(FadeTransform(domain2, domain3, run_time=1.5))
        self.wait()

        domain4 = MathTex("\\mathrm{D}:\\forall u\' \mid u\' \\neq - \\frac{c^2}{v}")
        self.play(FadeTransform(domain3, domain4, run_time=1.5))
        self.wait()

        domain5 = MathTex("\\mathrm{D}:\\forall u\' \mid u\' \\neq - \\frac{c}{\\beta}")
        self.play(ReplacementTransform(domain4, domain5, run_time=1.5))
        self.wait()

        lower_domain = MathTex("\\mathrm{D}:\\forall u\' \mid u\' \\neq - \\frac{c}{\\beta}")

        lower_domain.to_edge(UP)
        lower_domain.to_edge(RIGHT)

        limit = MathTex("\\lim_{u\' \\rightarrow - \\frac{c}{ \\beta} } {\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}}")
        self.play(FadeTransform(domain5, lower_domain, run_time=1.5), Write(limit, run_time=1.5))
        self.wait()

        limit2 = MathTex("\\frac{- \\frac{c}{ \\beta}+v}{-\\frac{cv}{\\beta c^2}+1}")
        self.play(ReplacementTransform(limit, limit2, run_time=1.5))
        self.wait()

        limit3 = MathTex("\\frac{- \\frac{c^2}{ v}+v}{-\\frac{v}{\\beta c}+1}")
        self.play(FadeTransform(limit2, limit3, run_time=1.5))
        self.wait()

        limit4 = MathTex("\\frac{ \\frac{-c^2+v} {v} }{-\\frac{cv}{vc}+1}")
        self.play(FadeTransform(limit3, limit4, run_time=1.5))
        self.wait()

        limit5 = MathTex("\\frac{-c^2+v}{v(-1+1)}")
        self.play(ReplacementTransform(limit4, limit5, run_time=1.5))
        self.wait()

        limit6 = MathTex("\\frac{v-c^2}{0}")
        self.play(FadeTransform(limit5, limit6, run_time=1.5))
        self.wait()

        limit6_lower = MathTex("\\frac{v-c^2}{0}")
        limit6_lower.to_edge(UP)
        
        # FIXME: THIS IS BROKEN
        system = MathTex("""
\\left\{\\begin{matrix} v > 0: v - c^2 < 0 (0 < v < c)
\\\ v < 0: v - c^2 < 0
\\end{matrix}\\right.
        """)
        system.shift(1.3 * LEFT)

        self.play(FadeTransform(limit6, limit6_lower, run_time=1.5), Write(system, run_time=1.5))
        self.wait()

        results = MathTex("""
\\begin{matrix}
\\\ -: + \infty
\\\ +: - \infty
\\end{matrix}
        """)
        #results.arrange(LEFT)
        arrow = MathTex("\\Rightarrow")

        arrow.next_to(system)
        results.next_to(arrow)

        #self.play(ReplacementTransform(system, results, run_time=1.5))
        self.play(Write(arrow, run_time=1.5), Write(results, run_time=1.5))
        self.wait()

        end = VGroup(
            MathTex(r"u'=- \frac{c}{ \beta}"),
            MathTex("\\mathrm{asintoto\\ verticale}")
        )
        end.arrange(DOWN)

        self.play(Unwrite(system, run_time=1.5), Unwrite(results, run_time=1.5), Unwrite(arrow, run_time=1.5), Write(end, run_time=1.5))
        self.wait()

class HLimit(Scene):
    """ Shows how to derive the horizontal asymptote of the function of the relativistic addition of velocities. """
    def construct(self):
        limit = MathTex("\\lim_{u\' \\rightarrow \infty } {\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}}")
        
        upper_text = MathTex("u=\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}")
        self.play(Write(upper_text, run_time=1.5))
        self.wait()

        lower_text = MathTex("u=\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}")
        lower_text.to_edge(UP)

        self.play(FadeTransform(upper_text, lower_text, run_time=1.5), Write(limit, run_time=1.5))
        self.wait()

        limit2 = MathTex(r"\lim_{u' \rightarrow \infty} {\frac{\frac{d}{du'}(u'+v)}{\frac{d}{du'}(\frac{u'v}{c^2}+1)}}")
        self.play(FadeTransform(limit, limit2, run_time=1.5))
        self.wait()

        limit3 = MathTex(r"\frac{1}{\frac{v}{c^2}}")
        self.play(ReplacementTransform(limit2, limit3, run_time=1.5))
        self.wait()

        group = VGroup(
            MathTex(r"u=\frac{c}{\beta}"),
            MathTex("\\mathrm{asintoto\\ orizzontale}"),
        )
        group.arrange(DOWN)

        self.play(ReplacementTransform(limit3, group, run_time=1.5))
        self.wait()

class Derivative(Scene):
    """ Shows how to calculate the derivative of the function of the relativistic addiotion of velocities. """
    def construct(self):
        center = MathTex("\\frac{d}{du\'} u = \\frac{d}{du\'} \\frac{u\'+v}{\\frac{u\'v}{c^2}+1}")

        upper_text = MathTex("u=\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}")
        self.play(Write(upper_text, run_time=1.5))
        self.wait()

        lower_text = MathTex("u=\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}")
        lower_text.to_edge(UP)

        self.play(FadeTransform(upper_text, lower_text, run_time=1.5), Write(center, run_time=1.5))
        self.wait()

        center2 = MathTex(r"\frac{d}{du'} u = \frac{ (1+ \frac{u' v}{c^2} ) - (u'+v) \frac{v}{c^2} } {(1+ \frac{u' v} {c^2})^2}")
        self.play(ReplacementTransform(center, center2, run_time=1.5))
        self.wait()

        center3 = MathTex(r"\frac{d}{du'} u = \frac{ 1+ \frac{u' v}{c^2} - \frac{u'v}{c^2} - \frac{v^2}{c^2} } {(1+ \frac{u' v} {c^2})^2}")
        self.play(FadeTransform(center2, center3, run_time=1.5))
        self.wait()

        center4 = MathTex(r"\frac{d}{du'} u = \frac{ 1 - \beta^2 } {(1+ \frac{\beta}{c} u')^2}")
        self.play(ReplacementTransform(center3, center4, run_time=1.5))
        self.wait()

class StudyDerivative(GraphScene):
    """ Studies the graph of the derivative of the function of the relativistic addition of velocities, and then shows it. """
    def construct(self):
        segno = MathTex(r"\frac{d}{du'} u = \frac{1 - \beta^2}{(1 + \frac{\beta}{c} u')^2}", color=GREEN)
        segno.to_edge(UP)

        self.play(Write(segno, run_time=1.5))
        self.wait()

        domain = MathTex(r"\mathrm{D_{u } } : \forall u' \mid u' \neq - \frac{c}{\beta}", color="#f2aa00")
        domain.to_edge(UP)
        domain.to_edge(RIGHT)
        domain.shift(DOWN * 0.2)

        self.play(Write(domain, run_time=1.5))
        
        segno2 = MathTex(r"\mathrm{Numeratore:\ } 1 - \beta^2", color="#ddccaa")
        self.play(Write(segno2, run_time=1.5))
        self.wait()

        self.play(Unwrite(segno2, run_time=0.6))

        segno3 = MathTex(r"1 - \beta^2 > 0", color="#ddccaa")
        self.play(Write(segno3, run_time=1.5))
        self.wait()

        segno4 = MathTex(r"\beta^2 < 1", color="#ddccaa")
        self.play(FadeTransform(segno3, segno4, run_time=1.5))
        self.wait()

        segno5 = MathTex(r"-1 < \beta < 1", color="#ddccaa")
        self.play(FadeTransform(segno4, segno5, run_time=1.5))
        self.wait()

        segno6 = MathTex(r"-1 < \frac{v}{c} < 1", color="#ddccaa")
        self.play(ReplacementTransform(segno5, segno6, run_time=1.5))
        self.wait()

        segno7 = MathTex(r"-c < v < c", color="#ddccaa")
        self.play(FadeTransform(segno6, segno7, run_time=1.5))
        self.wait()

        segno8 = MathTex(r"\Rightarrow 1 - \beta^2 > 0 \ \forall v", color="#ddccaa")
        segno8.next_to(segno7, DOWN)

        self.play(Write(segno8, run_time=1.5))
        self.wait()

        self.play(Unwrite(segno7, run_time=0.6), Unwrite(segno8, run_time=0.6))
        self.wait()

        den = MathTex(r"\mathrm{Denominatore:\ } (1 + \frac{\beta}{c} u')^2", color="#babaff")

        self.play(Write(den, run_time=1.5))
        self.wait()        

        self.play(Unwrite(den, run_time=0.6))

        den2 = MathTex(r"(1 + \frac{\beta}{c} u')^2 > 0", color="#babaff")
        self.play(Write(den2, run_time=1.5))
        self.wait()

        den3 = MathTex(r"\forall u' \mid 1 + \frac{\beta}{c} u' \neq 0", color="#babaff")
        den3.next_to(den2, DOWN)

        self.play(Write(den3, run_time=1.5))
        self.wait()

        den4 = MathTex(r"u' \neq - \frac{c}{ \beta}", color="#babaff")
        self.play(Unwrite(den2, run_time=0.7), ReplacementTransform(den3, den4, run_time=1.5))
        self.wait()

        den5 = MathTex(r"u' = - \frac{c}{\beta} \notin \mathrm{D_{u}}", color="#f2aa00")
        den5.next_to(den5, DOWN)

        self.play(Write(den5, run_time=1.5))
        self.wait()

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

        """ graph = self.get_graph(derivative, x_min=-20, x_max=20, y_min=-5, y_max=20, discontinuities=[-9], color=GREEN)

        asymptote = self.get_vertical_line_to_graph(1.001 * -c / beta, graph, color="#babaff")
        
        self.play(Create(graph, run_time=1))
        self.add(graph)
        self.wait()

        self.play(Create(asymptote, run_time=1))
        self.wait() """

        graph_before = self.get_graph(derivative, x_min=-20, x_max=1.1 * - c / beta, y_min=-5, y_max=20, color=GREEN)
        graph_after = self.get_graph(derivative, x_min=0.9 * - c / beta, x_max=20, y_min=-5, y_max=20, color=GREEN)

        asymptote = self.get_vertical_line_to_graph(1.001 * -c / beta, graph_before, color="#babaff")

        self.play(Create(graph_before, run_time=0.75))
        self.play(Create(graph_after, run_time=0.75))
        self.wait()

        self.play(Create(asymptote, run_time=1))
        self.wait()

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
        self.wait()

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
        self.wait()

        v = 1.35
        beta = v / c

        var_tracker = on_screen_var.tracker

        graph_before2 = self.get_graph(u_func, x_min=-40, x_max=1.05 * - c / beta, y_min=-80, y_max=80, color=GREEN)
        graph_after2 = self.get_graph(u_func, x_min=0.957 * - c / beta, x_max=40, y_min=-80, y_max=80, color=GREEN)

        self.play(var_tracker.animate.set_value(beta), ReplacementTransform(graph_before1, graph_before2), ReplacementTransform(graph_after1, graph_after2))
        self.wait()

        v = 0.6
        beta = v / c

        graph_before3 = self.get_graph(u_func, x_min=-40, x_max=1.05 * - c / beta, y_min=-80, y_max=80, color=GREEN)
        graph_after3 = self.get_graph(u_func, x_min=0.955 * - c / beta, x_max=40, y_min=-80, y_max=80, color=GREEN)
        
        var_tracker = on_screen_var.tracker

        self.play(var_tracker.animate.set_value(beta), ReplacementTransform(graph_before2, graph_before3), ReplacementTransform(graph_after2, graph_after3))
        self.wait()

        v = 1.8
        beta = v / c

        graph_before4 = self.get_graph(u_func, x_min=-40, x_max=1.05 * - c / beta, y_min=-80, y_max=80, color=GREEN)
        graph_after4 = self.get_graph(u_func, x_min=0.95 * - c / beta, x_max=40, y_min=-80, y_max=80, color=GREEN)
        
        var_tracker = on_screen_var.tracker

        self.play(var_tracker.animate.set_value(beta), ReplacementTransform(graph_before3, graph_before4), ReplacementTransform(graph_after3, graph_after4))
        self.wait()

        v = 1.5
        beta = v / c

        graph_before5 = self.get_graph(u_func, x_min=-40, x_max=1.05 * - c / beta, y_min=-80, y_max=80, color=GREEN)
        graph_after5 = self.get_graph(u_func, x_min=0.95 * - c / beta, x_max=40, y_min=-80, y_max=80, color=GREEN)
        
        var_tracker = on_screen_var.tracker

        self.play(var_tracker.animate.set_value(beta), ReplacementTransform(graph_before4, graph_before5), ReplacementTransform(graph_after4, graph_after5))
        self.wait()

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
        self.wait()

        fgroup_outer = VGroup(
            MathTex(r"y = \frac{ax + b}{cx + d}", color="#96fffc"),
            MathTex(r"(c \neq 0)", color="#96fffc"),
        )
        # the order matters!
        fgroup_outer.arrange(RIGHT)
        fgroup_outer.to_edge(UP)
        fgroup_outer.to_edge(RIGHT)

        self.play(ReplacementTransform(fgroup, fgroup_outer, run_time=1.5))
        self.wait()

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
        self.wait()

        u_func = MathTex(r"u = \frac{u' + v}{\frac{vu'}{c^2} + 1}", color="#8d88f2")
        u_func.next_to(fgroup_outer, DOWN)
        u_func.shift(DOWN)

        self.play(Write(u_func, run_time=1.5))
        self.wait()

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
        self.wait()
