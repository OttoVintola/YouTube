from manim import *

BACKGROUND_COLOR = "#2d2d2d"
TEXT_COLOR = "#d7d7d7"
WHITE = "#ffffff"

class question(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR


        question = Text("What will the wall-clock time be?", color=TEXT_COLOR, font_size=36, font = "Monospace")
        question.move_to(UP * 2.0)
        self.add(question)

        # A multiple choice question
        optionA = "17 milliseconds"
        optionB = "3 milliseconds"
        optionC = "7.5 nanoseconds"
        optionD = "0.2 seconds"

        options = [optionA, optionB, optionC, optionD]

        # Render an equally idented list of characters A), B), C) and D) all in the color yellow
        letters = ["A)", "B)", "C)", "D)"]
        letter_text_A = Text("A)", color=YELLOW, font_size=24, font="Monospace")
        letter_text_A.move_to(UP * 0.5 + LEFT * 2.5)
        self.add(letter_text_A)

        option_text_A = Text(optionA, color=TEXT_COLOR, font_size=24, font="Monospace")
        option_text_A.move_to(UP * 0.5 + LEFT * 0.5)
        self.add(option_text_A)

        letter_text_B = Text("B)", color=YELLOW, font_size=24, font="Monospace")
        letter_text_B.move_to(UP * 0.0 + LEFT * 2.5)
        self.add(letter_text_B)

        option_text_B = Text(optionB, color=TEXT_COLOR, font_size=24, font="Monospace")
        option_text_B.move_to(UP * 0.0 + LEFT * 0.5)
        self.add(option_text_B)

        letter_text_C = Text("C)", color=YELLOW, font_size=24, font="Monospace")
        letter_text_C.move_to(UP * -0.5 + LEFT * 2.5)
        self.add(letter_text_C)

        option_text_C = Text(optionC, color=TEXT_COLOR, font_size=24, font="Monospace")
        option_text_C.move_to(UP * -0.5 + LEFT * 0.5)
        self.add(option_text_C)

        letter_text_D = Text("D)", color=YELLOW, font_size=24, font="Monospace")
        letter_text_D.move_to(UP * -1.0 + LEFT * 2.5)
        self.add(letter_text_D)

        option_text_D = Text(optionD, color=TEXT_COLOR, font_size=24, font="Monospace")
        option_text_D.move_to(UP * -1.0 + LEFT * 0.5)
        self.add(option_text_D)

        self.wait(5.0)

        # Fade out B and D at the same time
        self.play(FadeOut(option_text_B), FadeOut(option_text_D), FadeOut(letter_text_B), FadeOut(letter_text_D), run_time=0.5)
        self.wait(3.5)

        A_cycles = Text("≈ 4 million clock cycles", color=TEXT_COLOR, font_size=24, font = "Monospace")
        A_cycles.move_to(option_text_A.get_center() + RIGHT * 4.2)


        C_cycles = Text("≈ 20 clock cycles", color=TEXT_COLOR, font_size=24, font="Monospace")
        C_cycles.move_to(option_text_C.get_center() + RIGHT * 3.5)

        self.play(Write(A_cycles), Write(C_cycles), run_time=1.0)

        self.wait(7.0)