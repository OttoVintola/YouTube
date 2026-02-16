from manim import *



BACKGROUND_COLOR = "#2d2d2d"
TEXT_COLOR = "#d7d7d7"
WHITE = "#ffffff"
TEXT_FONT = "Monospace"
NUMBER_COLOR = "#b5cea8"

class Highlight(Scene):
    def construct(self):

        self.camera.background_color = BACKGROUND_COLOR

        # 1) Background code image
        code_img = ImageMobject("assm.png")
        scale = max(
            config.frame_width / code_img.width,
            config.frame_height / code_img.height
        )
        code_img.scale(scale)
        self.add(code_img)

        # 2) Hole parameters
        rec_w = config.frame_width * 0.35
        rec_h = 5.0
        rec_center = UP * 1.48 + LEFT * 1 

        # Frame halves
        hw = config.frame_width / 2
        hh = config.frame_height / 2

        # 3) Strip dimensions
        # Get the actual coordinates of the rectangle center
        actual_center_x = rec_center[0]  # This includes the LEFT offset
        actual_center_y = rec_center[1]  # This includes the DOWN offset
        
        top_h    = hh - (actual_center_y + rec_h/2)
        bottom_h = hh + (actual_center_y - rec_h/2)
        left_w   = actual_center_x - rec_w/2 + hw
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

        strips = VGroup(top_strip, bottom_strip)
        # Extra safeguard: remove *any* stroke
        strips.set_stroke(width=0, opacity=0)

        self.wait(10)

        # 5) Fade them all in
        self.play(
            *[s.animate.set_fill(BLACK, 0.8) for s in strips],
            run_time=2.0
        )

        self.wait(4)

        bp = Text("Assembly boilerplate!", font="Monospace", font_size=24, color=TEXT_COLOR)
        bp.move_to(UP + RIGHT * 3.0)
        self.play(Write(bp))

        self.wait(3)
        # Remove the rectangles and text 
        self.play(
            *[s.animate.set_fill(BLACK, 0) for s in strips],
            FadeOut(bp),
            run_time=2.0
        )

        rec_w = config.frame_width * 0.35
        rec_h = 0.45
        rec_center = DOWN * 1.25 + LEFT * 1

        actual_center_x = rec_center[0]  # This includes the LEFT offset
        actual_center_y = rec_center[1]  # This includes the DOWN offset
        
        top_h    = hh - (actual_center_y + rec_h/2)
        bottom_h = hh + (actual_center_y - rec_h/2)
        left_w   = actual_center_x - rec_w/2 + hw
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

        strips = VGroup(top_strip, bottom_strip)

        # Extra safeguard: remove *any* stroke
        strips.set_stroke(width=0, opacity=0)

        # 5) Fade them all in
        self.play(
            *[s.animate.set_fill(BLACK, 0.6) for s in strips],
            run_time=2.0
        )

        self.wait(10)

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

        # MathTex equation at the bottom for j = 5 242 880
        equation = MathTex("\implies j = 5 \cdot 1\\,048\\,576 = 5\\,242\\,880", font_size=32, color="#d7d7d7")
        equation.move_to(DOWN * 2.7 + RIGHT * 3.0)
        self.play(Write(equation), run_time=1.0)
        self.wait(5.0)

        rect = Rectangle(
            width=config.frame_width * 0.45,
            height=config.frame_height * 0.08,
            fill_color=BLACK,
            fill_opacity=0.0,
            stroke_color=YELLOW,
            stroke_width=3
        ).move_to(equation.get_center())
        
        self.play(Create(rect), run_time=1.0)

        self.wait(10.0)

        self.play(
            FadeOut(rect),
            FadeOut(equation),
            run_time=1.0
        )

        # Transform the equation into sum form
        sum_eq = MathTex("\implies j = \sum_{i=1}^{1\\,048\\,576}5 = 5\\,242\\,880", font_size=32, color="#d7d7d7")
        sum_eq.move_to(DOWN * 2.7 + RIGHT * 3.0)
        self.play(Write(sum_eq), run_time=1.0)
        self.wait(5.0)

