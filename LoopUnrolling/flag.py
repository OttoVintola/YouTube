from manim import *

BACKGROUND_COLOR = "#2d2d2d"
TEXT_COLOR = "#d7d7d7"
WHITE = "#ffffff"
TEXT_FONT = "Monospace"
NUMBER_COLOR = "#b5cea8"
VAR_COLOR = "#569cd6"

class Flags(Scene):
    def construct(self):
        code_img = ImageMobject("flags.png")
        scale = max(
            config.frame_width / code_img.width,
            config.frame_height / code_img.height
        )
        code_img.scale(scale)
        self.add(code_img)

        self.wait(5)

        rec_pos = DOWN * 1.25 + LEFT * 4.1
        rect = Rectangle(
            width=config.frame_width * 0.08,
            height=config.frame_height * 0.025,
            fill_color=BLACK,
            fill_opacity=0.0,
            stroke_color=YELLOW,
            stroke_width=3
        ).move_to(rec_pos)

        self.play(Create(rect), run_time=1.0)

        self.wait(5)

        expl_text = Text("Flow-sensitive TREE-level\nConditional Constant Propagation", font_size=24, font=TEXT_FONT, color=BACKGROUND_COLOR)
        expl_text.next_to(rect, RIGHT*3.5)
        self.play(Write(expl_text), run_time=1.0)

        self.wait(10)



class Explanation(Scene):
    def construct(self):

        self.camera.background_color = BACKGROUND_COLOR

        compiler_text = Text("clang -O1 loop.c -o loop", font_size=24, font=TEXT_FONT, color=TEXT_COLOR)
        compiler_text.move_to(UP*3.0)
        self.play(Write(compiler_text), run_time=1.0)

        self.wait(3)

        # Make a vertical vector annotated by brackets [ . . . -ftree-ccp . . . ] (include the dots inside)
        dot1 = Text(".", font_size=16, font=TEXT_FONT, color=TEXT_COLOR)
        dot2 = Text(".", font_size=16, font=TEXT_FONT, color=TEXT_COLOR)
        dot3 = Text(".", font_size=16, font=TEXT_FONT, color=TEXT_COLOR)
        dot4 = Text(".", font_size=16, font=TEXT_FONT, color=TEXT_COLOR)
        dot5 = Text(".", font_size=16, font=TEXT_FONT, color=TEXT_COLOR)
        dot6 = Text(".", font_size=16, font=TEXT_FONT, color=TEXT_COLOR)

        ccp_text = Text("-ftree-ccp", font_size=16, font=TEXT_FONT, color=YELLOW)

        # Position the brackets and dots
        dot1.next_to(compiler_text, DOWN)
        dot2.next_to(dot1, DOWN)
        dot3.next_to(dot2, DOWN)
        ccp_text.next_to(dot3, DOWN)
        dot4.next_to(ccp_text, DOWN)
        dot5.next_to(dot4, DOWN)
        dot6.next_to(dot5, DOWN)

        # Group all elements and shift left
        vector_group = VGroup(dot1, dot2, dot3, ccp_text, dot4, dot5, dot6)
        vector_group.shift(LEFT * 0.8 + DOWN * 0.1)  # Adjust the value as needed

        brace_left = Brace(vector_group, direction=LEFT, buff=0.1)
        brace_right = Brace(vector_group, direction=RIGHT, buff=0.1)

        # Create the vector
        self.play(Write(brace_left), Write(dot1), Write(dot2), Write(dot3), Write(ccp_text), Write(dot4), Write(dot5), Write(dot6), Write(brace_right), run_time=1.0)

        self.wait(3)

        int_expr = MarkupText(
            f'<span fgcolor="{VAR_COLOR}">int</span><span fgcolor="{TEXT_COLOR}"> x =</span>',
            font_size=24, 
            font=TEXT_FONT
        )
        int_expr.move_to(DOWN + LEFT)
        self.play(Write(int_expr), run_time=1.0)
        
        self.wait(2)

        # Create just the "2 + 5" part to replace
        old_expr = MarkupText(
            f'<span fgcolor="{NUMBER_COLOR}">2</span><span fgcolor="{TEXT_COLOR}"> + </span><span fgcolor="{NUMBER_COLOR}">5</span><span fgcolor="{TEXT_COLOR}">;</span>',
            font_size=24, 
            font=TEXT_FONT
        )
        new_expr = MarkupText(
            f'<span fgcolor="{NUMBER_COLOR}">7</span><span fgcolor="{TEXT_COLOR}">;</span>',
            font_size=24, 
            font=TEXT_FONT
        )
        
        # Position the expressions to align with the original expression
        old_expr.move_to(DOWN*1.03 + RIGHT*0.5)
        self.play(Write(old_expr), run_time=1.0)
        self.wait(3)

        new_expr.move_to(DOWN*1.03 + RIGHT*0.01)
        self.play(Transform(old_expr, new_expr), run_time=1.0)

        self.wait(3)

        self.play(FadeOut(old_expr), run_time=1.0)
        self.play(FadeOut(int_expr), run_time=1.0)


        code_img = ImageMobject("loop.png")
        scale = max(
            config.frame_width / (code_img.width*1.5),
            config.frame_height / (code_img.height*1.5)
        )
        code_img.scale(scale)
        code_img.move_to(DOWN*1.03)
        self.play(FadeIn(code_img), run_time=0.3)

        self.wait(5)
        self.play(FadeOut(code_img), run_time=0.3)

        replacement = MarkupText(
            f'<span fgcolor="{VAR_COLOR}">int</span><span fgcolor="{TEXT_COLOR}"> j </span>=',
            font_size=24,
            font=TEXT_FONT
        )
        replacement.move_to(DOWN + LEFT)
        self.play(Write(replacement), run_time=1.0)

        to_be_replaced = MarkupText(
            f'<span fgcolor="{NUMBER_COLOR}">5</span> + <span fgcolor="{NUMBER_COLOR}">5</span> + ... + <span fgcolor="{NUMBER_COLOR}">5</span>;',
            font_size=24,
            font=TEXT_FONT
        )
        to_be_replaced.move_to(DOWN*1.00+ RIGHT*1.5)
        self.play(Write(to_be_replaced), run_time=1.0)

        self.wait(4)

        replacement_expr = MarkupText(
            f'<span fgcolor="{NUMBER_COLOR}">5 242 880</span>;',
            font_size=24,
            font=TEXT_FONT
        )
        replacement_expr.move_to(DOWN*1.00+ RIGHT*0.9)
        self.play(Transform(to_be_replaced, replacement_expr), run_time=1.0)

        self.wait(10)
