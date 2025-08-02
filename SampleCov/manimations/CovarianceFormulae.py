from manim import *


class CovarianceFormulae(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Big question mark in the beginning
        question_mark = Text("?", color=BLACK).scale(5).move_to(ORIGIN)

        # Population covariance label and formula
        population_label = Text("Population", color=BLACK).scale(0.8)
        population_formula = MathTex(
            r"\mathrm{Cov}(X, Y) = \sum_{i=1}^n \frac{(x_i - \bar{x})(y_i - \bar{y})}{n}",
            color=BLACK
        )
        
        # Sample covariance label and formula
        sample_label = Text("Sample", color=BLACK).scale(0.8)
        sample_formula = MathTex(
            r"\mathrm{Cov}(X, Y) = \sum_{i=1}^n \frac{(x_i - \bar{x})(y_i - \bar{y})}{n-1}",
            color=BLACK
        )
        
        # Group population elements
        population_group = VGroup(population_label, population_formula).arrange(DOWN, buff=0.3)
        
        # Group sample elements
        sample_group = VGroup(sample_label, sample_formula).arrange(DOWN, buff=0.3)
        
        # Arrange both groups vertically - population on top, sample below
        all_formulas = VGroup(population_group, sample_group).arrange(DOWN, buff=1)
        all_formulas.move_to(ORIGIN)

        # Display the question mark
        self.play(Write(question_mark))
        self.wait(10)

        # Fade out the question mark
        self.play(FadeOut(question_mark))
        
        self.play(Write(population_label))
        self.wait(3)
        self.play(Write(population_formula))
        self.wait(10)
        self.play(Write(sample_label))
        self.wait(3)
        self.play(Write(sample_formula))
        self.wait(5)
        
        # Create circles to highlight the n and n-1 terms
        # Circle for population formula 'n' term (denominator)
        population_circle = Circle(radius=0.35, color=BLUE).move_to(population_formula[0][-1])
        
        # Circle for sample formula 'n-1' term (denominator)
        sample_circle = Ellipse(width=1.75, height=0.65, color=BLUE).move_to(sample_formula[0][-3:])
        
        # Animate the circles
        self.play(Create(population_circle))
        self.play(Create(sample_circle))
        self.wait(3)
        self.play(FadeOut(population_circle), FadeOut(sample_circle))
        self.wait(2)


        