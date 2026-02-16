from manim import *

BACKGROUND_COLOR = "#2d2d2d"
TEXT_COLOR = "#d7d7d7"
WHITE = "#ffffff"

class BitShifts(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        # Create squares with "0" labels
        bit_squares = [
            Square(side_length=0.42, fill_color=BACKGROUND_COLOR, fill_opacity=1.0, stroke_color=TEXT_COLOR, stroke_width=3)
            for _ in range(32)
        ]
        
        bit_labels = [
            Text("1" if i == 31 else "0", font_size=24, color=TEXT_COLOR).move_to(square.get_center())
            for i, square in enumerate(bit_squares)
        ]
        
        bits = VGroup(*[VGroup(square, label) for square, label in zip(bit_squares, bit_labels)])
        bits.arrange(RIGHT, buff=0.0).to_edge(ORIGIN)
         
        self.play(
            *[Create(bit) for bit in bits],
            run_time=2.0
        )

        # animate yellow rectangle around last box
        last_square = bit_squares[-1]
        border = SurroundingRectangle(last_square, color=YELLOW, buff=0.0)
        self.play(Create(border), run_time=0.5)

        self.wait(4.0)


        # Write the line of code int n = 1 << 20; on top of the screen
        code = Text("int n = 1 << 20;", font_size=32, color=TEXT_COLOR, font="Monospace")
        code.next_to(bits, UP*2, buff=0.5)
        self.play(Write(code), run_time=1.0)

        # Make the << in the text purple
        shift_text = Text("<<", font_size=32, color=PURPLE, font="Monospace")
        shift_text.move_to(code[6:8].get_center())
        self.play(
            Transform(code[6:8], shift_text),
            run_time=0.5
        )

        self.wait(4.0)
        
        # Perform the bit shift animation 20 times (1 << 20)
        current_position = 31  # Starting position of the "1"
        
        for shift in range(20):
            if current_position > 0:  # Only shift if we haven't reached the leftmost position
                new_position = current_position - 1
                
                # Create new "1" label for the new position
                one_label = Text("1", font_size=24, color=TEXT_COLOR).move_to(bit_squares[new_position].get_center())
                
                # Create new "0" label for the old position
                zero_label = Text("0", font_size=24, color=TEXT_COLOR).move_to(bit_squares[current_position].get_center())
                
                # Create new border around the new position
                new_border = SurroundingRectangle(bit_squares[new_position], color=YELLOW, buff=0.0)
                
                self.play(
                    # Change the bit at new position from "0" to "1"
                    Transform(bit_labels[new_position], one_label),
                    # Move the border to the left
                    Transform(border, new_border),
                    # Change the old position from "1" to "0"
                    Transform(bit_labels[current_position], zero_label),
                    run_time=0.7 # Faster animation for multiple shifts
                )
                
                # Update current position
                current_position = new_position
            else:
                # If we've reached the leftmost position, just shift out (all become 0)
                zero_label = Text("0", font_size=24, color=TEXT_COLOR).move_to(bit_squares[current_position].get_center())
                self.play(
                    Transform(bit_labels[current_position], zero_label),
                    FadeOut(border),  # Remove border when bit shifts out
                    run_time=0.7
                )
                break


        self.wait(2.0)
    
        equation = MathTex("2^{20} = 1\\,048\\,576", font_size=24, color=TEXT_COLOR)
        equation.next_to(bit_squares[11], DOWN, buff=0.3)
        self.play(Write(equation), run_time=1.0)

        self.wait(4.0)
