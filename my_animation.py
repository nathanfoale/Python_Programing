from manim import *

class MyFirstScene(Scene):
    def construct(self):
        plane = ComplexPlane().scale(1.5)
        self.play(Create(plane))
        text = Text("Hello, and welcome to this video on Euler's Identity,\n"
        "where will will bring together the worlds of algebra,\n"
        "trigonometry and complex analysis!", font_size=40, color=YELLOW).to_edge(UP).shift(DOWN*1)
       
        self.play(Write(text))
        self.wait(3)


class EulersIdentity(Scene):
    def construct(self):
        # Display Euler's Identity
        equation = MathTex("e^{i\pi} + 1 = 0", font_size=60, color=BLUE)
        equation.to_edge(UP)

        # Display the question
        question1 = Text("What is this mysterious equation?", font_size=35)
        question1.next_to(equation, DOWN, buff=1.25)
        
        question2 = Text("What is e? and how can you raise it to an imaginary number?", font_size=35)
        question2.next_to(question1, DOWN, buff=1.25)

        question3 = Text("What is an imaginary number?", font_size=35)
        question3.next_to(question2, DOWN, buff=1.25)

        # Animate
        self.play(Write(equation))
        
        # Add a pause
        self.wait(2)

        # Animate the questions

        self.play(FadeIn(question1))

        self.wait(2)

        self.play(FadeIn(question2))

        self.wait(2)

        self.play(FadeIn(question3))
        self.wait(3)

class EulersHook(Scene):
    def construct(self):
        # Create a complex plane
        plane = ComplexPlane().scale(1.5)
        self.play(Create(plane))

        # Draw a circle of radius 1 (unit circle)
        circle = Circle(radius=1.5).set_color(WHITE)
        self.play(Create(circle))
        self.wait(1)

        # Function to get moving point
        def moving_point(t):
            return np.exp(1j * TAU * t)

        dot = Dot(plane.number_to_point(moving_point(0)), color=RED)
        line = Line(plane.c2p(0,0), dot.get_center(), color=RED)
        label = MathTex("e^{i\\theta}").next_to(dot, RIGHT, buff=0.2)
        
        self.add(dot, line, label)

        text = MathTex(r"\text{How is it that } e, \pi, \text{and imaginary numbers are so deeply connected?}", font_size=50).scale(0.8).move_to(UP * 2.5)
        text1 = Text("Let's first explore the realm of complex numbers", font_size=40).move_to(DOWN*2.5)

        self.play(Write(text))

        def update_dot(mob, alpha):
            theta = interpolate(0, TAU, alpha)
            z_value = moving_point(theta)
            point = plane.number_to_point(z_value)
            mob.move_to(point)
            line.become(Line(plane.c2p(0,0), point, color=RED))
            label.next_to(dot, RIGHT, buff=0.2)

        self.play(UpdateFromAlphaFunc(dot, update_dot), run_time=5)
        
        self.play(Write(text1))
        self.wait(1.5)



        # Overlay the text


class ComplexIntro(Scene):
    def construct(self):
        # Introduce the equation
        statement = Text('Complex Numbers', font_size=35)
        statement.to_edge(UP)
        statement1 = Text("Denoted as", font_size=30)
        statement1.next_to(statement, DOWN)
        equation = MathTex("z =", "x", "+", "y", "i",",", color=BLUE)
        equation.next_to(statement1, DOWN)
       
        symbol = MathTex(r"\mathbb{C}", font_size=60)
        symbol.next_to(statement, RIGHT)
       



        # Annotation for i
        i_annotation = MathTex(r"\text{where } i = \sqrt{-1}", font_size=30).next_to(equation, DOWN * 1)



        # Display all
        self.play(Write(statement))
        self.play(Write(symbol))
        self.wait(1)
        self.play(FadeIn(statement1))
        self.wait(1)
        self.play(Write(equation))
        self.wait(1)
        self.play(Write(i_annotation))
        
        self.wait(3.5)

        self.play(FadeOut(statement), FadeOut(symbol), FadeOut(statement1), FadeOut(i_annotation), FadeOut(equation))

        equation_part = MathTex("z = x + yi", color=BLUE)
        text_part1 = Text("Graphically,", font_size=33)
        text_part2 = Text("represents a point on the complex plane...", font_size=33)

        # Positioning them relative to each other:
        text_part1.to_edge(UP).to_edge(LEFT)
        equation_part.next_to(text_part1, RIGHT, buff=0.25)
        text_part2.next_to(equation_part, RIGHT, buff=0.25)

        # Grouping them together for easy manipulation:
        group = VGroup(text_part1, equation_part, text_part2)

        # Now you can manipulate this group as one entity:
        self.play(Write(group))

        # Display a graph with real and imaginary axes
        plane = ComplexPlane().scale(0.70).center().to_edge(DOWN)
        real_label = Text("Real(z)", font_size=25).next_to(plane, RIGHT)
        imag_label = Text("Imaginary(z)", font_size=25).next_to(plane, UP)
        self.play(Write(plane), Write(real_label), Write(imag_label))

        # Plot a point in the first quadrant

        x_value = 4
        y_value = 3
        dot_location = plane.number_to_point(x_value + y_value * 1j)
        dot = Dot(dot_location, color=RED)
        label = MathTex("x+yi", font_size=35).next_to(dot, UR, buff=0.1)
        self.play(FadeIn(dot), Write(label))

        vertical_line = DashedLine(dot_location, plane.c2p(x_value, 0), color=WHITE)
        horizontal_line = DashedLine(dot_location, plane.c2p(0, y_value), color=WHITE)

        x_label = MathTex("x").next_to(vertical_line, DOWN, buff=0.1)
        y_label = MathTex("y").next_to(horizontal_line, LEFT, buff=0.1)

        self.play(Create(vertical_line), Create(horizontal_line), Write(x_label), Write(y_label))

        self.wait(3)

