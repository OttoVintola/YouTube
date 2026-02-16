from manim import *

class HighlightLine(Scene):
    def construct(self):
        # 1) Background code image
        code_img = ImageMobject("output-16by9.png")
        scale = max(
            config.frame_width / code_img.width,
            config.frame_height / code_img.height
        )
        code_img.scale(scale)
        self.add(code_img)

        self.wait(10)

        # 2) Hole parameters
        rec_w = config.frame_width * 0.45
        rec_h = 0.45
        rec_center = UP * 1.2

        # Frame halves
        hw = config.frame_width / 2
        hh = config.frame_height / 2

        # 3) Strip dimensions
        top_h    = hh - (rec_center[1] + rec_h/2)
        bottom_h = hh + (rec_center[1] - rec_h/2)
        left_w   = rec_center[0] - rec_w/2 + hw
        right_w  = config.frame_width - (left_w + rec_w)

        # 4) Build strips with no stroke at all
        top_strip = Rectangle(
            width=config.frame_width,
            height=top_h,
            fill_color=BLACK,
            fill_opacity=0.0,
            stroke_width=0,
            stroke_opacity=0
        ).move_to(UP * (hh - top_h/2))

        bottom_strip = Rectangle(
            width=config.frame_width,
            height=bottom_h,
            fill_color=BLACK,
            fill_opacity=0.0,
            stroke_width=0,
            stroke_opacity=0
        ).move_to(DOWN * (hh - bottom_h/2))

        left_strip = Rectangle(
            width=left_w,
            height=rec_h,
            fill_color=BLACK,
            fill_opacity=0.0,
            stroke_width=0,
            stroke_opacity=0
        ).move_to(LEFT * (hw - left_w/2) + rec_center)

        right_strip = Rectangle(
            width=right_w,
            height=rec_h,
            fill_color=BLACK,
            fill_opacity=0.0,
            stroke_width=0,
            stroke_opacity=0
        ).move_to(RIGHT * (hw - right_w/2) + rec_center)

        strips = VGroup(top_strip, bottom_strip, left_strip, right_strip)
        # Extra safeguard: remove *any* stroke
        strips.set_stroke(width=0, opacity=0)

        # 5) Fade them all in
        self.play(
            *[s.animate.set_fill(BLACK, 0.6) for s in strips],
            run_time=2.0
        )

        # 6) Yellow border around the hole
        border = Rectangle(
            width=rec_w,
            height=rec_h,
            stroke_color=YELLOW,
            stroke_width=4,
            fill_opacity=0
        ).move_to(rec_center)
        self.play(Create(border), run_time=0.5)

        self.wait(4)
