# Math-Animation
## Description

The Repository that contains source-code for animations and problems from articles and YouTube channel
## Example from Probability theory

https://github.com/Monotirg/Math-animation/assets/144112818/f50889da-ce8f-47cf-89f9-440de7e04f7e

```python
from manim import *
import numpy as np


class BirthdayProblem(Scene):
    def construct(self):
        max_group = 65
        x, y = [0, 1], [0, 0]
        for i in range(2, max_group):
            prob = 1
            for n in range(i):
                prob *= (365 - n) / 365

            y.extend([y[-1], 1 - prob])
            x.extend([i - 1e-12, i])

        axes = (
            Axes(x_range=[0, max_group, 5], y_range=[0, 1.2, 0.2])
            .scale(0.8)
            .move_to(ORIGIN)
        )

        graph = axes.plot_line_graph(x, y, line_color="#F4BC00", add_vertex_dots=False)
        path = [axes.coords_to_point(xi, yi, 0) for xi, yi in zip(x, y)]

        target_dot = Dot(path[0], color="#005EFF").scale(0.8)
        vertical_line = always_redraw(
            lambda: axes.get_vertical_line(target_dot.get_center())
        )
        label_line = DecimalNumber(
            axes.point_to_coords(target_dot.get_center())[0],
            num_decimal_places=0,
            font_size=20,
        ).next_to(vertical_line, DOWN, buff=0.1)
        label_line.add_updater(lambda mob: mob.next_to(vertical_line, DOWN, buff=0.1))
        label_line.add_updater(
            lambda mob: mob.set_value(axes.point_to_coords(target_dot.get_center())[0])
        )

        number = DecimalNumber(
            axes.point_to_coords(target_dot.get_center())[1],
            num_decimal_places=3,
            font_size=20,
        ).next_to(target_dot, UP, buff=0.1)
        number.add_updater(lambda mob: mob.next_to(target_dot, UP, buff=0.1))
        number.add_updater(
            lambda mob: mob.set_value(axes.point_to_coords(target_dot.get_center())[1])
        )

        self.play(DrawBorderThenFill(axes))
        self.play(Create(graph), run_tim=2)
        self.play(Create(vertical_line), FadeIn(target_dot), FadeIn(number, label_line))

        target_value = np.linspace(1, 0.95 * max_group, 4).astype(int)
        target_run_time = [3] + [1] * (len(target_value) - 3) + [3]
        for i in range(len(target_value) - 1):
            for k in range(2 * target_value[i], 2 * target_value[i + 1]):
                self.play(
                    target_dot.animate.move_to(path[k]),
                    run_time=0.5
                    * target_run_time[i]
                    / (target_value[i + 1] - target_value[i]),
                )
            self.wait(0.5)

        self.wait(0.5)
```


