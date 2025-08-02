from manim import *
import numpy as np

BACKGROUND_COLOR = WHITE
FOREGROUND_COLOR = BLACK

class BiasOfMean(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

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
        self.play(Create(grid))
        
        self.play(Create(axes))
        self.wait(2)


        # Draw contour lines for the normal distribution
        contour_lines = VGroup()
        for level in np.linspace(0.1, 4, 15):
            contour = axes.plot_implicit_curve(
                lambda x, y: np.exp(-0.5 * ((x) ** 2 + (y) ** 2) / (2 ** 2)) - level,
                color=interpolate_color(BLUE, RED, level),
                stroke_width=2
            )
            contour_lines.add(contour)
        self.play(AnimationGroup(*[Create(contour) for contour in contour_lines], lag_ratio=0.1))
        self.wait(2)

        # Add blue dot in origin to denote the mean
        mean_dot = Dot(point=axes.c2p(0, 0), radius=0.1, color=BLUE)
        self.play(FadeIn(mean_dot))
        self.wait(3)

        # Animate a cloud of data points from the normal distribution 
        # with mean at (1, -0.5) and standard deviation of 2
        mean = np.array([1, -0.5])
        std_dev = 2
        np.random.seed(42)
        num_dots = 100
     
        data_points = np.random.normal(loc=mean, scale=std_dev, size=(num_dots, 2))
        dots = VGroup(*[Dot(point=axes.c2p(x, y), radius=0.05, color=BLACK) for x, y in data_points])
        self.play(LaggedStartMap(FadeIn, dots, scale_factor=0.1, lag_ratio=0.1))
        self.wait(10)
        
        # Add red dot at the mean position
        dot_mean_coords = np.mean(data_points, axis=0)  # Calculate mean in mathematical coordinates
        dot_mean = axes.c2p(dot_mean_coords[0], dot_mean_coords[1])
        mean_dot = Dot(dot_mean, color=RED, radius=0.1)
        self.play(FadeIn(mean_dot))
        self.wait(2)

        # Add dashed line from dots to the red mean dot
        dashed_lines = VGroup()
        for dot in dots:
            line = DashedLine(dot.get_center(), mean_dot.get_center(), color=RED, stroke_width=1)
            dashed_lines.add(line)
        self.play(LaggedStartMap(Create, dashed_lines, lag_ratio=0.1))
        self.wait(10)

        # Animate the sample covariance formula at the top left of the screen
        sample_covariance = MathTex(
            r"S_{n-1}^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar X)^2"
        ).scale(0.9).set_color(FOREGROUND_COLOR)
        sample_covariance.to_edge(UP + LEFT, buff=0.5)
        self.play(Write(sample_covariance))
        self.wait(2)

        # make square bracket around the deviations (X_i - \bar X)
        bracket = Brace(sample_covariance[0][17:23], direction=DOWN, color=RED)
        bracket_text = MathTex(r"\text{too small!}").scale(0.7).next_to(bracket, DOWN, buff=0.1).set_color(RED)
        self.play(Create(bracket), Write(bracket_text))
        self.wait(2)

        # Add a blue box around the n-1 term that says compensation
        n_minus_1_box = SurroundingRectangle(
            sample_covariance[0][7:9], 
            color=BLUE, 
            buff=0.02
        )
        n_minus_1_text = MathTex(r"\text{compensation!}").scale(
            0.7
        ).next_to(n_minus_1_box, DOWN, buff=0.1).set_color(BLUE)
        self.play(Create(n_minus_1_box), Write(n_minus_1_text))
        self.wait(5)




