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
        text.next_to(approx2, DOWN)
        self.play(Write(text, run_time=1.5))