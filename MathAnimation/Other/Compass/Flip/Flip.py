from manim import *


class Flip(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        dot_left = Dot(color="#0000FF", radius=0.15).shift(2*LEFT)
        dot_right = Dot(color="#FF0000", radius=0.15).shift(2*RIGHT)
        dot_center = Dot(color="#000000", radius=0.15).shift(2*UP)
        dot_flip_center = Dot(
            dot_left.get_center() + dot_right.get_center() - dot_center.get_center(),
            color=BLACK, 
            radius=0.15
        )

        vec1 = Line(dot_center.get_center(), dot_right.get_center(), color=BLACK, buff=0.15, stroke_width=6)
        vec1.add_tip(tip_length=0.25, tip_width=0.25)   
        vec2 = Line(dot_left.get_center(), dot_flip_center.get_center(), color=BLACK, buff=0.15, stroke_width=6)
        vec2.add_tip(tip_length=0.25, tip_width=0.25) 

        label_left = Text("left", color=BLACK).next_to(dot_left, DOWN)
        label_right = Text("right", color=BLACK).next_to(dot_right, DOWN)
        label_center = Text("center", color=BLACK).next_to(dot_center, UP)
        label_center_new = label_center.copy().next_to(dot_flip_center, DOWN)

        line_left = Line(dot_center.get_center(), dot_left.get_center(), color=BLACK, stroke_width=6, buff=0.15)
        line_right = Line(dot_center.get_center(), dot_right.get_center(), color=BLACK, stroke_width=6, buff=0.15)
        
        self.add(dot_left, dot_right, dot_center, line_left, line_right)
        self.add(label_left, label_right, label_center)
        self.wait(0.4)
        self.play(FadeOut(label_left, label_right, label_center, line_left, line_right))
        self.play(GrowFromPoint(vec1, vec1.get_start()), run_time = 0.8)
        self.play(ReplacementTransform(vec1, vec2))
        self.play(FadeIn(dot_flip_center), run_time = 0.8)
        self.play(FadeOut(vec2, dot_center), run_time = 0.8)
        
        line_left = Line(dot_flip_center.get_center(), dot_left.get_center(), color=BLACK, stroke_width=6, buff=0.15)
        line_right = Line(dot_flip_center.get_center(), dot_right.get_center(), color=BLACK, stroke_width=6 ,buff=0.15)
        label_left.next_to(dot_left, UP)
        label_right.next_to(dot_right, UP)
        
        self.play(FadeIn(label_left, label_right, label_center_new, line_left, line_right))
        self.wait(0.4)