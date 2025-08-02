from manim import *

BACKGROUND_COLOR = WHITE
FOREGROUND_COLOR = BLACK

class DegreeFormulae(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        sample_covariance = MathTex(r"\frac{1}{n-1}\mathbb{E}\left[\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})\right] = 0")
        sample_covariance.set_color(FOREGROUND_COLOR)
        sample_covariance.to_edge(UP, buff=0.5)  
        self.play(Write(sample_covariance))
        self.wait(2)

        expanded_formula = MathTex(
            r"\frac{1}{n-1}\mathbb{E} \left[ (x_1 - \bar{x})(y_1 - \bar{y}) + (x_2 - \bar{x})(y_2 - \bar{y}) + \right.", 
            r"\left. (x_3 - \bar{x})(y_3 - \bar{y}) + (x_4 - \bar{x})(y_4 - \bar{y}) \right] = 0"
        )
        expanded_formula.set_color(FOREGROUND_COLOR)
        expanded_formula.arrange(DOWN, center=False, aligned_edge=LEFT)
        expanded_formula.next_to(sample_covariance, DOWN, buff=0.5)
        self.play(Write(expanded_formula))
        self.wait(2)

        self.play(FadeOut(sample_covariance))
        self.wait(2)

        # Step 1: Apply linearity of expectation
        linearity_formula = MathTex(
            r"\frac{1}{n-1}\left[ \mathbb{E}[(x_1 - \bar{x})(y_1 - \bar{y})] + \mathbb{E}[(x_2 - \bar{x})(y_2 - \bar{y})] + \right.", 
            r"\left. \mathbb{E}[(x_3 - \bar{x})(y_3 - \bar{y})] + \mathbb{E}[(x_4 - \bar{x})(y_4 - \bar{y})] \right] = 0"
        )
        linearity_formula.set_color(FOREGROUND_COLOR)
        linearity_formula.arrange(DOWN, center=False, aligned_edge=LEFT)
        linearity_formula.move_to(expanded_formula.get_center())
        
        # Animate the transformation
        self.play(Transform(expanded_formula, linearity_formula))
        self.wait(2)

        # Step 2: Highlight the term we want to move
        highlight_box = SurroundingRectangle(
            linearity_formula[1][-20:-2],  # Highlight the last term
            color=RED,
            buff=0.1
        )
        self.play(Create(highlight_box))
        self.wait(1)

        # Step 3: Move the highlighted term to the other side
        moved_formula = MathTex(
            r"\frac{1}{n-1}\left[ \mathbb{E}[(x_1 - \bar{x})(y_1 - \bar{y})] + \mathbb{E}[(x_2 - \bar{x})(y_2 - \bar{y})] + \right.", 
            r"\left. \mathbb{E}[(x_3 - \bar{x})(y_3 - \bar{y})] \right] = -\mathbb{E}[(x_4 - \bar{x})(y_4 - \bar{y})]"
        )
        moved_formula.set_color(FOREGROUND_COLOR)
        moved_formula.arrange(DOWN, center=False, aligned_edge=LEFT)
        moved_formula.move_to(expanded_formula.get_center())

        # Animate the movement
        self.play(
            FadeOut(highlight_box),
            Transform(expanded_formula, moved_formula)
        )
        self.wait(10)

        # Black box around the RHS
        # Create a separate MathTex for the RHS term to ensure proper targeting
        rhs_term = MathTex(r"-\mathbb{E}[(x_4 - \bar{x})(y_4 - \bar{y})]")
        rhs_term.set_color(FOREGROUND_COLOR)
        rhs_term.move_to(moved_formula[1].get_right() + LEFT * 2.1)  # Position it roughly where the RHS is
        
        rhs_box = SurroundingRectangle(
            rhs_term,
            color=BLACK,
            fill_color=BLACK,
            fill_opacity=1.0,
            buff=0.1
        )
        self.play(Create(rhs_box))
        self.wait(10)


        line0 = expanded_formula[0]
        line1 = expanded_formula[1]
        term1 = line0[12:14]
        term2 = line0[19:21]
        term3 = line0[30:32]
        term5 = line0[37:39]
        term6 = line1[7:9]
        term7 = line1[14:16]

        three = VGroup(term1, term2, term3, term5, term6, term7)

        # 3) Apply a tiny up‑and‑down “lift” using there_and_back
        from manim.utils.rate_functions import there_and_back
        from manim.animation.transform import ApplyMethod

        self.play(
            ApplyMethod(three.shift, UP * 0.1,
                        rate_func=there_and_back,
                        run_time=4.0),
            lag_ratio=0.1
        )
        self.wait(5)





        