class ComplexExplanation(Scene):
    def construct(self):
        # 1. Display the equation
        statement = Text("Let's look at why complex numbers need to exist", font_size=35)
        
        equation = MathTex("x^2 + x + 1 = 0", color=BLUE)
        equation.to_edge(UP)
        equation.to_edge(UP)
        equation.shift(DOWN * 1)

        self.play(Write(statement))
        self.wait(2)
        self.play(FadeOut(statement))
        self.play(Write(equation))
        
        self.wait(1)
        

        # 2. Show the quadratic formula

        statement2 = Text("If we wanted to find the solutions of this quadratic equation,\n"
                  "we could plug the values of the coefficients into the quadratic formula", font_size=32)
        statement2.next_to(equation, DOWN)
        self.play(Write(statement2))
        self.wait(2.5)
        self.play(FadeOut(statement2))
        formula = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
        formula.move_to(ORIGIN)
        self.play(Write(formula))
        self.wait(2)

        # 3. Substitute values
        substituted = MathTex(r"x = \frac{-1 \pm \sqrt{1 - 4(1)(1)}}{2(1)}")
        
        self.play(Transform(formula, substituted))
        self.wait(2)

        simplified = MathTex(r"x = \frac{-1 \pm \sqrt{-3}}{2}")
        
        self.play(Transform(formula, simplified))
        self.wait(2)
        self.play(FadeOut(equation))
        self.play(FadeOut(formula))
        simplified = MathTex(r"x = \frac{-1 \pm \sqrt{-3}}{2}", color=BLUE)
        simplified.to_edge(UP)
        self.play(Write(simplified))

        # 4. Highlight sqrt(-3)
        numerator = Text("Take a look at the square root term in the numerator", font_size=25)
        numerator.next_to(simplified, DOWN*1.25)

        
        square_root = MathTex(r"\sqrt{-3}")
        square_root.set_color(RED)
        square_root.next_to(numerator, DOWN)
        
        self.play(Write(numerator))
        self.play(Write(square_root))
        self.wait(2)
        self.play(FadeOut(numerator))
        

        # 5. Explain the sqrt(-1) dilemma
        
        real_numbers = Text("The expression under the square root is negative, meaning the quadratic equation has no real solutions", font_size=25)
        symbol = MathTex(r"\mathbb{R}", font_size=40)
        explanation2 = MathTex(r" \sqrt{-3}")
        explanation4 = Text("is nonsense in the realm of real numbers, as no x can mulitply by itself \n"
        "to become a negative value", font_size=25)
        
        # Align them from the left edge
        real_numbers.to_edge(LEFT)
        explanation2.next_to(real_numbers, DOWN).align_to(real_numbers, LEFT)
        explanation4.next_to(explanation2, RIGHT, buff=0.2)
        
        
        
        self.play(Write(real_numbers))
        
        self.wait(0.5)
        self.play(Write(explanation2))
        self.play(Write(explanation4))
        self.wait(4)
        
        





class ComplexRepresentation(Scene):

    def construct(self):
        # 1. Display the complex number in exponential form
        statement = Text("z = x + yi, where x corresponds to Re(z), and y corresponds to Im(z) \n"
        "is just one way to graphically represent a unique complex number", font_size= 30)
        statement.to_edge(UP)

                # Display a graph with real and imaginary axes
        plane0 = ComplexPlane().scale(0.5).center()

        plane0.next_to(statement, DOWN * 3.5)
        real_label = Text("Real(z)", font_size=25).next_to(plane0, RIGHT)
        imag_label = Text("Imaginary(z)", font_size=25).next_to(plane0, UP)
        self.play(Write(statement))
        self.play(Write(plane0), Write(real_label), Write(imag_label))

        # Plot a point in the first quadrant
        dot_location = plane0.number_to_point(4+3j)  # Change coordinates (1+2j) as desired
        dot = Dot(dot_location, color=RED)
        label = MathTex("x+yi", font_size=35).next_to(dot, UR, buff=0.1)
        self.play(FadeIn(dot), Write(label))


        self.wait(1.5)
        self.play(FadeOut(statement,plane0,real_label,imag_label,dot,label ))
        statement1 = Text('A much more useful alternative for representing a complex number is', font_size=30)
        statement1.move_to(ORIGIN)

        formula = MathTex(r"z = re^{i\theta}, \text{ where } r \text{ is the modulus and } \theta \text{ is the argument.}")
        formula1 = MathTex(r"z = re^{i\theta")

        

        formula.next_to(statement1, DOWN)
        formula1.to_edge(UP)
        statement.next_to(formula)
 
       
        self.play(Write(statement1))
        self.play(Write(formula))
        self.wait(2)

        self.play(FadeOut(formula, statement1))
        

        # 2. Display the complex plane
        plane = ComplexPlane().scale(0.8).center()
       
        real_label = Text("Re(z)", font_size=25).next_to(plane, RIGHT)
        imag_label = Text("Im(z)", font_size=25).next_to(plane, UP)

        
        
        self.play(Write(plane), Write(real_label), Write(imag_label))
        self.wait(1)

        # 3. Plot a point on the complex plane
        point_coords = 5 * np.exp(2j * PI / 8)  # Adjust this for different points (r and theta)
        dot = Dot(plane.number_to_point(point_coords), color=RED)

        dotted_line = DashedLine(dot.get_center(), [dot.get_center()[0], 0, 0], dash_length=0.1, color=WHITE)
        dotted_label = MathTex('x').next_to(dotted_line, DOWN, buff=0.1)


        # 4. Draw the magnitude line segment from the origin to the point
        magnitude_line = Line(plane.c2p(0,0), dot.get_center(), color=BLUE)

        # 5. Indicate the angle theta
        theta_angle = np.angle(point_coords)  # Angle in radians
        arc = Arc(start_angle=0, angle=theta_angle, radius=0.5, color=GREEN)

        # 6. Add the theta symbol
        theta_label = MathTex(r"\theta").next_to(arc, RIGHT, buff=0.3).shift(UP * 0.2)  # Shift it upwards a bit

        # 7. Add the 'r' label
        r_position = (magnitude_line.get_start() + magnitude_line.get_end()) / 2  # Midpoint of magnitude line
        r_label = MathTex("r").next_to(r_position, LEFT, buff=0.25)

        # Display everything
        self.play(FadeIn(dot), Create(magnitude_line), Create(arc))
        self.wait(1.5)
        self.play(FadeIn(theta_label), Write(r_label))
        self.wait(1)
        self.play(FadeIn(dotted_line), Write(dotted_label))
        self.wait(3)






