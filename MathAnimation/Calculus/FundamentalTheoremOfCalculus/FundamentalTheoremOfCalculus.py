from manim import *


class FundamentalTheoremOfCalculus(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 10, 1], 
            y_range=[0, 10, 1],
        ).scale(0.8).set_z_index(4)
        func = lambda x: -5*x**4/288 + 193*x**3/480 - 1049*x**2/360 + 791*x/120 + 4
        func_width = lambda t: -0.0018*t + 0.518
        graph = axes.plot(func, x_range=[0, 9.6], color=YELLOW).set_z_index(2)
    
        rect = VGroup(*[
            axes.get_riemann_rectangles(
                graph, [1, 8], dx=7/k, color="#005EFF", stroke_width=func_width(k), 
                input_sample_type="center", width_scale_factor=1
                ).set_z_index(3) for k in [20, 40, 80, 160, 320]
            ]
        )

        self.play(
            DrawBorderThenFill(axes), 
            run_time=0.5, rate_func=rate_functions.ease_in_out_quad
        )
        self.play(Create(graph), run_time = 0.75)
        self.play(
            DrawBorderThenFill(rect[0],rate_func=smooth), 
            lag_ratio=0.5, run_time=0.6)
        self.wait(1)
        self.play(
            ReplacementTransform(
                rect[0], rect[1], 
                rate_func=rate_functions.ease_in_out_quart, 
                lag_ratio=0.5
            ), 
            run_time=0.6
        )
        self.wait(1)
        for i in range(1,len(rect)-1):
            self.play(
                ReplacementTransform(
                    rect[i], rect[i+1], 
                    rate_func=rate_functions.ease_in_out_quart, 
                    lag_ratio=0.5
                ), 
                run_time=0.6
            )
            
        r = axes.get_area(graph, x_range=[1, 8], color="#005EFF", opacity=0.9, stroke_width=0)
        r.set_z_index(1)
        self.add(r)
        self.play(FadeOut(rect[-1]), lag_ratio=0.5)
        self.wait(2)
