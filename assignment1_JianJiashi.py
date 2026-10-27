
# IMPORTANT:
# Paste the exact file header from your course template here.

import turtle
import colorsys
import re


# =========================================
# Part 1: Turtle Drawing
# =========================================

def draw_star(pen, side_length):
    """Draw a five-pointed star."""

    for _ in range(5):
        pen.forward(side_length)
        pen.right(144)


def draw_pattern():
    """Draw a colourful rotating pattern."""

    # Create drawing window
    screen = turtle.Screen()
    screen.setup(width=900, height=800)
    screen.title("Rainbow Star Galaxy")
    screen.bgcolor("#0B1020")
    screen.tracer(0)

    # Create drawing turtle
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(2)

    # Draw 72 colourful rotating stars
    for i in range(72):

        # Dynamically change colour
        hue = i / 72
        colour = colorsys.hsv_to_rgb(hue, 0.9, 1.0)

        # Dynamically change length
        length = 65 + i * 1.7

        # Set starting position and direction
        pen.penup()
        pen.goto(0, 0)
        pen.setheading(i * 5)
        pen.pencolor(colour)
        pen.pendown()

        draw_star(pen, length)

    # Draw smaller rotating triangles
    for i in range(36):

        hue = i / 36
        colour = colorsys.hsv_to_rgb(hue, 0.55, 1.0)
        length = 35 + i * 0.5

        pen.penup()
        pen.goto(0, 0)
        pen.setheading(i * 10)
        pen.pencolor(colour)
        pen.pendown()

        for _ in range(3):
            pen.forward(length)
            pen.left(120)

    screen.update()

    print("Turtle drawing finished.")
    print("Take a screenshot, then click the drawing window.")

    screen.exitonclick()


# =========================================
# Part 2: QA Bot
# =========================================

def qa_bot():
    """Answer questions using keyword matching."""

    print("\nWelcome to the QA Bot!")
    print("Ask me about HKU, robot, jetson, AI, or human.")
    print("Type 'quit' to exit.\n")

    while True:

        question = input("You: ").strip().lower()

        if question in ("quit", "exit"):
            print("Bot: Goodbye!")
            break

        elif not question:
            print("Bot: Please enter a question.")

        else:
            # Extract words from the question
            words = re.findall(r"[a-z]+", question)

            if "hku" in words:
                print("Bot: HKU is the University of Hong Kong.")

            elif "robot" in words or "robots" in words:
                print("Bot: A robot is a machine that can perform tasks automatically.")

            elif "jetson" in words:
                print("Bot: NVIDIA Jetson is a platform for edge AI and robotics.")

            elif "ai" in words:
                print("Bot: AI means artificial intelligence.")

            elif "human" in words or "humans" in words:
                print("Bot: A human is a person, capable of learning and reasoning.")

            else:
                print("Bot: Sorry, I can answer questions about HKU, robot, jetson, AI, and human.")


# =========================================
# Main Program
# =========================================

if __name__ == "__main__":
    draw_pattern()
    qa_bot()