class ComplexTriangle(Scene): ###fix pythag transformation
    def construct(self):
        # Display the complex plane
        plane = ComplexPlane().scale(0.8).center()
        self.play(Create(plane))
        self.wait(1)

        # Plot a point on the complex plane (representing a complex number)
        point_coords = 4 * np.exp(2j * PI / 7)
        dot = Dot(plane.number_to_point(point_coords), color=RED)

        # Draw the magnitude line segment from the origin to the point (hypotenuse r)
        magnitude_line = Line(plane.c2p(0,0), dot.get_center(), color=BLUE)

        # Vertical line from the dot to the x-axis (imaginary part y)
        vertical_line = Line(dot.get_center(), [dot.get_center()[0], 0, 0], color=BLUE)
        
        horizontal_line = Line(plane.c2p(0, 0), [dot.get_center()[0], 0, 0], color=WHITE)

        # Indicate the angle theta
        theta = np.angle(point_coords)
        arc = Arc(start_angle=0, angle=theta, radius=0.5, color=GREEN)

        # Add labels for r, x, and y
        r_label = MathTex("r").next_to(magnitude_line, buff=-0.5).shift(LEFT)
        x_label = MathTex("x").next_to(vertical_line.get_end(), DOWN, buff=0.1).shift(LEFT * 0.75)
        y_label = MathTex("y").next_to(vertical_line, RIGHT, buff=0.1)
        theta_label = MathTex(r"\theta").next_to(arc, RIGHT, buff=0.1).shift(UP * 0.2)

        # Display everything
        self.play(FadeIn(dot), Create(magnitude_line), Create(vertical_line), Create(arc), 
                  Write(r_label), Write(x_label), Write(y_label), Write(theta_label), Create(horizontal_line))
        self.wait(2)

        self.play(FadeOut(plane), FadeOut(dot))

        #FadeOut(magnitude_line), FadeOut(vertical_line), FadeOut(arc), FadeOut(theta_label))
        

        # Transform the labels into the Pythagorean theorem equation
        pythagorean = MathTex("r^2", "=", "x^2", "+", "y^2").move_to(ORIGIN)
        new_equation = MathTex("r", "=", r"\sqrt{x^2 + y^2}").move_to(ORIGIN)
        title = Text("By Pythagorean Theorem", font_size=30, color=RED)
        title.to_edge(UP)

        self.play(Write(title))
        self.play(FadeOut(magnitude_line), FadeOut(vertical_line), FadeOut(arc), FadeOut(theta_label), FadeOut(horizontal_line))
        self.play(
            Transform(r_label, pythagorean[0]),
            Transform(x_label, pythagorean[2]),
            Transform(y_label, pythagorean[4]),
            FadeIn(pythagorean[1]), FadeIn(pythagorean[3]),
        )
        
        self.wait(2)

        equation1 = MathTex(r"r^2 = x^2 + y^2 \implies r = \sqrt{x^2 + y^2}")
        equation1.move_to(ORIGIN)

        self.play(FadeOut(r_label), FadeOut(x_label), FadeOut(y_label), FadeOut(pythagorean))
        self.play(FadeIn(equation1))

        self.wait(3)

        

       # self.play(Transform(pythagorean, new_equation))
        
        
        
class TrigonometricIdentities(Scene):
    def construct(self):
        # 1. Display the right-angled triangle
        triangle = Polygon([0, 0, 0], [3, 0, 0], [3, 4, 0], color=WHITE)
        triangle.shift(DOWN*1)
        # Adjusting the positions of the labels
        r_label = MathTex("r").next_to(triangle.get_left(), LEFT, buff=0.1)
        r_label.shift(RIGHT*1.40)
        r_label.shift(UP*0.1)
        x_label = MathTex("x").next_to(triangle.get_bottom(), DOWN, buff=0.2)
        y_label = MathTex("y").next_to(triangle.get_right(), RIGHT, buff=0.2)

        # Adding right-angle symbol inside the triangle
        horizontal_line = Line(triangle.get_corner(DR), triangle.get_corner(DL))
        vertical_line = Line(triangle.get_corner(DR), triangle.get_corner(UR))


        right_angle = RightAngle(line1=horizontal_line, line2=vertical_line, length=0.25)

        self.play(Create(triangle), Write(r_label), Write(x_label), Write(y_label), Write(right_angle))
        self.wait(1)

        # 2. Present the Pythagoras theorem and its simplified form
        pythagoras = MathTex("r^2", "=", "x^2", "+", "y^2").to_edge(UP)
        simplified = MathTex("r", "=", r"\sqrt{x^2 + y^2}").to_edge(UP)

        self.play(Write(pythagoras))
        self.wait(1)
        self.play(Transform(pythagoras, simplified))
        self.wait(1)

        # 3. Present trigonometric ratios
        cos_relation = MathTex(r"\cos(\theta)", "=", r"\frac{x}{r}", r"\implies x = r\cos(\theta)", color=GREEN).next_to(triangle, LEFT, buff=0.1)
        sin_relation = MathTex(r"\sin(\theta)", "=", r"\frac{y}{r}", r"\implies y = r\sin(\theta)", color=RED).next_to(cos_relation, DOWN, buff=0.5)

        self.play(Write(cos_relation))
        self.wait(1)
        self.play(Write(sin_relation))
        self.wait(3)
            
        self.play(FadeOut(triangle), FadeOut(r_label),  FadeOut(x_label),  FadeOut(y_label),  FadeOut(right_angle), FadeOut(pythagoras), FadeOut(cos_relation), FadeOut(sin_relation))

        cos_relation = MathTex(r"\cos(\theta)", "=", r"\frac{x}{r}", r"\implies x = r\cos(\theta)").to_edge(UP)
        sin_relation = MathTex(r"\sin(\theta)", "=", r"\frac{y}{r}", r"\implies y = r\sin(\theta)").next_to(cos_relation, DOWN, buff=0.5)

        self.play(Write(cos_relation))
        self.wait(1)
        self.play(Write(sin_relation))
        self.wait(2)

        intro_text = Text('Now we have relationships between x, y, r, cosine and sine')
        intro_text.next_to(sin_relation, DOWN)
        intro_text.scale(0.7)
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))
        self.play(FadeOut(cos_relation), FadeOut(sin_relation))

        # Display the initial complex number formula
        complex_formula = MathTex("z", "=", "re^{i\\theta}", "=", "x", "+", "iy").to_edge(UP)
        expression = MathTex(r"\text{Since we know }", "x",  "=" r"\cos(\theta)", r"\text{ and }", "y", "=" r"\sin(\theta)", r"\text{, then}")
        expression.next_to(complex_formula, DOWN)
        
        self.play(Write(complex_formula))
        self.wait(1)
        self.play(FadeIn(expression))
        self.wait(3)
        self.play(FadeOut(expression))

        # Transform x and y to their trigonometric relationships
        new_formula = MathTex("z", "=", "re^{i\\theta}", "=", "r\\cos(\\theta)", "+", "ir\\sin(\\theta)")
        
        self.play(TransformMatchingTex(complex_formula, new_formula))
        self.wait(2)

        # Euler's Identity
        euler_identity = MathTex("e^{i\\theta}", "=", "\\cos(\\theta)", "+", "i\\sin(\\theta)")
        self.play(TransformMatchingTex(new_formula, euler_identity))
        self.wait(2)

        # Surrounding rectangle (i.e., box) for Euler's Identity
        box = SurroundingRectangle(euler_identity, color=WHITE)
        label = Text("Euler's Formula").next_to(box, UP)

        # Displaying the box and label
        self.play(Create(box), Write(label))
        self.wait(2)



