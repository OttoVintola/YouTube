from manim import *

class HighlightIncrement(Scene):
    def construct(self):
        # 1) Background code image
        code_img = ImageMobject("output-16by9.png")
        scale = max(
            config.frame_width / code_img.width,
            config.frame_height / code_img.height
        )
        code_img.scale(scale)
        self.add(code_img)


        # 2) Bounding rectangle around the variable j and the increment operation
        rec_w = config.frame_width * 0.15
        rec_h = config.frame_height * 0.08

        bounding_rect = Rectangle(
            width=rec_w,
            height=rec_h,
            fill_color=BLACK,
            fill_opacity=0.0,
            stroke_color=YELLOW,
            stroke_width=3
        ).move_to(UP * 0.7 + LEFT * 2.1)

        self.play(Create(bounding_rect), run_time=1.0)

        self.wait(3.0)
        

        # 3) Highlight the increment operation
        rec_w = config.frame_width * 0.11
        rec_h = config.frame_height * 0.08

        increment_rect = Rectangle(
            width=rec_w,
            height=rec_h,
            fill_color=BLACK,
            fill_opacity=0.0,
            stroke_color=YELLOW,
            stroke_width=3
        ).move_to(DOWN * 0.8+ LEFT * 1.6)

        self.play(Create(increment_rect), run_time=1.0)

        self.wait(6.0)


        # MathTex equation at the bottom for j = 5 242 880
        equation = MathTex("\implies j = 5 \cdot 1\\,048\\,576 = 5\\,242\\,880", font_size=32, color="#d7d7d7")
        equation.move_to(DOWN * 2.7 + RIGHT * 3.0)
        self.play(Write(equation), run_time=1.0)
        self.wait(5.0)