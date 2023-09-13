from manim import *


class IntermediateValueTheorem(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-5, 60, 10],
        ).scale(0.8)
        func = (
            lambda x: (x**3) * 11 / 10
            - (x**2) * 58 / 5
            + x * 301 / 10
            - 73 / 5
            + 25
        )
        graph = axes.plot(func, x_range=[0, 7.2], color=YELLOW)

        x_min = 116 / 33 + (3523**0.5) / 33
        x_max = 116 / 33 - (3523**0.5) / 33
        dot_min = Dot(axes.coords_to_point(x_min, func(x_min)), color="#FF0000")
        dot_max = Dot(axes.coords_to_point(x_max, func(x_max)), color="#FF0000")

        line_min = axes.get_lines_to_point(axes.c2p(x_min, func(x_min)))
        line_min.set_z_index(dot_min.get_z_index() - 1)
        line_max = axes.get_lines_to_point(axes.c2p(x_max, func(x_max)))
        line_max.set_z_index(dot_max.get_z_index() - 1)
        label_b = MathTex("a", font_size=40).move_to(line_min[1].get_bottom())
        label_b.shift(0.3 * DOWN)
        label_a = MathTex("b", font_size=40).move_to(line_max[1].get_bottom())
        label_a.align_to(label_b, DOWN)
        label_B = MathTex("A", font_size=40).move_to(line_min[0].get_left())
        label_B.shift(0.3 * LEFT)
        label_A = MathTex("B", font_size=40).move_to(line_max[0].get_left())
        label_A.align_to(label_B, LEFT)

        t = ValueTracker(x_max)
        initial_point = [axes.coords_to_point(t.get_value(), func(t.get_value()))]
        dot = Dot(point=initial_point, color="#005EFF")
        dot.add_updater(
            lambda x: x.move_to(axes.c2p(t.get_value(), func(t.get_value())))
        )

        vertical_line = always_redraw(
            lambda: axes.get_vertical_line(axes.c2p(t.get_value(), func(t.get_value())))
        ).set_z_index(line_max.get_z_index())
        horizontal_line = always_redraw(
            lambda: axes.get_horizontal_line(
                axes.c2p(t.get_value(), func(t.get_value()))
            )
        ).set_z_index(line_max.get_z_index())
        label_c = MathTex("c", font_size=40)
        label_C = MathTex("C", font_size=40)
        label_c.add_updater(
            lambda item: item.move_to(vertical_line.get_bottom()).shift(0.3 * DOWN)
        )
        label_C.add_updater(
            lambda item: item.move_to(horizontal_line.get_left()).shift(0.3 * LEFT)
        )

        self.play(
            DrawBorderThenFill(axes),
            run_time=0.5,
            rate_func=rate_functions.ease_in_out_quad,
        )
        self.play(Create(graph), run_time=0.754)
        self.play(FadeIn(label_a, label_b), run_time=0.75)
        self.play(Create(line_min[1]), Create(line_max[1]), run_time=0.7)
        self.play(FadeIn(dot_min, dot_max), run_time=0.5)
        self.play(
            Create(line_min[0].rotate(PI)), Create(line_max[0].rotate(PI)), run_time=0.5
        )
        self.play(FadeIn(label_A, label_B), run_time=0.75)
        self.play(Create(vertical_line), Create(horizontal_line), run_time=0.5)
        self.play(
            FadeIn(dot, label_c, label_C),
            FadeOut(label_a, label_b, label_A, label_B),
            run_time=0.75,
        )
        self.play(t.animate.set_value(x_min), run_time=1.2)
        self.play(t.animate.set_value(0.5 * (x_min + x_max)), run_time=1)
        self.play(FadeIn(label_a, label_b, label_A, label_B), run_time=0.5)
        self.wait(1)