class Cosine(Scene):
    def construct(self):
        # Set up the axes
        axes = Axes(
            x_range=[-3.5, 3.5], 
            y_range=[-1.5, 1.5],
            axis_config={"color": BLUE},
        )
        axes_labels = axes.get_axis_labels(
            x_label="x",
            y_label="y"
        )

        # Graph the function
        graph = axes.plot(lambda x: np.cos(x), color=YELLOW)
        

        self.play(Create(axes), Write(axes_labels), Create(graph))
        self.wait(1)

        # Pick a value for theta and highlight cos(theta) and cos(-theta)
        theta_val = PI / 3
        dot1 = Dot(point=axes.c2p(theta_val, np.cos(theta_val)), color=RED)
        dot2 = Dot(point=axes.c2p(-theta_val, np.cos(-theta_val)), color=RED)

       

        # Display the equation cos(theta) = cos(-theta)
        equation = MathTex("\\cos(\\theta)", "=", "\\cos(-\\theta)").to_edge(UP)
        self.play(FadeOut(axes_labels))
        self.play(Write(equation))
        self.play(FadeIn(dot1), FadeIn(dot2))
        self.wait(3)

class Sine(Scene):
    def construct(self):
        # Set up the axes
        axes = Axes(
            x_range=[-3.5, 3.5], 
            y_range=[-1.5, 1.5],
            axis_config={"color": BLUE},
        )
        axes_labels = axes.get_axis_labels(
            x_label="x",
            y_label="y"
        )

        # Graph the function
        graph = axes.plot(lambda x: np.sin(x), color=YELLOW)
        

        self.play(Create(axes), Write(axes_labels), Create(graph))
        self.wait(1)

        # Pick a value for theta and highlight sin(theta) and sin(-theta)
        theta_val = PI / 3
        dot1 = Dot(point=axes.c2p(theta_val, np.sin(theta_val)), color=RED)
        dot2 = Dot(point=axes.c2p(-theta_val, -np.sin(theta_val)), color=RED)

        

        # Display the equation sin(-theta) = -sin(theta)
        equation = MathTex("\\sin(-\\theta)", "=", "-\\sin(\\theta)").to_edge(UP)
        self.play(FadeOut(axes_labels))
        self.play(Write(equation))
        self.play(FadeIn(dot1), FadeIn(dot2))
        self.wait(2)

class EulerToTrig(Scene):
    def construct(self):

                # Show that cos(-theta) = cos(theta) and sin(-theta) = -sin(theta)
        statement = Text('Trigonometric Identities', font_size=30).to_edge(UP)
        cos_relationship = MathTex("\\cos(-\\theta)", "=", "\\cos(\\theta)", color=GREEN).next_to(statement, DOWN)
        sin_relationship = MathTex("\\sin(-\\theta)", "=", "-\\sin(\\theta)", color=RED).next_to(cos_relationship, DOWN)
        self.play(Write(statement))
        self.wait(1.5)
        self.play(Write(cos_relationship))
        self.play(Write(sin_relationship))
        self.wait(3)
        self.play(FadeOut(cos_relationship), FadeOut(sin_relationship), FadeOut(statement))
        cos_relationship = MathTex("\\cos(-\\theta)", "=", "\\cos(\\theta)", color=GREEN).to_edge(RIGHT).shift(UP*3.25)
        sin_relationship = MathTex("\\sin(-\\theta)", "=", "-\\sin(\\theta)", color=RED).next_to(cos_relationship, DOWN)
        self.play(FadeIn(cos_relationship), FadeIn(sin_relationship))

        
        # Start with Euler's formula for e^(i theta) and e^(-i theta)
        eulers_formula_positive = MathTex("e^{i\\theta}", "=", "\\cos(\\theta)", "+", "i\\sin(\\theta)").to_edge(UP+LEFT*2)
        eulers_formula_negative = MathTex("e^{-i\\theta}", "=", "\\cos(-\\theta)", "+", "i\\sin(-\\theta)").next_to(eulers_formula_positive, DOWN, aligned_edge=LEFT)
        eulers_formula_negative_substituted = MathTex("e^{-i\\theta}", "=", "\\cos(\\theta)", "-", "i\\sin(\\theta)").next_to(eulers_formula_positive, DOWN, aligned_edge=LEFT)
        
        self.play(Write(eulers_formula_positive))
        self.play(Write(eulers_formula_negative))
        self.wait(2)
        self.play(Transform(eulers_formula_negative, eulers_formula_negative_substituted))
        

        # Substitute the relationships into the equation
        #eulers_formula_negative_substituted = MathTex("e^{-i\\theta}", "=", "\\cos(\\theta)", "-", "i\\sin(\\theta)").next_to(eulers_formula_negative, DOWN * 1.25, RIGHT * 0.75)
        #eulers_formula_negative = MathTex("e^{-i\\theta}", "=", "\\cos(-\\theta)", "+", "i\\sin(-\\theta)").next_to(eulers_formula_negative, DOWN * 1.25, RIGHT * 0.75)
        
        
       
        self.wait(1)

        # Add both e^(i theta) and e^(-i theta) to get 2cos(theta)
        cos_combined1 = MathTex("e^{i\\theta}", "+", "e^{-i\\theta}", "=", "\\cos(\\theta)", "+", "\\cos(\\theta)","+", "i \\sin(\\theta)", "-", "i \\sin(\\theta)", color=GREEN).move_to(ORIGIN)
        
        self.play(Write(cos_combined1))
        self.wait(2)
        

        cos_combined = MathTex("e^{i\\theta}", "+", "e^{-i\\theta}", "=", "2\\cos(\\theta)", color=GREEN)
        self.play(Transform(cos_combined1, cos_combined))
        self.wait(2)
        
        

        # Divide both sides by 2 to get expression for cos(theta)
        cos_result = MathTex("\\cos(\\theta)", "=", "\\frac{e^{i\\theta} + e^{-i\\theta}}{2}", color=GREEN).move_to(ORIGIN)
        self.play(Transform(cos_combined1, cos_result))
        self.wait(3)
        
        self.play(FadeOut(cos_combined1))

        # Likewise, subtract e^(-i theta) from e^(i theta) to get 2i sin(theta)
        sin_combined1 = MathTex("e^{i\\theta}", "-", "e^{-i\\theta}", "=", "\\cos(\\theta)", "-", "\\cos(\\theta)","+", "i \\sin(\\theta)", "-","-" "i \\sin(\\theta)", color=RED).move_to(ORIGIN)
        sin_combined = MathTex("e^{i\\theta}", "-", "e^{-i\\theta}", "=", "2i\\sin(\\theta)", color=RED).move_to(ORIGIN)
        self.play(Write(sin_combined1))
        self.wait(1)
        self.play(Transform(sin_combined1, sin_combined))
        self.wait(2)

        # Divide both sides by 2i to get expression for sin(theta)
        sin_result = MathTex("\\sin(\\theta)", "=", "\\frac{e^{i\\theta} - e^{-i\\theta}}{2i}", color=RED).move_to(ORIGIN)
        
        self.play(Transform(sin_combined1, sin_result))
        self.wait(3)

        self.play(FadeOut(eulers_formula_positive), FadeOut(sin_combined1), FadeOut(eulers_formula_negative), FadeOut(cos_relationship), FadeOut(sin_relationship))
        self.wait(1)

        cos_result = MathTex("\\cos(\\theta)", "=", "\\frac{e^{i\\theta} + e^{-i\\theta}}{2}", color=GREEN).to_edge(UP)
        sin_result = MathTex("\\sin(\\theta)", "=", "\\frac{e^{i\\theta} - e^{-i\\theta}}{2i}", color=RED).next_to(cos_result, DOWN)
        statement1 = Text("We have just derived sine and cosine in terms of the exponential function,\n" 
        "                         which leads us into the fascinating topic of", font_size=30).next_to(sin_result, DOWN * 2)
        statement2 = Text("Infinite Series", font_size=40, color=BLUE).next_to(statement1, DOWN * 2)

        self.play(FadeIn(cos_result))

        self.play(FadeIn(sin_result))
        self.wait(1)

        self.play(Write(statement1))
        self.wait(1.5)
        self.play(Write(statement2))
        self.wait(2)


        


