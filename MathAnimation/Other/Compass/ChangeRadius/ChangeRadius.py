from manim import *


class ChangeRadius(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        dot_left = Dot(color="#0000FF", radius=0.15).shift(2 * LEFT)
        dot_right = Dot(color="#FF0000", radius=0.15).shift(2 * RIGHT)
        dot_center = Dot(color="#000000", radius=0.15).shift(2 * UP)
        dot_right_new = Dot(color="#FF0000", radius=0.15).shift(4 * RIGHT + 2.4 * DOWN)
        dot_mid = Dot(color="#000000", radius=0.15).move_to(1.3 * RIGHT + 2.4 * DOWN)
        dot_center_new = Dot(color="#000000", radius=0.15)

        label_left = Text("left", color=BLACK).next_to(dot_left, DOWN)
        label_right = Text("right", color=BLACK).next_to(dot_right, DOWN)
        label_center = Text("center", color=BLACK).next_to(dot_center, UP)

        line_left_start = always_redraw(
            lambda: Line(
                dot_center.get_center(),
                dot_left.get_center(),
                color=BLACK,
                stroke_width=6,
                z_index=dot_left.get_z_index() - 1,
            )
        )
        line_right_start = always_redraw(
            lambda: Line(
                dot_center.get_center(),
                dot_right.get_center(),
                color=BLACK,
                stroke_width=6,
                z_index=dot_left.get_z_index() - 1,
            )
        )

        length = np.linalg.norm(dot_center.get_center() - dot_left.get_center())
        radius = np.linalg.norm(dot_left.get_center() - dot_right_new.get_center())
        h = (length**2 - 0.25 * radius**2) ** 0.5
        center_new_coords = 0.5 * (
            dot_left.get_center() + dot_right_new.get_center()
        ) + h * np.array([0, 1, 0])
        dot_center_new.move_to(center_new_coords)

        vec_radius = always_redraw(
            lambda: Line(
                dot_left.get_center(),
                dot_right.get_center(),
                color=BLACK,
                buff=0.15,
                stroke_width=6,
            ).add_tip(tip_length=0.25, tip_width=0.25)
        )
        vec_sum1 = Line(
            dot_left.get_center(),
            dot_right_new.get_center(),
            buff=0.15,
            color=BLACK,
            stroke_width=6,
        ).set_z_index(-1000)
        vec_sum2 = Line(
            0.5 * (dot_right_new.get_center() + dot_left.get_center()),
            0.5 * (dot_right_new.get_center() + dot_left.get_center()) + [0, 1, 0],
            color=BLACK,
            stroke_width=6,
        ).add_tip(tip_length=0.25, tip_width=0.25)
        vec_sum3 = Line(
            0.5 * (dot_right_new.get_center() + dot_left.get_center()),
            dot_center_new.get_center() - [0, 0.15, 0],
            color=BLACK,
            stroke_width=6,
        ).add_tip(tip_length=0.25, tip_width=0.25)

        line_left = Line(
            dot_left.get_center(),
            dot_center_new.get_center(),
            color=BLACK,
            buff=0.15,
            stroke_width=6,
        ).set_z_index(-1000)

        label_height = MathTex(r"\vec{h}", color=BLACK).next_to(vec_sum3, LEFT, buff=0)
        label_l = MathTex("l", color=BLACK).next_to(line_left, LEFT).shift(RIGHT)
        label_r = MathTex("r", color=BLACK)
        height_formula = (
            MathTex(r"|\vec{h}| = \sqrt{l^2 - \frac{r^2}{4}}", color=BLACK)
            .to_edge(LEFT)
            .shift(RIGHT)
        )

        self.add(dot_left, dot_right, dot_center, line_left_start)
        self.add(label_left, label_right, label_center, line_right_start)
        self.wait(0.4)
        self.play(
            FadeOut(
                label_left, label_right, label_center, line_left_start, line_right_start
            ),
            run_time=0.8,
        )

        label_right.next_to(dot_right_new, DOWN)
        label_center.next_to(dot_center_new, UP)

        self.play(GrowFromPoint(vec_radius, vec_radius.get_start()), run_time=1)
        self.play(dot_right.animate.move_to(dot_right_new.get_center()))

        label_r.next_to(vec_radius, DOWN)

        self.play(FadeOut(vec_radius), run_time=0.8)
        self.play(FadeOut(dot_center), run_time=0.8)
        self.play(Create(vec_sum1), run_time=1.2)
        self.play(FadeIn(dot_mid), run_time=0.8)
        self.play(GrowFromPoint(vec_sum2, vec_sum2.get_start()), run_time=1.2)
        self.play(ReplacementTransform(vec_sum2, vec_sum3), run_time=1.2)
        self.play(
            Create(line_left),
            FadeIn(label_l, label_height, label_r, dot_center_new),
            run_time=0.8,
        )
        self.play(
            AnimationGroup(
                AnimationGroup(
                    ReplacementTransform(label_height.copy(), height_formula[0][1:3]),
                    ReplacementTransform(label_l.copy(), height_formula[0][7]),
                    ReplacementTransform(label_r.copy(), height_formula[0][10]),
                ),
                FadeIn(
                    height_formula[0][0],
                    height_formula[0][3:7],
                    height_formula[0][8:10],
                    height_formula[0][11:],
                ),
                lag_ratio=0.4,
            )
        )
        self.wait(0.2)

        line_right_start = Line(
            dot_center_new.get_center(),
            dot_left.get_center(),
            color=BLACK,
            stroke_width=6,
            buff=0.15,
        )
        line_left_start = Line(
            dot_center_new.get_center(),
            dot_right.get_center(),
            color=BLACK,
            stroke_width=6,
            buff=0.15,
        )

        self.play(
            AnimationGroup(
                FadeOut(
                    vec_sum1,
                    vec_sum3,
                    dot_mid,
                    height_formula,
                    label_r,
                    label_height,
                    label_l,
                    line_left,
                ),
                FadeIn(
                    label_left,
                    label_right,
                    label_center,
                    line_left_start,
                    line_right_start,
                ),
                lag_ratio=0.3,
            )
        )
        self.wait(0.4)
