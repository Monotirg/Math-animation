from manim import *


class PseudoscalarProduct(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        product = MathTex(r"a \vee  b = ", color=BLACK)
        product_val = DecimalNumber(6.12, font_size=42, color=BLACK)
        product_val.next_to(product, RIGHT).align_to(product, DOWN)
        product_label = VGroup(product, product_val)
        
        vec1 = Vector([4,0,0], color=BLACK)
        vec2 = Vector([4,0,0], color=BLACK)
        vec2.rotate(PI/8, about_point = vec1.get_start())
        vec = VGroup(vec1,vec2)

        def f_product():
            v1 = vec1.get_end() - vec1.get_start()
            v2 = vec2.get_end() - vec2.get_start()
            return v1[0]*v2[1] - v1[1]*v2[0]

        f_always(product_val.set_value, f_product)
        VGroup(product_label, vec).arrange(DOWN, buff=1)
        
        label_a = MathTex("a", color=BLACK).next_to(vec1, DOWN, buff=0)
        label_b  = MathTex("b", color=BLACK).next_to(vec2.get_center(), UP, buff=0.25)
        label_b.add_updater(
            lambda mobj: label_b.next_to(vec2.get_center(), UP, buff=0.25)
        )      
        
        self.add(product_val, product)
        self.add(vec1,vec2)
        self.add(label_a, label_b)
        self.wait(0.4)
        self.play(Rotate(vec2, -PI/3, about_point=vec2.get_start()), run_time=1.5)
        self.play(Rotate(vec2, -PI + PI/3, about_point=vec2.get_start()), run_time=1)
        self.play(Rotate(vec2, -PI/3, about_point=vec2.get_start()), run_time=1.5)
        self.play(Rotate(vec2,  -PI + PI/3, about_point=vec2.get_start()), run_time=1)
        self.wait(0.4)