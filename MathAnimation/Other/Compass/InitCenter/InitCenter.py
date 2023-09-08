from manim import *


class InitCenter(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        dot_left = Dot(color="#0000FF", radius=0.15).shift(1.4*LEFT + 2.4*DOWN)
        dot_right = Dot(color="#FF0000", radius=0.15).shift(1.4*RIGHT + 2.4*DOWN)
        dot_center = Dot(color="#000000", radius=0.15).shift(2*UP)
        dot_mid = Dot(color="#000000", radius=0.15).shift(DOWN)
        
        line_left = always_redraw(
            lambda: Line(
                dot_center.get_center(), 
                dot_left.get_center(), 
                color=BLACK, 
                stroke_width=6, 
                z_index=dot_left.get_z_index()-1
            )
        )
        line_right = always_redraw(
            lambda: Line(
                dot_center.get_center(), 
                dot_right.get_center(), 
                color=BLACK, 
                stroke_width=6, 
                z_index=dot_left.get_z_index()-1
            )
        )
        line_radius = always_redraw(
            lambda: Line(
                dot_left.get_center(), 
                dot_right.get_right(), 
                color=BLACK,
                stroke_width=6,
                z_index=dot_left.get_z_index()-1
            )
        )
       
        vec_norm = always_redraw(
            lambda : Line(
                [0, -1, 0],
                dot_center.get_center() - [0, dot_center.radius, 0],
                buff=0,
                color=BLACK, 
                stroke_width=6
            ).add_tip(tip_length=0.25, tip_width=0.25)
        )
        
        label_left = Text("left", color = BLACK).next_to(dot_left, DOWN)
        label_right = Text("right", color = BLACK).next_to(dot_right, DOWN)
        label_center = Text("center", color = BLACK).next_to(dot_center, UP) 
        
        self.add(dot_left, dot_right)
        self.add(label_left, label_right)
        self.wait(0.4)
        self.play(FadeOut(label_left, label_right))
        self.play(Create(line_radius))
        self.play(FadeIn(dot_mid))
        self.play(AnimationGroup(
            AnimationGroup(
                GrowFromPoint(vec_norm, vec_norm.get_start()), 
                DrawBorderThenFill(dot_center), 
                run_time=1.2
            ),
            AnimationGroup(
                Create(line_left), 
                Create(line_right)
            ),
            lag_ratio=0.8
        ))
        self.play(dot_center.animate.shift(2.2*DOWN), run_time=1)
        self.play(dot_center.animate.shift(2.2*UP), run_time=1)
        self.play(AnimationGroup(
            FadeOut(line_radius, dot_mid, vec_norm),
            FadeIn(label_left, label_right, label_center), 
            lag_ratio=0.3
        ))
        self.wait(0.4)
