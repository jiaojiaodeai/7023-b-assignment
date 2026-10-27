# IMPORTANT:
# Paste the exact file header from your course template here.

import turtle
import re

# =========================================
# Part 1: Turtle Drawing
# =========================================

def draw_star(pen, side_length):
    """Draw a five-pointed star."""
    for _ in range(5):
        pen.forward(side_length)
        pen.right(144)

def interpolate_color(start, end, t):
    """
    Interpolate between two RGB colours.
    start, end: tuples like (r, g, b), values from 0 to 1
    t: value from 0 to 1
    """
    r = start[0] + (end[0] - start[0]) * t
    g = start[1] + (end[1] - start[1]) * t
    b = start[2] + (end[2] - start[2]) * t
    return (r, g, b)

def get_blue_purple_white_color(i, total):
    """
    Create a colour gradient:
    dark blue -> purple -> white
    """
    dark_blue = (0.10, 0.25, 0.85)
    purple = (0.60, 0.30, 0.95)
    white = (1.0, 1.0, 1.0)

    t = i / (total - 1)

    if t < 0.5:
        # First half: dark blue -> purple
        return interpolate_color(dark_blue, purple, t / 0.5)
    else:
        # Second half: purple -> white
        return interpolate_color(purple, white, (t - 0.5) / 0.5)

def draw_pattern():
    """Draw a beautiful colourful rotating pattern."""

    screen = turtle.Screen()
    screen.setup(width=900, height=800)
    screen.title("Blue Purple Star Pattern")
    screen.bgcolor("#0B1020")
    screen.tracer(0)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(2)

    total_stars = 72

    # Draw rotating stars
    for i in range(total_stars):
        colour = get_blue_purple_white_color(i, total_stars)

        # Dynamically change length
        length = 65 + i * 1.5

        pen.penup()
        pen.goto(0, 0)

        # Rotate more slowly than before
        pen.setheading(i * 3)

        pen.pencolor(colour)
        pen.pendown()

        draw_star(pen, length)

    # Draw smaller triangles in similar colour style
    total_triangles = 36
    for i in range(total_triangles):
        colour = get_blue_purple_white_color(i, total_triangles)
        length = 35 + i * 0.5

        pen.penup()
        pen.goto(0, 0)
        pen.setheading(i * 6)
        pen.pencolor(colour)
        pen.pendown()

        for _ in range(3):
            pen.forward(length)
            pen.left(120)

    screen.update()

    print("Turtle drawing finished.")
    print("Take a screenshot, then click the drawing window to continue.")

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
            print("Bot: Goodbye! Thank you for chatting with me, and I hope you have a great day.")
            break

        elif not question:
            print("Bot: Please enter a question so I can help you.")

        else:
            words = re.findall(r"[a-z]+", question)

            if "hku" in words:
                print("Bot: HKU stands for the University of Hong Kong. It is a well-known university with strong teaching and research in many fields, including engineering, science, medicine, and business.")

            elif "robot" in words or "robots" in words:
                print("Bot: A robot is a machine designed to perform tasks automatically or semi-automatically. Robots are often used in factories, hospitals, homes, and research laboratories to improve efficiency and reduce human effort.")

            elif "jetson" in words:
                print("Bot: NVIDIA Jetson is a compact computing platform for edge AI and robotics. It is widely used for projects such as computer vision, autonomous systems, and smart devices because it can run AI models efficiently.")

            elif "ai" in words:
                print("Bot: AI means artificial intelligence. It refers to computer systems that can perform tasks such as learning, reasoning, recognizing patterns, and making decisions in ways that resemble human intelligence.")

            elif "human" in words or "humans" in words:
                print("Bot: A human is a person with the ability to think, learn, communicate, and create. Humans are different from machines because they have emotions, self-awareness, and complex social relationships.")

            else:
                print("Bot: Sorry, I can answer questions about HKU, robot, jetson, AI, and human. Please try asking about one of these topics.")

# =========================================
# Main Program
# =========================================

if __name__ == "__main__":
    draw_pattern()
    qa_bot()
