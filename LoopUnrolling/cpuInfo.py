from manim import *

BACKGROUND_COLOR = "#2d2d2d"
TEXT_COLOR = "#d7d7d7"
WHITE = "#ffffff"

class showCPU(Scene):
    def construct(self):
        code_img = ImageMobject("cpuInfo.jpg")
        scale = max(
            config.frame_width / code_img.width,
            config.frame_height / code_img.height
        )
        code_img.scale(scale)
        self.add(code_img)

        self.wait(5.0)

        rec_w = config.frame_width * 0.35
        rec_h = config.frame_height * 0.05
        rec_x = DOWN * 3.35
        rec_y = LEFT * 0.15

        bounding_rect = Rectangle(
            width=rec_w,
            height=rec_h,
            fill_color=BLACK,
            fill_opacity=0.0,
            stroke_color=YELLOW,
            stroke_width=3
        ).move_to(rec_x + rec_y)

        self.play(Create(bounding_rect), run_time=1.0)

        self.wait(3.0)




