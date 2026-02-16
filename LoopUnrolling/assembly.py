from manim import *

BACKGROUND_COLOR = "#2d2d2d"
TEXT_COLOR = "#d7d7d7"
WHITE = "#ffffff"
TEXT_FONT = "Monospace"
NUMBER_COLOR = "#b5cea8"


class assembly(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        # Create a code image
        code_img = ImageMobject("output-16by9.png")
        scale = max(
            config.frame_width / code_img.width,
            config.frame_height / code_img.height
        )
        code_img.scale(scale)
        self.add(code_img)

        self.wait(5.0)

        # make the image split screen vertically with smooth animation
        self.play(
            code_img.animate.set_width(config.frame_width / 2).move_to(LEFT * config.frame_width / 4),
            run_time=1.5,
            rate_func=smooth
        )

        self.wait(5.0)

        # Write C code on the left side above the code
        c_code = Text("C", font_size=24, color=TEXT_COLOR, font=TEXT_FONT)
        c_code.next_to(code_img, UP, buff=0.1)
        self.play(Write(c_code), run_time=1.0)


        # Write assembly code on the right side above the code
        asm_code = Text("MIPS Pseudo-instructions", font_size=24, color=TEXT_COLOR, font=TEXT_FONT)
        asm_code.move_to(RIGHT * config.frame_width / 4 + UP*2.2)
        self.play(Write(asm_code), run_time=1.0)

        loading_ints = Text("LOAD:\n li $t0, 0\n li $t1, 1048576\n li $t2, 0", font_size=14, color=TEXT_COLOR, font=TEXT_FONT, line_spacing=1.5)
        # Make the $t0 and $t1 registers more visible
        loading_ints[7:10].set_color(BLUE)
        loading_ints[14:17].set_color(BLUE)
        loading_ints[27:30].set_color(BLUE)

        loading_ints[11:12].set_color(NUMBER_COLOR)
        loading_ints[17:25].set_color(NUMBER_COLOR)
        loading_ints[31:33].set_color(NUMBER_COLOR)

        # Move loading ints under Pseudo-instructions
        loading_ints.next_to(asm_code, DOWN, buff=0.5)
        self.play(Write(loading_ints), run_time=1.0)

        self.wait(5.0)

        check_loop = Text("CHECK:\n cmp $t0, $t1\n bge $t0, $t1, END", font_size=14, color=TEXT_COLOR, font=TEXT_FONT, line_spacing=1.5)
        check_loop.next_to(loading_ints, DOWN, buff=0.5)
        check_loop[9:12].set_color(BLUE)
        check_loop[13:16].set_color(BLUE)
        check_loop[19:22].set_color(BLUE)
        check_loop[23:26].set_color(BLUE)
        self.play(Write(check_loop), run_time=1.0)

        self.wait(5.0)

        for_loop = Text("LOOP:\n addi $t2, $t2, 5\n addi $t0, $t0, 1\nCHECK", font_size=14, color=TEXT_COLOR, font=TEXT_FONT, line_spacing=1.5)
        for_loop.next_to(check_loop, DOWN, buff=0.5)
        for_loop[9:12].set_color(BLUE)
        for_loop[13:16].set_color(BLUE)
        for_loop[22:25].set_color(BLUE)
        for_loop[26:29].set_color(BLUE)

        for_loop[17:18].set_color(NUMBER_COLOR)
        for_loop[30:31].set_color(NUMBER_COLOR)
        self.play(Write(for_loop), run_time=1.0)

        self.wait(5.0)

        end = Text("END:\n ret", font_size=14, color=TEXT_COLOR, font=TEXT_FONT, line_spacing=1.5)
        end.next_to(for_loop, DOWN, buff=0.5)
        end.shift(LEFT*0.65)
        self.play(Write(end), run_time=1.0)

        self.wait(5.0)

        cmp_rectangle = Rectangle(width=1.5, height=0.5, color=YELLOW)
        cmp_rectangle.move_to(check_loop[10:13].get_center())
        self.play(Create(cmp_rectangle), run_time=1.0)

        addi_rectangle = Rectangle(width=2.0, height=0.8, color=YELLOW)
        addi_rectangle.move_to(for_loop[9:12].get_center() + DOWN * 0.2 + RIGHT * 0.15)
        self.play(Create(addi_rectangle), run_time=1.0)

        # Make braces around the right side to encapsulate the rectangles
        brace = Brace(VGroup(cmp_rectangle, addi_rectangle), direction=LEFT, stroke_width=1.0, color=YELLOW)
        self.play(Create(brace), run_time=1.0)

        self.wait(2.0) 
        symbol = Text("≈", font="Monospace", font_size=24, color=TEXT_COLOR)
        instruction_text = Text("3 or more instructions\nper iteration", font="Monospace", font_size=16, color=TEXT_COLOR)
        instruction_text.next_to(brace, LEFT*2.5)
        symbol.next_to(instruction_text, RIGHT)
        self.play(Write(symbol), Write(instruction_text), run_time=1.0)

        self.wait(5.0)

        conclusion_text = Text("In total around\n3 million instructions", font="Monospace", font_size=16, color=TEXT_COLOR)
        conclusion_text.next_to(instruction_text, DOWN)
        self.play(Write(conclusion_text), run_time=1.0)

        self.wait(5.0)

