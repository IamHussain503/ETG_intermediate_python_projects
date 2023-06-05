import random
import turtle


def generate_color():
    """
    Generates a random color from a color gradient.

    Returns:
        A random color from the color gradient.
    """
    colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00",
              "#0000FF", "#8B00FF"]  # Example color gradient
    return random.choice(colors)


def draw_shape(t, shape, sides, color, width):
    """
    Draws a shape using the turtle object.

    Args:
        t: The turtle object.
        shape: The shape to draw.
        sides: The number of sides of the shape.
        color: The color of the shape.
        width: The width of the line.
    """

    # Set the turtle's speed.
    t.speed(0)

    # Set the turtle's color.
    t.color(color)

    # Set the turtle's line width.
    t.pensize(width)

    # Check if the shape is a straight line.
    if sides == 2:
        return

    # Draw the shape.
    if shape == "rectangle":
        for i in range(sides):
            t.forward(20)
            t.left(360 / sides)
    elif shape == "star":
        for i in range(sides):
            t.forward(20)
            t.left(180 - 180 / sides)
    elif shape == "triangle":
        for i in range(sides):
            t.forward(20)
            t.left(120)
    else:
        for i in range(sides):
            t.forward(20)
            t.left(360 / sides)

    # Check if the turtle is out of bounds.
    if t.xcor() > turtle.window_width() or t.xcor() < -turtle.window_width():
        t.setx(-turtle.window_width())
    elif t.ycor() > turtle.window_height() or t.ycor() < -turtle.window_height():
        t.sety(-turtle.window_height())


def main():
    """
    Main function.
    """

    # Create a turtle object.
    t = turtle.Turtle()

    # Get the screen size.
    screen = turtle.Screen()
    width, height = screen.window_width() // 2, screen.window_height() // 2

    # Generate the shape data.
    shapes = []
    for i in range(100):
        # Choose a random shape.
        shape = random.choice(
            ["rectangle", "star", "triangle", "multi-corner star"])

        # Choose a random number of sides.
        sides = random.randint(3, 7)

        # Choose a random color from the gradient.
        color = generate_color()

        # Choose a random line width.
        line_width = random.randint(3,7)

        # Add the shape data to the list.
        shapes.append((shape, sides, color, line_width))

    # Draw the shapes.
    for shape_data in shapes:
        shape, sides, color, line_width = shape_data
        t.color(color)
        t.pensize(line_width)

        # Generate random position within the screen bounds
        x = random.randint(-width, width)
        y = random.randint(-height, height)

        # Move the turtle to the random position without drawing a line
        t.penup()
        t.goto(x, y)
        t.pendown()

        draw_shape(t, shape, sides, color, line_width)

    # Hide the turtle.
    t.hideturtle()

    # Keep the turtle graphics window open until it is closed manually.
    turtle.mainloop()


# Call the main function.
if __name__ == "__main__":
    main()
