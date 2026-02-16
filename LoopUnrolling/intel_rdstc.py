from manim import *

class showIntrinsic(Scene):
    def construct(self):
        img = ImageMobject("intrinsic.png")
        scale = max(
            config.frame_width / img.width,
            config.frame_height / img.height
        )
        img.scale(scale)
        self.add(img)

        self.wait(3.0)

        rect = Rectangle(width=5, height=0.25, color=YELLOW)
        rect.move_to(img.get_center() + LEFT * 0.42 + DOWN * 1.27)
        self.play(Create(rect))

        self.wait(3.0)
