from manim import *
from os.path import dirname


def per_line(l):
    return np.array([-l[1], l[0], 0]) / np.linalg.norm(l)


class InitCompass(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        dot_left = Dot(color="#0000FF", radius=0.15).shift(1.4 * LEFT + 2.4 * DOWN)
        dot_right = Dot(color="#FF0000", radius=0.15).shift(1.4 * RIGHT + 2.4 * DOWN)
        dot_center = Dot(color="#000000", radius=0.15).shift(2 * UP)

        line_left = always_redraw(
            lambda: Line(
                dot_center.get_center(),
                dot_left.get_center(),
                color=BLACK,
                stroke_width=6,
                z_index=dot_left.get_z_index() - 1,
            )
        )
        line_right = always_redraw(
            lambda: Line(
                dot_center.get_center(),
                dot_right.get_center(),
                color=BLACK,
                stroke_width=6,
                z_index=dot_left.get_z_index() - 1,
            )
        )
        line_radius = always_redraw(
            lambda: Line(
                dot_left.get_center(),
                dot_right.get_right(),
                color=BLACK,
                stroke_width=6,
                z_index=dot_left.get_z_index() - 1,
            )
        )

        label_left = Text("left", color=BLACK).next_to(dot_left, DOWN)
        label_left.add_updater(lambda mobj: mobj.next_to(dot_left, DOWN))
        label_right = Text("right", color=BLACK).next_to(dot_right, DOWN)
        label_right.add_updater(lambda mobj: mobj.next_to(dot_right, DOWN))
        label_center = Text("center", color=BLACK).next_to(dot_center, UP)

        vec_left = (dot_left.get_center() - dot_center.get_center()) / np.linalg.norm(
            dot_left.get_center() - dot_center.get_center()
        )
        vec_right = (dot_right.get_center() - dot_center.get_center()) / np.linalg.norm(
            dot_right.get_center() - dot_center.get_center()
        )
        per_left = per_line(vec_left)

        label_length_left = Text("length", color=BLACK).rotate(
            -np.arctan2(vec_left[1], vec_right[0])
        )
        label_length_left.next_to(vec_left, UP).shift(-per_left)
        label_length_right = Text("length", color=BLACK).rotate(
            np.arctan2(vec_left[1], vec_right[0])
        )
        label_length_right.move_to(
            [-label_length_left.get_center()[0], label_length_left.get_center()[1], 0]
        )
        label_radius = Text("radius", color=BLACK).next_to(line_radius, UP)

        dit_image = dirname(__file__) + "\\image\\"
        compass1 = ImageMobject(dit_image + "\\compass1")
        compass2 = ImageMobject(dit_image + "\\compass2").scale(1.3)
        compass3 = ImageMobject(dit_image + "\\compass3").scale(1.3)
        Group(compass1, compass2, compass3).arrange(RIGHT)
        compass2.move_to(ORIGIN)

        self.add(compass1, compass2, compass3)
        self.wait(0.4)
        self.play(
            AnimationGroup(
                compass1.animate.shift(
                    RIGHT * (compass2.get_center()[0] - compass1.get_center()[0])
                ),
                compass3.animate.shift(
                    RIGHT * (compass2.get_center()[0] - compass3.get_center()[0])
                ),
            )
        )
        self.add(dot_left, dot_right, dot_center)
        self.add(line_left, line_right)
        self.play(FadeOut(compass1, compass2, compass3, shift=UP))
        self.play(FadeIn(label_left, label_right, label_center))
        self.play(FadeIn(label_length_left, label_length_right))
        self.play(FadeIn(line_radius, label_radius))
        self.wait(0.4)
