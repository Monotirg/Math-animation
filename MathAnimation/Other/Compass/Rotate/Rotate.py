from manim import *


class RotateCompass(ZoomedScene):
    def construct(self):
        self.camera.background_color = WHITE

        line_x = Line([-6.5, -1, 0], [6.5, -1, 0], color=BLACK, stroke_width=5)
        line_x.add_tip(tip_length=0.25, tip_width=0.25)
        line_y = Line([-2, -3.5, 0], [-2, 3.5, 0], color=BLACK, stroke_width=5)
        line_y.add_tip(tip_length=0.25, tip_width=0.25)
        axes = VGroup(line_x, line_y)

        dot_left = Dot(color="#0000FF", radius=0.15).shift(1.4 * LEFT + 2.4 * DOWN)
        dot_right = Dot(color="#FF0000", radius=0.15).shift(1.4 * RIGHT + 2.4 * DOWN)
        dot_center = Dot(color="#000000", radius=0.15).shift(2 * UP)

        label_left = Text("left", color=BLACK).next_to(dot_left, DOWN)
        label_right = Text("right", color=BLACK).next_to(dot_right, DOWN)
        label_center = Text("center", color=BLACK).next_to(dot_center, UP)

        line_left = Line(
            dot_center.get_center(), dot_left.get_center(), buff=0.15, color=BLACK
        )
        line_right = Line(
            dot_center.get_center(), dot_right.get_center(), buff=0.15, color=BLACK
        )

        compass = VGroup(dot_left, dot_right, dot_center)
        labels = VGroup(label_left, label_right, label_center)
        lines = VGroup(line_left, line_right)

        compass_labels = VGroup(compass, labels, lines)
        compass_labels.scale(0.5).shift(2 * UP + 2 * RIGHT)

        vec_shift = Line(
            dot_center.get_center(), np.array([-2, -1, 0]), color=BLACK, stroke_width=4
        )
        vec_shift.add_tip(tip_length=0.25, tip_width=0.25)
        vec_shift_reverse = Line(
            np.array([-2, -1, 0]), dot_center.get_center(), color=BLACK, stroke_width=4
        )
        vec_shift_reverse.add_tip(tip_length=0.25, tip_width=0.25)

        rot_mat = Matrix(
            [[r"\cos{\alpha}", r"-\sin{\alpha}"], [r"\sin{\alpha}", r"\cos{\alpha}"]],
            left_bracket="(",
            right_bracket=")",
            bracket_h_buff=0.1,
            h_buff=2,
        ).set_column_colors(BLACK, BLACK)
        rot_mat.get_brackets()[0].set_color(BLACK)
        rot_mat.get_brackets()[1].set_color(BLACK)
        rot_mat.scale(0.8)

        self.camera.frame.save_state()
        self.camera.frame.scale(0.5).move_to(compass.get_center())

        self.add(compass_labels)
        self.wait(0.4)
        self.play(FadeOut(labels), run_time=0.8)
        self.play(Restore(self.camera.frame))
        self.play(DrawBorderThenFill(axes), run_time=1.2)
        self.play(DrawBorderThenFill(vec_shift), run_time=1.2)
        self.play(
            AnimationGroup(
                VGroup(compass, lines).animate.shift(
                    -compass_labels[0][2].get_center() + np.array([-2, -1, 0])
                ),
                FadeOut(vec_shift),
            ),
            run_time=1.2,
        )
        self.play(FadeIn(rot_mat), run_time=0.8)
        self.play(
            AnimationGroup(
                ReplacementTransform(rot_mat, dot_center),
                Rotate(
                    VGroup(compass, lines),
                    angle=2 * PI / 7,
                    about_point=dot_center.get_center(),
                ),
                lag_ratio=0.5,
            ),
            run_time=1.2,
        )
        self.play(DrawBorderThenFill(vec_shift_reverse), run_time=1.2)
        self.play(
            AnimationGroup(
                VGroup(compass, lines).animate.shift(
                    -compass_labels[0][2].get_center() + vec_shift_reverse.get_end()
                ),
                FadeOut(vec_shift_reverse),
            ),
            run_time=1.2,
        )

        label_left.next_to(dot_left, DOWN)
        label_right.next_to(dot_right, DOWN)
        label_center.next_to(dot_center, UP)

        self.play(
            self.camera.frame.animate.scale(0.5).move_to(compass.get_center()),
            run_time=1.2,
        )
        self.play(FadeIn(labels), run_time=0.8)
        self.wait(0.4)
