from manim import *


def create_dice(
    count: int,
    size: float,
    radius: float,
    color_dice: color = WHITE,
    color_circle: color = BLACK,
) -> VGroup:
    dice = VGroup()
    dice_shape = RoundedRectangle(
        width=size,
        height=size,
        corner_radius=radius,
        color=BLACK,
        fill_color=color_dice,
        fill_opacity=1,
    )
    dot_dice = [
        Circle(
            radius=size / 12, stroke_width=0, fill_color=color_circle, fill_opacity=1
        )
        for _ in range(count)
    ]
    dice.add(dice_shape, *dot_dice)

    match count:
        case 1:
            dot_dice[0].move_to(dice_shape.get_center())
        case 2:
            dot_dice[0].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_left()
                    + dice_shape.get_bottom()
                )
            )
            dot_dice[1].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_right()
                    + dice_shape.get_top()
                )
            )
        case 3:
            dot_dice[0].move_to(dice_shape.get_center())
            dot_dice[1].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_left()
                    + dice_shape.get_bottom()
                )
            )
            dot_dice[2].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_right()
                    + dice_shape.get_top()
                )
            )
        case 4:
            dot_dice[0].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_left()
                    + dice_shape.get_top()
                )
            )
            dot_dice[1].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_right()
                    + dice_shape.get_top()
                )
            )
            dot_dice[2].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_left()
                    + dice_shape.get_bottom()
                )
            )
            dot_dice[3].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_right()
                    + dice_shape.get_bottom()
                )
            )
        case 5:
            dot_dice[0].move_to(dice_shape.get_center())
            dot_dice[1].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_left()
                    + dice_shape.get_top()
                )
            )
            dot_dice[2].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_right()
                    + dice_shape.get_top()
                )
            )
            dot_dice[3].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_left()
                    + dice_shape.get_bottom()
                )
            )
            dot_dice[4].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_right()
                    + dice_shape.get_bottom()
                )
            )
        case _:
            dot_dice[0].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_left()
                    + dice_shape.get_top()
                )
            )
            dot_dice[1].move_to(0.5 * (dice_shape.get_center() + dice_shape.get_left()))
            dot_dice[2].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_left()
                    + dice_shape.get_bottom()
                )
            )
            dot_dice[3].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_right()
                    + dice_shape.get_top()
                )
            )
            dot_dice[4].move_to(
                0.5 * (dice_shape.get_center() + dice_shape.get_right())
            )
            dot_dice[5].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_right()
                    + dice_shape.get_bottom()
                )
            )

    return dice
