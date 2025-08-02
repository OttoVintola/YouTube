from manim import *

BACKGROUND_COLOR = WHITE
FOREGROUND_COLOR = BLACK

class First_Intertitle(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        # Make a list indexed by numbers that has 
        # 1. Proof
        # 2. Graphical Representation of (Possible) Sample Bias and Compensation
        
        items = VGroup(
            Text("1. Proof", font_size=36, color=FOREGROUND_COLOR),
            Text("2. Graphical Representation", 
                 font_size=36, color=FOREGROUND_COLOR)
        )
        
        items.arrange(DOWN, aligned_edge=LEFT, buff=0.8)
        items.center()
        
        for item in items:
            self.play(Write(item))
            self.wait(0.5)
        
        self.wait(2)

        # Animate blue rectangle around the first item
        rect1 = SurroundingRectangle(items[0], color=BLUE, buff=0.1)
        self.play(Create(rect1))
        self.wait(1)

        # Fade out the items and rectangle
        self.play(FadeOut(items), FadeOut(rect1))
        self.wait(1)
        
