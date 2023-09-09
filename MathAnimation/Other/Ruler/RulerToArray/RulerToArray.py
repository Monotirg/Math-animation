from manim import *
from Ruler import *


class RulerToArray(ZoomedScene):
    def construct(self):    
        self.camera.background_color = WHITE
        
        div, subdiv = 2, 4
        ruler = create_ruler(4, 0.5, div, subdiv)
        count = div + (div-1)*subdiv
        step = 0.375

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

        ruler_dots = VGroup(ruler, dots_div, dots_subdiv, dots_side)
        ruler_dots_copy = ruler_dots.copy().rotate(-PI/2)

        square_dot_black = VGroup(
            Square(step, fill_color="#4868B2", fill_opacity=1), 
            Dot(ORIGIN, color="#000000")
        )
        square_dot_black[1].set_z_index(square_dot_black[0].get_z_index()+1)
        square_dot_black[1].move_to(square_dot_black[0].get_center())
        
        square_dot_blue = square_dot_black.copy()
        square_dot_blue[1].set_color("#0000FF")
        square_dot_red = square_dot_black.copy()
        square_dot_red[1].set_color("#FF0000")

        arr_dots_side1 = VGroup(*[square_dot_black.copy() for _ in range(4)])
        arr_dots_side1.arrange(DOWN, buff=0)
        arr_dots_side2 = VGroup(arr_dots_side1.copy(), arr_dots_side1.copy())
        arr_dots_side2.arrange(RIGHT, buff=0)

        arr_dots_div1 = VGroup()
        for _ in range(div):
            arr_dots_div1.add(square_dot_blue.copy())
            arr_dots_div1.add(square_dot_red.copy())
        
        arr_dots_subdiv1 = VGroup()
        for _ in range(subdiv):
            arr_dots_subdiv1.add(square_dot_blue.copy())
            arr_dots_subdiv1.add(square_dot_red.copy())

        arr_dots_div1.arrange(DOWN, buff=0)
        arr_dots_subdiv1.arrange(DOWN, buff=0)
        
        arr_dots_div2 = VGroup(arr_dots_div1.copy(),arr_dots_div1.copy())
        arr_dots_div2.arrange(RIGHT, buff=0)
        arr_dots_subdiv2 = VGroup(
            arr_dots_subdiv1.copy(),
            arr_dots_subdiv1.copy()
        )
        arr_dots_subdiv2.arrange(RIGHT, buff=0)
        
        arr = VGroup(
            arr_dots_side2,
            arr_dots_div2, 
            arr_dots_subdiv2
        ).arrange(RIGHT, buff=1.25)
        arr_dots_side2.align_to(arr_dots_subdiv2, UP)
        arr_dots_div2.align_to(arr_dots_subdiv2, UP)

        VGroup(ruler_dots_copy, arr).arrange(RIGHT, buff=2)
        
        arr_dots_side1.move_to(arr_dots_side2[0].get_center())
        arr_dots_div1.move_to(arr_dots_div2[0].get_center())
        arr_dots_subdiv1.move_to(arr_dots_subdiv2[0].get_center())

        ruler_dots_copy.set_z_index(1000000)

        symb_x = MathTex("x", color=BLACK, font_size=16)
        symb_x.move_to(arr_dots_side1[0][1].get_bottom())
        symb_x.shift(0.1*RIGHT)
        symb_y = MathTex("y", color=BLACK, font_size=16)
        symb_y.move_to(arr_dots_side2[1][0][1].get_bottom())
        symb_y.shift(0.1*RIGHT)

        arr1_lab = VGroup()
        for i in range(len(arr_dots_side2)):
            for j in range(len(arr_dots_side2[i])):
                temp = symb_x.copy() if i == 0 else symb_y.copy()
                temp.move_to(arr_dots_side2[i][j][1].get_bottom())
                temp.shift(0.1*RIGHT)
                arr1_lab.add(temp)
        
        arr2_lab = VGroup()
        for i in range(len(arr_dots_div2)):
            for j in range(len(arr_dots_div2[i])):
                temp = symb_x.copy() if i == 0 else symb_y.copy()
                temp.move_to(arr_dots_div2[i][j][1].get_bottom())
                temp.shift(0.1*RIGHT)
                arr1_lab.add(temp)

        arr3_lab = VGroup()
        for i in range(len(arr_dots_subdiv2)):
            for j in range(len(arr_dots_subdiv2[i])):
                temp = symb_x.copy() if i == 0 else symb_y.copy()
                temp.move_to(arr_dots_subdiv2[i][j][1].get_bottom())
                temp.shift(0.1*RIGHT)
                arr1_lab.add(temp)
        
        label_dots_shape = Tex("shape", color=BLACK, font_size=32)
        label_dots_shape.next_to(arr_dots_side2[0], UP)
        label_dots_div = Tex("division", color = BLACK, font_size=32)
        label_dots_div.next_to(arr_dots_div2[0], UP)
        label_dots_subdiv = Tex("subdivision", color=BLACK, font_size=32)
        label_dots_subdiv.next_to(arr_dots_subdiv2[0], UP)

        label_dots_shape2 = label_dots_shape.copy()
        label_dots_shape2.next_to(arr_dots_side2, UP)
        label_dots_div2 = label_dots_div.copy()
        label_dots_div2.next_to(arr_dots_div2, UP)
        label_dots_subdiv2 = label_dots_subdiv.copy()
        label_dots_subdiv2.next_to(arr_dots_subdiv2, UP)

        self.camera.frame.scale(0.6)
        self.add(ruler)
        self.wait(0.4)
        self.play(FadeIn(dots_side, shift=DOWN), lag_ratio=0.2)
        self.play(
            FadeIn(ruler_dots[1][0],ruler_dots[1:-1], ruler_dots[1][1], shift=DOWN), 
            lag_ratio=0.2, run_time=1.1
        )
        self.play(ReplacementTransform(ruler_dots, ruler_dots_copy))

        square  = VGroup(*[item[0] for item in arr_dots_side1])
        dots = VGroup(*[item[1] for item in arr_dots_side1])

        self.play(FadeIn(square, label_dots_shape))
        self.play(ReplacementTransform(ruler_dots_copy[-1], dots, path_arc=1))

        square1  = VGroup(*[item[0] for item in arr_dots_div1])
        dots1 = VGroup(*[item[1] for item in arr_dots_div1])
        square2  = VGroup(*[item[0] for item in arr_dots_subdiv1])
        dots2 = VGroup(*[item[1] for item in arr_dots_subdiv1])

        self.play(FadeIn(square1, square2, label_dots_div, label_dots_subdiv))
        self.play(Succession(
            ReplacementTransform(ruler_dots_copy[1], dots1, path_arc=1),
            ReplacementTransform(ruler_dots_copy[2], dots2, path_arc=1)
        ))
        self.play(AnimationGroup(
            AnimationGroup(
            ReplacementTransform(label_dots_shape,label_dots_shape2),
            ReplacementTransform(label_dots_div,label_dots_div2),
            ReplacementTransform(label_dots_subdiv,label_dots_subdiv2),
            ReplacementTransform(arr_dots_side1.copy(),arr_dots_side2[1]),
            ReplacementTransform(arr_dots_div1.copy(),arr_dots_div2[1]),
            ReplacementTransform(arr_dots_subdiv1.copy(),arr_dots_subdiv2[1]) 
            ),
            FadeIn(arr1_lab, arr2_lab, arr3_lab),
            lag_ratio = 0.3
        ))
        self.wait(1)