class InfiniteSeries(Scene):
    def construct(self):
        # 1. Display the e^x infinite series at the top
        statement = MathTex("e^x " r"\text{ can be written in an infinitely long string of pieces added together }" , font_size=40).to_edge(UP)
        series_text = MathTex(
            "e^x", "=", "1", "+", "x", "+", 
            r"\frac{x^2}{2!}", "+", 
            r"\frac{x^3}{3!}", "+",
            r"\frac{x^4}{4!}", "+", 
            r"\frac{x^5}{5!}", "+ \dots"
        ).scale(0.8).to_edge(UP)
        self.play(Write(statement))
        self.wait(3)
        self.play(FadeOut(statement))
        self.play(Write(series_text))

                # 2. Display the graph of e^x underneath
        axes = Axes(x_range=[-2, 2], y_range=[-3, 8], axis_config={"color": BLUE})
        axes.shift(DOWN * 0.75)
        

        graph = axes.plot(lambda x: np.exp(x), color=WHITE)
        graph_label = axes.get_graph_label(graph, label='e^x')

        self.play(
            Create(axes),
            Create(graph),
            Write(graph_label)
        )

        # 3. Display the graph that updates as we add more terms to the series
        partial_series = [
            lambda x: 1,
            lambda x: 1 + x,
            lambda x: 1 + x + x**2/np.math.factorial(2),
            lambda x: 1 + x + x**2/np.math.factorial(2) + x**3/np.math.factorial(3),
            lambda x: 1 + x + x**2/np.math.factorial(2) + x**3/np.math.factorial(3) + x**4/np.math.factorial(4),
            lambda x: 1 + x + x**2/np.math.factorial(2) + x**3/np.math.factorial(3) + x**4/np.math.factorial(4) + x**5/np.math.factorial(5)
        ]


        self.wait(1)

        terms = [
            "1 ",
            "+ x",
            "+ \\frac{x^2}{2!}",
            "+ \\frac{x^3}{3!}",
            "+ \\frac{x^4}{4!}",
            "+ \\frac{x^5}{5!}",
        ]

        previous_partial_graph = axes.plot(partial_series[0], color=YELLOW)
        current_series = MathTex("e^x", "=", *terms[0]).move_to(UP * 3.5)
        self.play(Create(previous_partial_graph), Transform(series_text, current_series), run_time=1)
        self.wait(0.5)

        # Now, for each remaining partial sum, transform the previous one into the current one
        for i, partial in enumerate(partial_series[1:], start=1):
            new_partial_graph = axes.plot(partial, color=YELLOW)
            current_series = MathTex("e^x", "=", *terms[:i+1]).move_to(UP * 3).scale(0.8)
            self.play(Transform(previous_partial_graph, new_partial_graph), Transform(series_text, current_series), run_time=1)
            self.wait(0.5)

        self.wait(1)

class EulersSeries(Scene):
    def construct(self):
        # Series for e^x
        series_ex = MathTex(
            "e^x", "=", "1", "+", "x", "+", 
            r"\frac{x^2}{2!}", "+", 
            r"\frac{x^3}{3!}", "+",
            r"\frac{x^4}{4!}", "+", 
            r"\frac{x^5}{5!}", "+ \dots"
        ).to_edge(UP)
        self.play(Write(series_ex))
        self.wait(1)

        statement = MathTex(r"\text{Substituting in }", "i\\theta" r"\text{ and }" "-i\\theta" r"\text{ for }" "x", r"\text{, we get:}" , font_size=35).next_to(series_ex, DOWN)
        self.play(Write(statement))
        self.wait(2)
        self.play(FadeOut(statement))

        # Series for e^{i\theta}
        series_itheta = MathTex(
            "e^{i\\theta}", "=", "1", "+", "i\\theta", "-", 
            r"\frac{\theta^2}{2!}", "-", 
            r"i\frac{\theta^3}{3!}", "+",
            r"\frac{\theta^4}{4!}", "+", 
            r"i\frac{\theta^5}{5!}", "+ \dots"
        ).next_to(series_ex, DOWN, buff=0.5)
        self.play(TransformMatchingTex(series_ex, series_itheta))

        self.wait(3)

        # Series for e^{-i\theta}
        series_minus_itheta = MathTex(
            "e^{-i\\theta}", "=", "1", "-", "i\\theta", "-", 
            r"\frac{\theta^2}{2!}", "+", 
            r"i\frac{\theta^3}{3!}", "+",
            r"\frac{\theta^4}{4!}", "-", 
            r"i\frac{\theta^5}{5!}", "+ \dots"
        ).next_to(series_itheta, DOWN, buff=0.5)
        self.play(TransformMatchingTex(series_itheta, series_minus_itheta))
        self.wait(2)


