import turtle
import random

# Function to draw the tree branches
def draw_tree(t, branch_length, left_angle, right_angle, reduction_factor, depth, season):
    if depth == 0:
        return

    t.forward(branch_length)

    # Save state
    position = t.pos()
    heading = t.heading()

    # Draw left branch
    t.left(left_angle)
    t.width(max(1, depth))  # makes the branch thicker near base
    t.color("brown")
    draw_tree(t, branch_length * reduction_factor, left_angle, right_angle, reduction_factor, depth - 1, season)

    # Restore state
    t.penup()
    t.setpos(position)
    t.setheading(heading)
    t.pendown()

    # Draw right branch
    t.right(right_angle)
    t.width(max(1, depth))
    t.color("brown")
    draw_tree(t, branch_length * reduction_factor, left_angle, right_angle, reduction_factor, depth - 1, season)

    # Restore again
    t.penup()
    t.setpos(position)
    t.setheading(heading)
    t.pendown()

    # Draw leaves if at depth 1
    if depth == 1 and season != "winter":
        draw_leaf(t, season)

# Function to draw leaves
def draw_leaf(t, season):
    # Store current state
    pos = t.pos()
    heading = t.heading()

    t.width(1)
    t.penup()
    t.forward(4)
    t.pendown()

    if season == "spring":
        t.color("lightgreen")
    elif season == "summer":
        t.color("forestgreen")
    elif season == "autumn":
        t.color(random.choice(["orange", "red", "gold"]))

    t.begin_fill()
    t.circle(3)
    t.end_fill()

    # Restore state
    t.penup()
    t.setpos(pos)
    t.setheading(heading)
    t.pendown()


# Main function
def main():
    # Get user inputs
    left_angle = float(input("Enter left branch angle for the tree (e.g., 30): "))
    right_angle = float(input("Enter right branch angle for the tree (e.g., 33): "))
    start_length = float(input("Enter starting branch length for the tree (e.g., 100): "))
    reduction_factor = float(input("Enter branch length reduction factor (In range of 0.1 to 1, e.g : 0.5): "))
    depth = int(input("Enter recursion depth (e.g., 5): "))
    season = input("Enter season (spring, summer, autumn, winter): ").strip().lower()

    # Create turtle
    t = turtle.Turtle()
    t.speed('fastest')
    t.shape("turtle")
    t.color("brown")
    t.width(5)

    # Initial position
    t.penup()
    t.goto(0, -250)
    t.left(90)
    t.pendown()

    # Draw the tree
    draw_tree(t, start_length, left_angle, right_angle, reduction_factor, depth, season)

    t.hideturtle()
    turtle.done()

main()
