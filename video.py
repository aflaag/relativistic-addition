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
        self.play(FadeTransform(text2, text3, run_time=1.5))
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

        self.play(FadeTransform(upper_text, lower_text, run_time=1.5), Write(group, run_time=1.5))
        self.wait()

        approx1 = MathTex("u\'\\approx\\frac{u-v}{1-0}")
        self.play(Write(approx1, run_time=1.5))
        self.wait()

        approx2 = MathTex("u\'\\approx u-v")
        self.play(ReplacementTransform(approx1, approx2, run_time=1.5))
        self.wait()

        text = MathTex("\mathrm{Trasformazione\\ di\\ Galileo}")
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
        self.play(FadeTransform(text1, text2, run_time=1.5))
        self.wait()

class Demonstration2(Scene):
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
        self.play(FadeTransform(formula, formula2, run_time=1.5))
        self.wait()

        formula3 = MathTex("\\frac{\\Delta x\'}{\\Delta t\'}=\\frac{(x_2-vt_2)-(x_1-vt_1)}{(t_2-\\frac{vx_2}{c^2})-(t_1-\\frac{vx_1}{c^2})}")

        lower_text = MathTex("\\frac{x\'}{t\'}=\\frac{x-vt}{t-\\frac{vx}{c^2}}")
        lower_text.to_edge(DOWN)

        self.play(FadeTransform(formula2, lower_text, run_time=1.5), Write(formula3, run_time=1.5))
        self.wait()

        formula4 = MathTex("u\'=\\frac{x_2-vt_2-x_1+vt_1}{t_2-\\frac{vx_2}{c^2}-t_1+\\frac{vx_1}{c^2}}")
        self.play(FadeTransform(formula3, formula4, run_time=1.5))
        self.wait()

        formula5 = MathTex("u\'=\\frac{(x_2-x_1)-v(t_2-t_1)}{(t_2-t_1)-\\frac{v}{c^2}(x_2-x_1)")
        self.play(FadeTransform(formula4, formula5, run_time=1.5))
        self.wait()

        formula6 = MathTex("u\'=\\frac{u(t_2-t_1)-v(t_2-t_1)}{(t_2-t_1)-\\frac{uv}{c^2}(t_2-t_1)")
        self.play(FadeTransform(formula5, formula6, run_time=1.5))
        self.wait()

        formula7 = MathTex("u\'=\\frac{(t_2-t_1)(u-v)}{(t_2-t_1)(1-\\frac{uv}{c^2})")
        self.play(ReplacementTransform(formula6, formula7, run_time=1.5))
        self.wait()

        formula8 = MathTex("u\'=\\frac{u-v}{1-\\frac{uv}{c^2}")
        self.play(ReplacementTransform(formula7, formula8, run_time=1.5))
        self.wait()

class Limit(Scene):
    """ Shows how to derive the vertical asymptote of the relativistic addition of velocities function. """
    def construct(self):
        domain = MathTex("\\mathrm{D}:\\forall x\mid \\frac{u\'v}{c^2}+1 \\neq 0")

        upper_text = MathTex("u=\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}")
        self.play(Write(upper_text, run_time=1.5))
        self.wait()

        lower_text = MathTex("u=\\frac{u\'+v}{\\frac{u\'v}{c^2}+1}")
        lower_text.to_edge(UP)
        lower_text.to_edge(LEFT)

        self.play(FadeTransform(upper_text, lower_text, run_time=1.5), Write(domain, run_time=1.5))
        self.wait()

        domain2 = MathTex("\\mathrm{D}:\\forall x\mid \\frac{u\'v}{c^2} \\neq -1")
        self.play(FadeTransform(domain, domain2, run_time=1.5))
        self.wait()

        domain3 = MathTex("\\mathrm{D}:\\forall x\mid u\'v \\neq -c^2")
        self.play(FadeTransform(domain2, domain3, run_time=1.5))
        self.wait()

        domain4 = MathTex("\\mathrm{D}:\\forall x\mid u\' \\neq - \\frac{c^2}{v}")
        self.play(FadeTransform(domain3, domain4, run_time=1.5))
        self.wait()

        domain5 = MathTex("\\mathrm{D}:\\forall x\mid u\' \\neq - \\frac{c}{\\beta}")
        self.play(ReplacementTransform(domain4, domain5, run_time=1.5))
        self.wait()

        lower_domain = MathTex("\\mathrm{D}:\\forall x\mid u\' \\neq - \\frac{c}{\\beta}")

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
            MathTex("x=- \\frac{c}{ \\beta}"),
            MathTex("\\mathrm{asintoto\\ verticale}")
        )
        end.arrange(DOWN)

        self.play(Unwrite(system, run_time=1.5), Unwrite(results, run_time=1.5), Unwrite(arrow, run_time=1.5), Write(end, run_time=1.5))
        self.wait()

class HLimit(Scene):
    """ Shows how to derive the horizontal asymptote of the relativistic addition of velocities function. """
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
            MathTex(r"y=\frac{c^2}{v}"),
            MathTex("\\mathrm{asintoto\\ orizzontale}"),
        )
        # the order matters!
        group.arrange(DOWN)

        self.play(ReplacementTransform(limit3, group, run_time=1.5))
        self.wait()