#class EulersSeries1(Scene):
   # def construct(self):
        # Properties of i
     #   properties_i = VGroup(
     #       MathTex("i =", r"\sqrt{-1}"),
     #       MathTex("i^2 =", "-1"),
     #       MathTex("i^3 =", "-i"),
     #       MathTex("i^4 =", "1"),
      #      Text("...", font_size=36)
      #  ).arrange(DOWN, buff=0.5).to_edge(UP)

     #   self.play(Write(properties_i))
      #  self.wait(2)
      #  self.play(FadeOut(properties_i))

        # Series for e^x
       # series_ex = MathTex(
      #      "e^x", "=", "1", "+", "x", "+", 
       #     r"\frac{x^2}{2!}", "+", 
      #      r"\frac{x^3}{3!}", "+",
       #     r"\frac{x^4}{4!}", "+", 
      #      r"\frac{x^5}{5!}", "+ \dots"
     #   ).to_edge(UP)
     #   self.play(Write(series_ex))
     #   self.wait(1)

        # Series for e^{i\theta}
     #   series_itheta = MathTex(
     #       "e^{i\\theta}", "=", "1", "+", "i\\theta", "-", 
     #       r"\frac{\theta^2}{2!}", "-", 
     #       r"i\frac{\theta^3}{3!}", "+",
     #       r"\frac{\theta^4}{4!}", "+", 
     #       r"i\frac{\theta^5}{5!}", "+ \dots"
     #   ).next_to(series_ex, DOWN, buff=0.5)
     #   self.play(TransformMatchingTex(series_ex, series_itheta))
     #   self.wait(1)

        # Series for e^{-i\theta}
     #   series_minus_itheta = MathTex(
     #       "e^{-i\\theta}", "=", "1", "-", "i\\theta", "-", 
     #       r"\frac{\theta^2}{2!}", "+", 
     #       r"i\frac{\theta^3}{3!}", "+",
      #      r"\frac{\theta^4}{4!}", "-", 
      #      r"i\frac{\theta^5}{5!}", "+ \dots"
      #  ).next_to(series_itheta, DOWN, buff=0.5)
     #   self.play(TransformMatchingTex(series_itheta, series_minus_itheta))
      #  self.wait(2)

class TrigSeriesFromEulers(Scene):
    def construct(self):
        # Starting series for e^{i\theta}

        cos_result = MathTex("\\cos(\\theta)", "=", "\\frac{e^{i\\theta} + e^{-i\\theta}}{2}", color=GREEN).move_to(ORIGIN)
        sin_result = MathTex("\\sin(\\theta)", "=", "\\frac{e^{i\\theta} - e^{-i\\theta}}{2i}", color=RED).next_to(cos_result, DOWN)

        series_itheta = MathTex(
            "e^{i\\theta}", "=", "1", "+", "i\\theta", "-", 
            r"\frac{\theta^2}{2!}", "-", 
            r"i\frac{\theta^3}{3!}", "+",
            r"\frac{\theta^4}{4!}", "+", 
            r"i\frac{\theta^5}{5!}", "+ \dots"
        ).to_edge(UP)

        # Series for e^{-i\theta}
        series_minus_itheta = MathTex(
            "e^{-i\\theta}", "=", "1", "-", "i\\theta", "-", 
            r"\frac{\theta^2}{2!}", "+", 
            r"i\frac{\theta^3}{3!}", "+",
            r"\frac{\theta^4}{4!}", "-", 
            r"i\frac{\theta^5}{5!}", "+ \dots"
        ).next_to(series_itheta, DOWN, buff=0.5)

        self.play(Write(series_itheta), Write(series_minus_itheta))

        statement = Text("Since we found cosine in terms of e earlier:", font_size=25)
        statement.next_to(series_minus_itheta, DOWN)
        cos_result = MathTex("\\cos(\\theta)", "=", "\\frac{e^{i\\theta} + e^{-i\\theta}}{2}", color=GREEN).next_to(statement, DOWN)
        sin_result = MathTex("\\sin(\\theta)", "=", "\\frac{e^{i\\theta} - e^{-i\\theta}}{2i}", color=RED).next_to(cos_result, DOWN)
        statement2 = MathTex(r"\text{we can add together the infinite series for }", "e^{i\\theta}" r"\text{ and }", "e^{-i\\theta}"r"\text{ and divide by 2}", font_size=30).next_to(series_minus_itheta, DOWN)

        self.play(Write(statement))
        self.wait(2)
        self.play(Write(cos_result))
    
        self.wait(3)
        self.play(FadeOut(statement))
        self.play(FadeIn(statement2))
        self.wait(3)
        self.play(FadeOut(statement2))
        self.play(FadeOut(cos_result))
        

        cos_result2 = MathTex( "\\frac{e^{i\\theta} + e^{-i\\theta}}{2}" "=", color=GREEN).next_to(series_minus_itheta, DOWN * 1.5)
        cos_result3 = MathTex(r"=\cos(\theta) =", "1", "-", r"\frac{(\theta)^2}{2!}", "+", r"\frac{(\theta)^4}{4!}", "-", r"\frac{(\theta)^6}{6!}", "+ \dots").next_to(cos_result2, DOWN * 1.5)
        comment = MathTex(r"\text{(all of the even powers of }", "\\theta}"r"\text{)}").next_to(cos_result3, DOWN)
        self.play(Write(cos_result2))
        self.wait(1)
        self.play(Write(cos_result3))
        self.wait(1)
        self.play(Write(comment))
        self.wait(3)
        self.play(FadeOut(cos_result2), FadeOut(cos_result3), FadeOut(comment))

        statement3 = Text("and since we found sine in terms of e earlier:", font_size=25)
        sin_result = MathTex("\\sin(\\theta)", "=", "\\frac{e^{i\\theta} - e^{-i\\theta}}{2i}", color=RED).next_to(statement3, DOWN)
        statement3.next_to(series_minus_itheta, DOWN)
        statement4 = MathTex(r"\text{we can subtract the infinite series for }", "-e^{i\\theta}" r"\text{ from }", "e^{i\\theta}" r"\text{ and divide by 2i}", font_size=30).next_to(series_minus_itheta, DOWN)

        self.play(Write(statement3))
        self.wait(2)
        self.play(Write(sin_result))
        self.wait(3)
        self.play(FadeOut(statement3))
        self.play(FadeIn(statement4))
        self.wait(3)
        self.play(FadeOut(statement4))
        self.play(FadeOut(sin_result))

        sin_result2 = MathTex( "\\frac{e^{i\\theta} - e^{-i\\theta}}{2i}" "=", color=RED).next_to(series_minus_itheta, DOWN * 1.5)
        sin_result3 = MathTex(r"\sin(\theta) =", "\\theta", "-", r"\frac{(\theta)^3}{3!}", "+", r"\frac{(\theta)^5}{5!}", "+ \dots")
        sin_result3.next_to(sin_result2, DOWN * 1.5)
        comment2 = MathTex(r"\text{(all of the odd powers of }", "\\theta}"r"\text{)}").next_to(sin_result3, DOWN)

        self.play(Write(sin_result2))
        self.wait(2)
        self.play(Write(sin_result3))
        self.wait(1)
        self.play(Write(comment2))
        self.wait(3)
        self.play(FadeOut(sin_result2), FadeOut(sin_result3), FadeOut(comment2), FadeOut(series_itheta), FadeOut(series_minus_itheta))

