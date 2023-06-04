import random
import turtle


def main():
    """
    Main function.
    """

    # Create a turtle object.
    t = turtle.Turtle()

    # Set the turtle's speed.
    t.speed(10)

    # Create a list of colors.
    colors = ["red", "green", "blue", "yellow",
              "purple", "orange", "pink", "brown"]

    # Draw a moving shape.
    for i in range(500):
        t.color(random.choice(colors))
        t.forward(20)
        t.left(random.randint(0, 360))


# Call the main function.
if __name__ == "__main__":
    main()

