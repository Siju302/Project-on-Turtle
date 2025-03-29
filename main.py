import turtle

turtle.Screen().bgcolor("lightgreen")
board = turtle.Turtle()

# this is a hexagon

for i in range(6):
    turtle.fillcolor("lightpink")
    turtle.pendown()
    turtle.forward(100)
    turtle.left(60)
    turtle.penup()

# Define rectangle dimensions
length = 100
width = 50

# Draw the rectangle
turtle.fillcolor("lightblue")
turtle.pendown()
turtle.forward(length)
turtle.left(90)
turtle.forward(width)
turtle.left(90)
turtle.forward(length)
turtle.left(90)
turtle.forward(width)
turtle.left(90)
turtle.penup()

# Set the side length of the triangle
side_length = 100

# Draw the triangle
for _ in range(3):
    turtle.fillcolor("orange")
    turtle.pendown()
    turtle.forward(side_length)
    turtle.left(120)

turtle.done()