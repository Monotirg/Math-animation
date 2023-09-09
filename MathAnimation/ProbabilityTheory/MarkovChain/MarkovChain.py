from manim import *

class MarkovChain(Scene):
    def construct(self):
        vertex1 = Circle(
            radius=0.5, color="#E5E5E5", 
            fill_color="#E5E5E5", fill_opacity=1
        )
        vertex2, vertex3, vertex4 = [vertex1.copy() for _ in range(3)]
        top_vertex = VGroup(vertex1,vertex2).arrange(RIGHT, buff=3)
        bot_vertex = VGroup(vertex3,vertex4).arrange(RIGHT, buff=3)
        vertex = VGroup(top_vertex,bot_vertex).arrange(DOWN, buff=1.5)
        
        arrow_color = YELLOW
        arrow12 = Arrow(
            vertex1.get_center(), vertex2.get_center(), 
            color=arrow_color, buff=0.5
        ).shift(0.15*UP)
        arrow13 = Arrow(
            vertex1.get_center(), vertex3.get_center(), 
            color=arrow_color, buff=0.5
        ).shift(0.15*RIGHT)
        arrow21 = Arrow(
            vertex2.get_center(), vertex1.get_center(), 
            color=arrow_color, buff=0.5
        ).shift(0.15*DOWN)
        arrow23 = Arrow(
            vertex2.get_center(), vertex3.get_center(), 
            color=arrow_color, buff=0.5
        )
        arrow31 = Arrow(
            vertex3.get_center(), vertex1.get_center(), 
            color=arrow_color, buff=0.5
        ).shift(0.15*LEFT)
        arrow34 = Arrow(
            vertex3.get_center(), vertex4.get_center(), 
            color=arrow_color, buff=0.5
        )
        arrow42 = Arrow(
            vertex4.get_center(), vertex2.get_center(), 
            color=arrow_color, buff=0.5
        )
       
        label12 = MathTex("0.3", font_size=40, color=WHITE)
        label12.move_to(arrow12.get_center()).shift(0.3*UP)
        label13 = MathTex("0.7", font_size=40, color=WHITE)
        label13.move_to(arrow13.get_center()).shift(0.4*RIGHT)
        label21 = MathTex("0.8", font_size=40, color=WHITE)
        label21.move_to(arrow21.get_center()).shift(0.3*DOWN)
        label23 = MathTex("0.2", font_size=40, color=WHITE)
        label23.move_to(arrow23.get_center()).shift(0.3*DOWN+0.1*RIGHT)
        label31 = MathTex("0.5", font_size=40, color=WHITE)
        label31.move_to(arrow31.get_center()).shift(0.4*LEFT)
        label34 = MathTex("0.5", font_size=40, color=WHITE)
        label34.move_to(arrow34.get_center()).shift(0.3*DOWN)
        label42 = MathTex("1", font_size=40, color=WHITE)
        label42.move_to(arrow42.get_center()).shift(0.2*RIGHT)

        res1 = MathTex("0.334", font_size=40, color=WHITE)
        res1.move_to(vertex1.get_top()).shift(0.3*UP)
        res2 = MathTex("0.242", font_size=40, color=WHITE)
        res2.move_to(vertex2.get_top()).shift(0.3*UP)
        res3 = MathTex("0.283", font_size=40, color=WHITE)
        res3.move_to(vertex3.get_bottom()).shift(0.3*DOWN)
        res4 = MathTex("0.141", font_size=40, color=WHITE)
        res4.move_to(vertex4.get_bottom()).shift(0.3*DOWN)
        
        all_arrow = VGroup(arrow12, arrow21, arrow13, arrow23, arrow31, arrow34, arrow42)
        all_label = VGroup(label12, label13, label21, label23, label31, label34, label42)
        
        target_vertex = Circle(
            radius=0.5, color=YELLOW, 
            fill_color=YELLOW, fill_opacity=1
        ).move_to(vertex1.get_center())

        self.play(DrawBorderThenFill(vertex), run_time = 0.85)
        self.play(DrawBorderThenFill(all_arrow), FadeIn(all_label))
        self.play(DrawBorderThenFill(target_vertex), run_time = 0.85)
        
        self.wait(0.25) 
        self.play(target_vertex.animate.move_to(vertex2.get_center()), run_time=0.75)
        self.play(target_vertex.animate.move_to(vertex3.get_center()), run_time=0.75)
        self.play(target_vertex.animate.move_to(vertex4.get_center()), run_time=0.75)
        self.play(target_vertex.animate.move_to(vertex2.get_center()), run_time=0.75)
        self.play(target_vertex.animate.move_to(vertex1.get_center()), run_time=0.75)
        self.play(FadeOut(all_label))
        self.play(
            target_vertex.animate.move_to(vertex3.get_center()),
            FadeIn(res3),lag_ratio=0.8, 
            run_time=0.75
        )
        self.play(
            target_vertex.animate.move_to(vertex4.get_center()),
            FadeIn(res4),
            lag_ratio=0.8, run_time=0.75
        )
        self.play(
            target_vertex.animate.move_to(vertex2.get_center()),
            FadeIn(res2),
            lag_ratio=0.8, run_time=0.75
        )
        self.play(
            target_vertex.animate.move_to(vertex1.get_center()),
            FadeIn(res1),
            lag_ratio=0.8, run_time=0.75
        )
        self.wait(0.25)
