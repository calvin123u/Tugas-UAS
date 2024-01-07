import turtle
turtle.shape("turtle")
for a in range(4):
    turtle.forward(100)
    turtle.right(90)
for b in range (1):
    turtle.forward(100)
    turtle.right(90)
for c in range(1):
    turtle.forward(100)
for d in range(2):
    turtle.forward(100)
    turtle.right(90)

turtle.penup()
turtle.setx(200.0)
turtle.pendown()

for e in range(1):
    turtle.right(90)
for f in range(3):
    turtle.forward(100)
    turtle.left(90)
for g in range(2):
    turtle.backward(100)
    turtle.right(90)

turtle.exitonclick()