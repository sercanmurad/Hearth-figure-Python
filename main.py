import turtle

turtle.speed(100)
turtle.bgcolor("black")
turtle.pensize(5)
def heart():
  for i in range(200):
    turtle.right(1)
    turtle.forward(1)

turtle.color('red','red')
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
heart()
turtle.left(120)
heart()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()
turtle.done()