from manim import *


class ChangeAngle(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        dot_left = Dot(color = "#0000FF", radius=0.15).shift(1.4*LEFT + 2.4*DOWN)
        dot_left_copy = dot_left.copy().set_opacity(0.25)
        dot_right = Dot(color = "#FF0000", radius=0.15).shift(1.4*RIGHT + 2.4*DOWN)
        dot_right_copy = dot_right.copy().set_opacity(0.25)
        dot_center = Dot(color = "#000000", radius=0.15).shift(2*UP)
        
        label_left = Text("left", color=BLACK).next_to(dot_left, DOWN)
        label_right = Text("right", color=BLACK).next_to(dot_right, DOWN)
        label_center = Text("center", color=BLACK).next_to(dot_center, UP)

        line_left = Line(dot_center.get_center(), dot_left.get_center(), color=BLACK, buff=0.15, stroke_width=6)
        line_right = Line(dot_center.get_center(), dot_right.get_center(), color=BLACK, buff=0.15, stroke_width=6)
        
        compass = VGroup(dot_left, dot_right, dot_center)
        labels = VGroup(label_left, label_right, label_center)

        vec_left = Line(dot_center.get_center(), dot_left.get_center(), color=BLACK, buff=0.15, stroke_width=6)
        vec_left.add_tip(tip_length=0.25, tip_width=0.25)
        vec_left.set_opacity(0.25)
        vec_right = Line(dot_center.get_center(), dot_right.get_center(), color=BLACK, buff=0.15, stroke_width=6)
        vec_right.add_tip(tip_length=0.25, tip_width=0.25)
        vec_right.set_opacity(0.25)
        vec_vertical = Line(dot_center.get_center(), 0.5*(dot_left.get_center() + dot_right.get_center()), color=BLACK, stroke_width=6, buff=0.15)
        vec_vertical.add_tip(tip_length=0.25, tip_width=0.25)
        vec_left_copy =  always_redraw(
            lambda : Line(
                dot_center.get_center(), 
                dot_left.get_center(), 
                color=BLACK, 
                buff=0.15, stroke_width=6
            ).add_tip(tip_length=0.25, tip_width=0.25)
        )
        vec_right_copy = always_redraw(
            lambda: Line(
                dot_center.get_center(), 
                dot_right.get_center(), 
                color=BLACK, 
                buff=0.15, 
                stroke_width=6
            ).add_tip(tip_length=0.25, tip_width= 0.25)
        )
        
        vec_left_label = MathTex(r"\vec{v}_1", color=BLACK).next_to(vec_left, LEFT).shift(0.5*RIGHT)
        vec_right_label = MathTex(r"\vec{v}_2", color=BLACK).next_to(vec_right, RIGHT).shift(0.5*LEFT)

        angle = Angle(vec_left, vec_right, radius=0.9, color=BLACK)         
        angle_label = MathTex(r"\theta", color=BLACK).next_to(angle, DOWN)
        formula = MathTex(r"\theta = \arccos{\frac{(\vec{v}_1,\vec{v}_2)}{|\vec{v}_1||\vec{v}_2|}}", color=BLACK).to_edge(LEFT)

        self.add(compass, labels)
        self.add(dot_left_copy, dot_right_copy)
        self.add(line_left, line_right)
        self.wait(0.4)
        self.play(FadeOut(labels, line_left, line_right), run_time=0.8)
        self.play(AnimationGroup(
            GrowFromPoint(vec_left_copy, vec_left_copy.get_start()),
            GrowFromPoint(vec_right_copy, vec_right_copy.get_start())
            ), 
            run_time=1.2
        )
        self.add(vec_left, vec_right)
        self.play(Create(angle), FadeIn(angle_label), run_time=0.8)
        self.play(FadeIn(vec_left_label, vec_right_label), run_time=0.8)
        self.play(AnimationGroup(
            AnimationGroup(
                ReplacementTransform(angle_label.copy(), formula[0][0]),
                ReplacementTransform(vec_left_label.copy(), formula[0][9:12]),
                ReplacementTransform(vec_right_label.copy(), formula[0][13:16]),
                ReplacementTransform(vec_left_label.copy(), formula[0][19:22]),
                ReplacementTransform(vec_right_label.copy(), formula[0][24:27])
            ),
            FadeIn(formula[0][1:9], formula[0][12],formula[0][16:19],formula[0][22:24], formula[0][27:]),
            lag_ratio=0.3
            )
        )   
        self.wait(0.2)
        self.play(FadeOut(vec_left_label, vec_right_label, formula, angle, angle_label), run_time=0.8)
        self.play(GrowFromPoint(vec_vertical, vec_vertical.get_start()))
        
        angle = always_redraw(lambda : Angle(vec_vertical, vec_right_copy, radius=0.9, color=BLACK))     
        angle_label = MathTex(r"\frac{\theta}{2}", color=BLACK).next_to(angle, DOWN).shift(RIGHT*0.05)
        angle_label_new1 = MathTex(r"\frac{\alpha}{2}", color=BLACK).next_to(angle, DOWN).shift(0.4*RIGHT + 0.1*UP)
        angle_label[0][1:].shift(0.1*UP)
        angle_label_new1[0][1:].shift(0.1*UP)

        self.play(Create(angle), FadeIn(angle_label), run_time=0.8)
        self.play(AnimationGroup(
            Rotate(dot_right, PI/6, about_point = dot_center.get_center()),
            Rotate(dot_left, -PI/6, about_point = dot_center.get_center()),
            ReplacementTransform(angle_label, angle_label_new1) 
        ))
        self.wait(0.2)

        angle_new = Angle(vec_right, vec_right_copy, radius=0.9, color=BLACK)  
        angle_label_new2 = MathTex(r"\gamma", color=BLACK).move_to(angle_label_new1.get_center()).shift(0.2*UP + 0.2*RIGHT)
        
        self.play(AnimationGroup(
            ReplacementTransform(angle, angle_new),
            ReplacementTransform(angle_label_new1, angle_label_new2),
            VGroup(vec_right, dot_right_copy).animate.set_opacity(1)  
        ))
        
        formula = MathTex(r"\gamma = \frac{1}{2}(\theta - \alpha)", color=BLACK).to_edge(RIGHT)
        formula.shift([0, angle_label_new2.get_bottom()[1] - formula[0][0].get_bottom()[1], 0])

        self.play(AnimationGroup(
            ReplacementTransform(angle_label_new2.copy(), formula[0][0]),
            FadeIn(formula[0][1:]),
            lag_ratio=0.4
        ))
        self.wait(0.2)

        line_left = Line(dot_center.get_center(), dot_left.get_center(), color=BLACK, buff=0.15, stroke_width=6)
        line_right = Line(dot_center.get_center(), dot_right.get_center(), color=BLACK, buff=0.15, stroke_width=6)
        
        labels[0].next_to(dot_left, DOWN)
        labels[1].next_to(dot_right, DOWN)

        self.play(AnimationGroup(
            FadeOut(
                formula, angle_label_new2, vec_vertical, vec_left,
                vec_right,vec_left_copy, vec_right_copy, angle_new, 
                dot_right_copy, dot_left_copy
            ),
            FadeIn(labels, line_left, line_right), 
            lag_ratio = 0.3
        ))
        self.wait(0.4)