from manim import *

BACKGROUND_COLOR = WHITE
FOREGROUND_COLOR = BLACK

class Proof(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        # Unbiased estimator text
        unbiased_estimator_text = MathTex(r"\text{Definition of an Unbiased Estimator}") 
        unbiased_estimator_text.set_color(FOREGROUND_COLOR)
        unbiased_estimator_text.to_edge(UP, buff=0.5)
        self.play(Write(unbiased_estimator_text))
        self.wait(2)    

        unbiased_estimator = MathTex(
            r"\mathbb{E}[\hat{\theta}] = \theta"
        )
        unbiased_estimator.set_color(FOREGROUND_COLOR)
        unbiased_estimator.next_to(unbiased_estimator_text, DOWN, buff=0.5)
        self.play(Write(unbiased_estimator))
        self.wait(2)


        self.play(FadeOut(unbiased_estimator_text))
        self.play(FadeOut(unbiased_estimator))
        self.wait(1)

        # Proof lines for 1/n sample covariance
        lines = [
            r"\mathbb{E}[S_n^2] = \mathbb{E}\!\Bigl[\frac{1}{n}\sum_{i=1}^n (X_i - \bar X)^2\Bigr]",
            r"= \frac{1}{n}\sum_{i=1}^n \Bigl(\mathbb{E}[X_i^2] - 2\mathbb{E}[X_i\bar X] + \mathbb{E}[\bar X^2]\Bigr)",
            r"= \frac{1}{n}\sum_{i=1}^n \Bigl(\mathbb{E}[X_i^2] - \frac{2}{n}\sum_{j=1}^n \mathbb{E}[X_i X_j] + \mathbb{E}[\bar X^2]\Bigr)",
            r"= \frac{1}{n}\sum_{i=1}^n \Bigl(\mathbb{E}[X_i^2] - \frac{2}{n}(\mathbb{E}[X_i^2] + \sum_{j\neq i}^{n-1}\mathbb{E}[X_i X_j]) + \mathbb{E}[\bar X^2]\Bigr)",
            r"= \frac{1}{n}\sum_{i=1}^n \Bigl(\sigma^2 + \mu^2 - \frac{2}{n}(\sigma^2 + \mu^2 + (n-1)\mu^2) + \frac{1}{n^2}(n(\sigma^2+\mu^2)+2\frac{n(n-1)}{2}\mu^2)\Bigr)",
            r"= \frac{1}{n}\sum_{i=1}^n \left(\sigma^2 + \mu^2 - \frac{2}{n}(\sigma^2 + n\mu^2) + \frac{1}{n^2}(n\sigma^2 + n\mu^2 + n(n-1)\mu^2)\right)",
            r"= \sigma^2 + \mu^2 - \frac{2}{n}\sigma^2 - 2\mu^2 + \frac{1}{n}\sigma^2 + \mu^2",
            r"= \sigma^2 - \frac{1}{n}\sigma^2",
            r"= \frac{n-1}{n}\sigma^2"
        ]

        proof_lines = []
        left_shift = LEFT * 3.0  # ~20% screen shift to the left
        upper_shift = UP * 0.9  # Shift up to avoid overlap with the top edge

        # First 6 lines (separate lines)
        for i in range(6):
            line = MathTex(lines[i]).scale(0.7).set_color(FOREGROUND_COLOR)
            if i == 0:
                line.to_edge(UP, buff=1)
                line.shift(left_shift)
                line.shift(upper_shift)  # Shift up to avoid overlap with the top edge
            else:
                line.next_to(proof_lines[-1], DOWN, aligned_edge=LEFT)
            self.play(Write(line))
            self.wait(2)
            proof_lines.append(line)

        # From line 6 onward: transform last line
        current_line = proof_lines[-1]
        for line_text in lines[6:]:
            new_line = MathTex(line_text).scale(0.7).set_color(FOREGROUND_COLOR)
            new_line.move_to(current_line)
            self.play(Transform(current_line, new_line))
            self.wait(2)

        # Fadeout the previous lines
        for line in proof_lines:
            self.play(FadeOut(line))
        self.wait(1)

        # Keep final result visible on the left
        final_result = MathTex(r"\mathbb{E}[S_n^2] = \frac{n-1}{n} \sigma^2").scale(0.9).set_color(FOREGROUND_COLOR)
        final_result.to_edge((UP + LEFT)*3.0, buff=0.5)
        self.play(Write(final_result))
        self.wait(2)

        # Animate second proof (n-1 case) to the right
        last_lines = [
            r"\mathbb{E}[S_{n-1}^2]",
            r"= \mathbb{E}\!\Bigl[\tfrac1{n-1}\sum_{i=1}^{n}(X_i - \bar X)^2\Bigr]",
            r"= \tfrac1{n-1}\mathbb{E}\!\Bigl[\sum_{i=1}^{n}(X_i - \bar X)^2\Bigr]",
            r"= \tfrac1{n-1}(n-1)\sigma^2",
            r"= \sigma^2"
        ]

        right_proof = []
        for i, line_text in enumerate(last_lines):
            line = MathTex(line_text).scale(0.7).set_color(FOREGROUND_COLOR)
            if i == 0:
                line.to_edge(UP, buff=1)
                line.shift(RIGHT)  # Shift to the right side
            else:
                line.next_to(right_proof[-1], DOWN, aligned_edge=LEFT)
            self.play(Write(line))
            self.wait(2)
            right_proof.append(line)

        self.wait(3)

        for line in right_proof:
            self.play(FadeOut(line))
        self.wait(1)

        # Final result for n-1 case
        final_result_n_minus_1 = MathTex(r"\mathbb{E}[S_{n-1}^2] = \sigma^2").scale(0.9).set_color(FOREGROUND_COLOR)
        final_result_n_minus_1.to_edge((UP + RIGHT)*3.3, buff=0.5)
        self.play(Write(final_result_n_minus_1))
        self.wait(2)

        # Move final results to the center smoothly
        self.play(
            final_result.animate.move_to(ORIGIN + LEFT * 2.0),
            final_result_n_minus_1.animate.move_to(ORIGIN + RIGHT * 2.0)
        )
        self.wait(2)

        # Add red text above the final result of n case that says "Biased!"
        biased_text = MathTex(r"\text{Biased!}").scale(1.5).set_color(RED)
        biased_text.next_to(final_result, UP*3.5, buff=0.1)
        
        self.play(Write(biased_text))
        
        # Add rectangle around the fraction part
        fraction_rect = SurroundingRectangle(final_result[0][7:12], color=RED, buff=0.05)
        self.play(Create(fraction_rect))
        self.wait(10)
