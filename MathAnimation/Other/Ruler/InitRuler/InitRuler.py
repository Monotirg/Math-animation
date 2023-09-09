from manim import *
from Ruler import *

class InitRuler(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        ruler = create_ruler(8, 1, 8, 9)
        ruler.scale(1.3)
        
        dots_side = VGroup(*[
            Dot(dot, color=BLACK) for dot in ruler[0].get_vertex_groups()[0]
        ])
        dots_div_start = VGroup(*[
            Dot(line.get_start(), color="#0000FF") for line in ruler[1]
        ])
        dots_div_end = VGroup(*[
            Dot(line.get_end(), color="#FF0000") for line in ruler[1]
        ])
        dots_div = VGroup(*[
            VGroup(d1, d2) for d1, d2 in zip(dots_div_start, dots_div_end)
        ])
        dots_subdiv_start = VGroup(*[
            Dot(line.get_start(), color="#0000FF") for line in ruler[2]
        ])
        dots_subdiv_end = VGroup(*[
            Dot(line.get_end(), color="#FF0000") for line in ruler[2]
        ])
        dots_subdiv = VGroup(*[
            VGroup(d1, d2) for d1, d2 in zip(dots_subdiv_start, dots_subdiv_end)
        ])
        
        
        self.add(ruler)
        self.wait(0.4)
        self.play(AnimationGroup(
            *[FadeIn(dot, shift = DOWN) for dot in dots_side], 
            run_time = 0.8
        ))
        self.play(AnimationGroup(
            *[FadeIn(dot, shift = DOWN) for dot in dots_div], 
            lag_ratio = 0.3
            ), 
            run_time = 2, rate_func = rate_functions.smooth
        )
        self.play(AnimationGroup(
            *[FadeIn(dot, shift = DOWN) for dot in dots_subdiv], 
            lag_ratio = 0.3
            ), 
            run_time = 4, rate_func = rate_functions.smooth
        )
        self.wait(0.4)