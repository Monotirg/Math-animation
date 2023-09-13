from manim import *
from Dice import create_dice
import numpy as np


class DiceAverage(Scene):
    def construct(self):
        np.random.seed(1004)
        dice_value = np.random.randint(1, 7, size=(5, 7))
        dice = VGroup(
            *[
                VGroup(*[create_dice(val, 0.75, 0.2) for val in dice_value[i]]).arrange(
                    RIGHT, buff=0.2
                )
                for i in range(dice_value.shape[0])
            ]
        )
        cumsum_mean = np.array(
            [val / (i + 1) for i, val in enumerate(np.cumsum(dice_value))]
        )
        cumsum.reshape((dice_value.shape[0], -1))

        axes = Axes(
            x_range=[0, dice_value.shape[0] * dice_value.shape[1] + 2, 1],
            y_range=[0, 7, 1],
        ).scale(0.8)
        VGroup(axes, dice).arrange(DOWN, buff=1).move_to(ORIGIN)
        graph = axes.plot_line_graph(
            np.arange(1, dice_value.shape[1] + 1),
            cumsum_mean[0],
            add_vertex_dots=False,
            line_color="#FDE910",
        )

        self.play(DrawBorderThenFill(axes))
        self.play(
            AnimationGroup(
                AnimationGroup(
                    *[GrowFromPoint(d, [d.get_bottom()[0], -5, 0]) for d in dice[0]],
                    lag_ratio=0.2
                ),
                Create(graph),
                lag_ratio=0.85,
            )
        )

        for i in range(1, dice_value.shape[0]):
            graph = axes.plot_line_graph(
                np.arange(
                    i * dice_value.shape[1] - 1, (i + 1) * dice_value.shape[1] + 1
                ),
                np.append(cumsum_mean[i - 1, -2:], cumsum_mean[i]),
                add_vertex_dots=False,
                line_color="#FDE910",
            )
            self.play(
                AnimationGroup(
                    AnimationGroup(
                        *[
                            GrowFromPoint(d, [d.get_bottom()[0], -5, 0])
                            for d in dice[i]
                        ],
                        lag_ratio=0.2
                    ),
                    Create(graph),
                    lag_ratio=0.75,
                    run_time=0.75,
                )
            )

        graph = axes.get_lines_to_point(
            axes.c2p(dice_value.shape[0] * dice_value.shape[1] + 1, 3.5)
        )
        graph = graph[0]
        label = MathTex("3.5", font_size=24).move_to(graph.get_left()).shift(0.3 * LEFT)
        self.play(Create(graph), FadeIn(label), run_time=0.75)
        self.wait(1)
