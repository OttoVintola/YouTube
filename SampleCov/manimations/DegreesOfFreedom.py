from manim import *
import numpy as np

num_dots: int = 4

class DegreesOfFreedom(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Create aligned grid and axes that fill the entire screen
        x_range = [-16, 16, 1]
        y_range = [-9, 9, 1]
        
        # Make grid fill the screen
        grid = NumberPlane(
            x_range=x_range,
            y_range=y_range,
            x_length=14,  # Full width to cover the screen
            y_length=8,   # Full height to cover the screen
            background_line_style={
                "stroke_color": GREY_A,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        )

        # Make Axes with same dimensions and no tips
        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=14,
            y_length=8,
            axis_config={
                "color": BLACK,
                "stroke_width": 2,
                "include_ticks": True,
                "tick_size": 0.1,
                "include_tip": False  # Remove arrow tips
            }
        )
        
        # Add axis labels
        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN, buff=0.5)
        y_label = axes.get_y_axis_label("y", edge=UP, direction=LEFT, buff=0.5)
        x_label.set_color(BLACK)
        y_label.set_color(BLACK)

        # Animation sequence
        self.play(Create(grid), run_time=2)
        self.wait(0.5)
        
        self.play(Create(axes), run_time=5)
        self.wait(0.5)
        
        self.play(
            Write(x_label),
            Write(y_label),
            run_time=1.5
        )
        self.wait(1)
        
        # Define dot positions
        dot_positions = [
            (8, 6),   # RED
            (5, 5),   # BLUE
            (10, 3),  # GREEN
            (6, 1),   # PURPLE
        ]
        
        colors = [BLACK] * num_dots
        
        dots = [
            Dot(axes.coords_to_point(x, y), color=color)
            for (x, y), color in zip(dot_positions, colors)
        ]

        # Animate dots appearing
        self.play(*[GrowFromCenter(dot) for dot in dots], run_time=1.5)
        self.wait(5)
        

        # Make a red dot at the mean position
        dot_mean_coords = np.mean(dot_positions, axis=0)  # Calculate mean in mathematical coordinates
        dot_mean = axes.coords_to_point(dot_mean_coords[0], dot_mean_coords[1])  # Convert to screen coordinates
        mean_dot = Dot(dot_mean, color=RED, radius=0.1)
        self.play(FadeIn(mean_dot))
        self.wait(2)
        
        # Add an arrow from the origin to the mean dot
        mean_arrow = Arrow(axes.coords_to_point(0, 0), axes.coords_to_point(dot_mean_coords[0], dot_mean_coords[1]), color=RED, buff=0, stroke_width=4)
        self.play(
            GrowArrow(mean_arrow),
            run_time=1.5
        )
        self.wait(2)

        # Create initial vectors from origin to dot positions
        initial_vectors = [
            Arrow(
                axes.coords_to_point(dot_mean_coords[0], dot_mean_coords[1]), 
                axes.coords_to_point(x, y), 
                color=color, 
                buff=0, 
                stroke_width=4
            )
            for (x, y), color in zip(dot_positions, colors)
        ]

        # Animate initial vectors appearing
        self.play(*[GrowArrow(vector) for vector in initial_vectors], run_time=1.5)
        self.wait(5)

        # Define final vector endpoints (the target vectors)
        final_endpoints = [
            (1, 2),   # RED
            (-2, 1),  # BLUE
            (3, -1),  # GREEN
            (-1, -3), # PURPLE
        ]
        
        # Create the final vectors
        final_vectors = [
            Arrow(
                axes.coords_to_point(0, 0), 
                axes.coords_to_point(x, y), 
                color=color, 
                buff=0, 
                stroke_width=4
            )
            for (x, y), color in zip(final_endpoints, colors)
        ]
        
        self.play(FadeOut(mean_dot), run_time=1)
        self.play(*[FadeOut(dot) for dot in dots], run_time=1)
        self.wait(1)

        # Use a more explicit approach to control the color of specific parts
        formula = MathTex(
            "\\frac{1}{n-1}",
            "\\mathbb{E}\\left[",
            "\\sum_{i=1}^{n}",
            "(",
            "x_i",
            "-",
            "\\bar{x}",
            ")",
            "(",
            "y_i",
            "-",
            "\\bar{y}",
            ")",
            "\\right]"
        )
        # Color the means in red
        formula.set_color(BLACK)
        formula.set_color_by_tex("\\bar{x}", RED)
        formula.set_color_by_tex("\\bar{y}", RED)
        
        # Animate writing the formula
        formula.to_corner(UL, buff=0.5)
        self.play(Write(formula))
        self.wait(5)



        # Animate transformation of vectors to their final positions
        self.play(
            *[Transform(initial_vector, final_vector) 
              for initial_vector, final_vector in zip(initial_vectors, final_vectors)],
            run_time=2.5
        )
        self.wait(1)
        self.play(FadeOut(mean_arrow), run_time=1)

        # Add = 0 to the formula
        equals_zero = MathTex("= 0")
        equals_zero.set_color(BLACK)  # Set color to BLACK to be visible on white background
        equals_zero.next_to(formula, DOWN, buff=0.3)  # Use DOWN instead of BOTTOM for alignment
        self.play(Write(equals_zero))
        self.wait(5)