class EulersIdentityReveal(Scene):
    def construct(self):
        # Introduction to Euler's identity
        eulers_identity = MathTex("e^{i\\pi} + 1 = 0")
        intro = Text("Behold, one of the most beautiful equations in mathematics", font_size=30)
        self.play(Write(intro))
        self.wait(1)
        self.play(FadeOut(intro))
        self.wait(1)
        

        # Derivation of Euler's identity
        # Using e^(i*theta) formula:
        eulers_formula = MathTex("e^{i\\theta} =", "\\cos(\\theta)", "+", "i\\sin(\\theta)")
        self.play(Write(eulers_formula))
        self.wait(1)
        sub = MathTex(r"\text{Substituting }", "\pi",r"\text{ in for }",  "\\theta}"r"\text{:}").next_to(eulers_formula, UP)
        self.play(Write(sub))
        self.wait(2)
        self.play(FadeOut(sub))

        # Substituting theta with pi:
        substituted = MathTex("e^{i\\pi} =", "\\cos(\\pi)", "+", "i\\sin(\\pi)")
        self.play(TransformMatchingTex(eulers_formula, substituted))
        self.wait(2)

        # Evaluating the trigonometric values:
        evaluated = MathTex("e^{i\\pi} =", "-1", "+", "0i")
        self.play(TransformMatchingTex(substituted, evaluated))
        self.wait(2)

        # Simplifying to Euler's identity:
        simplified = MathTex("e^{i\\pi} + 1 = 0")
        self.play(TransformMatchingTex(evaluated, simplified))
        self.wait(1)
        


        
        conclusion = Text("And that's Euler's Identity!", font_size=30).next_to(simplified, DOWN)
        plane = ComplexPlane().scale(1.5)
        original_plane = plane.copy()
        self.add(plane)

        # Function to perform complex transformation: dilation + rotation
        def complex_transform(mob, alpha):
            factor = 1 + 0.5*np.sin(2*PI*alpha)
            angle = 2*PI*alpha
            mob.become(original_plane.copy().rotate(angle).scale(factor))

        # Apply the transformation
        self.play(Write(conclusion))
        self.play(UpdateFromAlphaFunc(plane, complex_transform), run_time=5, rate_func=linear)
        
        
        self.play(FadeOut(conclusion, simplified))
        thanks  = Text("If you made it this far, thank you for watching !")
        thanks.to_edge(UP)
        name = Text('Nathan Foale')
        name.next_to(thanks, DOWN * 2)
        self.play(Write(thanks))
        self.wait(1)
        self.play(Write(name))




class ACPhasorVisualisation(Scene):
    def construct(self):
        # 1. AC Signals and Sinusoids
        axes = Axes(
            x_range=[0, 2*PI],
            y_range=[-1.5,1.5],
            axis_config={"color": BLUE},
        )
        curve = axes.plot(lambda x: np.sin(x), color=YELLOW)
        curve_label = axes.get_graph_label(curve, label='Sinusoidal AC Voltage').shift(UP*2)
        text = Text("Beyond Euler's formula's aesthetic beauty, the underlying mathematics \n"
        "has many practical applications. One of the most tangible and easy to visualise \n"
        "applications is in electrical engineering dealing with alternating current circuits", color=YELLOW, font_size=30)

        self.play(Write(text))
        self.wait(3)
        self.play(FadeOut(text))

        self.play(Create(axes), Create(curve), Write(curve_label))
        self.wait(1)

        # Transition to Phasor Representation
        self.play(FadeOut(curve_label))

        # 2. Phasor Visualization
        complex_plane = ComplexPlane().scale(0.8).center()
        phasor = Line(complex_plane.c2p(0,0), complex_plane.c2p(1, 0), color=YELLOW)

        def update_phasor(mob, alpha):
            mob.become(Line(complex_plane.c2p(0,0), complex_plane.number_to_point(np.exp(1j * TAU * alpha)), color=YELLOW))
        
        self.play(Transform(axes, complex_plane), Transform(curve, phasor))
        self.play(UpdateFromAlphaFunc(phasor, update_phasor), run_time=2, rate_func=linear)

        # Explanation of Phasor and Euler's Identity
        explanation = Text("The rotating vector represents the AC signal in the complex plane.", font_size=24).to_edge(UP)
        euler_explanation = MathTex("e^{j\\theta} = \\cos(\\theta) + j\\sin(\\theta)").to_edge(DOWN)
        self.play(Write(explanation), Write(euler_explanation))
        self.wait(2)

        # FadeOut to conclude
        self.play(FadeOut(explanation), FadeOut(euler_explanation), FadeOut(phasor))

