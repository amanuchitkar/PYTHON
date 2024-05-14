import turtle

print(25//5)
print(2 << 2)
print(2 >> 0)
print(2 ^ 2)
print(2 != 2)
print(2 >0)

# Create a turtle object

my_turtle = turtle.Turtle()

# Move the turtle forward
my_turtle.forward(100)

# Turn the turtle right
my_turtle.right(90)

# Move the turtle forward again
my_turtle.forward(50)

# Turn the turtle right again
my_turtle.right(90)

# Move the turtle forward once more
my_turtle.forward(100)

# Turn the turtle right one last time
my_turtle.right(90)

# Move the turtle forward to complete the rectangle
my_turtle.forward(50)

# Hide the turtle
my_turtle.hideturtle()

# Keep the window open
turtle.done()
