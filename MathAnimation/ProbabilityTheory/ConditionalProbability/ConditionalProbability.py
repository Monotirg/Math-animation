from manim import *


class ConditionalProbability(Scene):
    def construct(self):
        circle_left = Circle(2, color=BLUE, stroke_width=1, fill_color=BLUE, fill_opacity=0.7).shift(RIGHT)
        circle_right = Circle(2, color=RED,stroke_width=1 ,fill_color=RED, fill_opacity=0.8).set_z_index(circle_left.z_index-1).shift(LEFT)
        formula = MathTex(r"P(A|B) = \frac{P(A \cap B)}{P(B)}").set_z_index(circle_left.z_index + 1)
        VGroup(VGroup(circle_left, circle_right), formula).arrange(RIGHT, buff = 1.5)
        
        label_a = MathTex("B").move_to(circle_left.get_top()).shift(0.325*UP)
        label_b = MathTex("A").move_to(circle_right.get_top()).shift(0.325*UP)
        
        intersection_cirlce = Intersection(circle_left, circle_right, color=GREEN, fill_color=GREEN, fill_opacity=0.5).set_z_index(circle_left.z_index + 1)
        
        self.play(DrawBorderThenFill(VGroup(circle_left, circle_right)))
        self.play(FadeIn(label_a, label_b))
        self.play(FadeIn(formula[0][0:7], formula[0][13]))
        self.play(FadeIn(intersection_cirlce), run_time=0.75)
        self.play(ReplacementTransform(intersection_cirlce, formula[0][7:13]))
        self.wait(0.5)
        self.play(ReplacementTransform(circle_left.copy(), formula[0][14:]))
        self.wait(0.5)