class ACPhasorExplanation(Scene):
    def construct(self):
        
        # Create a complex plane
        plane = ComplexPlane().scale(0.6).to_edge(LEFT).shift(DOWN * 0.6)
        self.play(Create(plane))

        # Explanation of Phasor and Euler's Identity
        title = Text("AC Phasor Representation", font_size=32).to_edge(UP)
        explanation1 = Text("In AC circuits, voltage or current can be represented as a rotating vector (phasor).", font_size=24).next_to(title, DOWN)
        explanation2 = Text("This phasor's projection on the vertical axis gives the instantaneous value of the AC signal.", font_size=24).next_to(explanation1, DOWN)
        self.play(Write(title), Write(explanation1), Write(explanation2))
        self.wait(2)
        
        # Display phasor (rotating vector)
        phasor_start = plane.c2p(0, 0)
        phasor_end = plane.c2p(np.cos(PI / 4), np.sin(PI / 4))
        phasor = Arrow(phasor_start, phasor_end, color=YELLOW)
        self.play(GrowArrow(phasor))
        self.wait(1)

        # Show the projection of the phasor on the vertical axis (imaginary axis)
        projection_line = DashedLine(plane.c2p(0,0), plane.c2p(0, phasor.get_end()[1]), color=RED)
        self.play(Create(projection_line))
        self.wait(1)
        
        # AC waveform corresponding to the phasor
        ac_waveform = ParametricFunction(
            lambda t: plane.c2p(t-3, np.sin(t*TAU)),
            t_range=[0, 2*PI],
            color=RED
        ).next_to(plane, RIGHT, buff=0.75)
        ac_waveform_label = Text("AC Waveform", font_size=24).next_to(ac_waveform, UP)
        self.play(Create(ac_waveform), Write(ac_waveform_label))
        self.wait(2)

        # Animation of phasor rotation and its corresponding AC waveform generation
        def update_func(mob, dt):
            mob.rotate(0.1*TAU*dt)
            new_end = mob.get_end()
            projection_line.become(DashedLine(plane.c2p(0,0), plane.c2p(0, new_end[1]), color=RED))

        phasor.add_updater(update_func)
        self.add(phasor, projection_line)
        self.wait(5)  # Duration of phasor rotation and waveform generation

        phasor.remove_updater(update_func)
        
        # Euler's Relation
        euler_explanation = MathTex("e^{j\\theta} = \\cos(\\theta) + j\\sin(\\theta)").to_edge(DOWN)
        self.play(Write(euler_explanation))
        self.wait(2)

        # FadeOut to conclude
        self.play(FadeOut(plane), FadeOut(title), FadeOut(explanation1), FadeOut(explanation2), 
                  FadeOut(phasor), FadeOut(projection_line), FadeOut(ac_waveform), FadeOut(ac_waveform_label),
                  FadeOut(euler_explanation))


class ACPhasorExplanation1(Scene):

    def construct(self):
        # Create a complex plane
        plane = ComplexPlane().scale(1)
        self.play(Create(plane))

        # Draw a circle of radius 1 (unit circle)


        # Function to get moving point
        def moving_point(t):
            return np.exp(1j * TAU * t)

        dot = Dot(plane.number_to_point(moving_point(0)), color=YELLOW)
        line = Line(plane.c2p(0,0), dot.get_center(), color=YELLOW)
       # label = MathTex("e^{i\\theta}").next_to(dot, RIGHT, buff=0.2)
        
        self.add(dot, line)

        def update_dot(mob, alpha):
            theta = interpolate(0, TAU, alpha)
            z_value = moving_point(theta)
            point = plane.number_to_point(z_value)
            mob.move_to(point)
            line.become(Line(plane.c2p(0,0), point, color=YELLOW))
            

        self.play(UpdateFromAlphaFunc(dot, update_dot), run_time=5)




class RotatingDot(Scene):
    def construct(self):
        # Create a complex plane
        plane = ComplexPlane().scale(1)
        self.play(Create(plane))

        title = Text("AC Phasor Representation", font_size=25, color=YELLOW).to_edge(UP)
        explanation1 = Text("In AC circuits, voltage or current can be represented as a rotating vector (phasor).", font_size=24, color=YELLOW).next_to(title, DOWN)
        explanation2 = Text("This phasor's projection on the vertical axis gives the instantaneous value of the AC signal.", font_size=24, color=YELLOW).next_to(explanation1, DOWN)
        self.play(Write(title), Write(explanation1), Write(explanation2))
        self.wait(2)

        # Function to get moving point
        def moving_point(t):
            return np.exp(1j * TAU * t)

        arrow = Arrow(plane.c2p(0, 0), plane.number_to_point(moving_point(0)), color=YELLOW, buff=0)
        self.add(arrow)
        points = VGroup()

        def update_arrow(mob, alpha):
            theta = interpolate(0, TAU, alpha)
            z_value = moving_point(theta)
            point = plane.number_to_point(z_value)
            mob.become(Arrow(plane.c2p(0, 0), point, color=YELLOW, buff=0))

           # Record the arrow tip for the dotted line
            dot = Dot(point, color=WHITE, radius=0.02).set_stroke(width=0.5)
            points.add(dot)
            
            wave = DashedLine(plane.c2p(0,0), point, dash_length=0.05).set_stroke(width=2)
            for p in points:
                wave.add_points_as_corners([p.get_center()])
            self.add(wave, dot)

        self.play(UpdateFromAlphaFunc(arrow, update_arrow), run_time=10)

        
        ac_waveform = ParametricFunction(
            lambda t: plane.c2p(t-3, np.sin(t*TAU)),
            t_range=[0, 2*PI],
            color=RED
        ).to_edge(RIGHT)
        ac_waveform_label = Text("AC Waveform", font_size=24).next_to(ac_waveform, UP)
        self.play(Create(ac_waveform), Write(ac_waveform_label))
        

        self.play(UpdateFromAlphaFunc(arrow, update_arrow), run_time=12)  # Increase run_time for slower rotation
        self.wait(2)




class ComplexTransformation(Scene):
    def construct(self):
        # Create a complex plane
        plane = ComplexPlane().scale(1.5)
        original_plane = plane.copy()
        self.add(plane)

        # Function to perform complex transformation: dilation + rotation
        def complex_transform(mob, alpha):
            factor = 1 + 0.5*np.sin(2*PI*alpha)
            angle = 2*PI*alpha
            mob.become(original_plane.copy().rotate(angle).scale(factor))

        # Apply the transformation
        self.play(UpdateFromAlphaFunc(plane, complex_transform), run_time=10, rate_func=linear)