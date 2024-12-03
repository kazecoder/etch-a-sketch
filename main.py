
import turtle as t

turtle = t.Turtle()
screen = t.Screen()

t.colormode(255)


def move_forward():
    turtle.forward(10)

def move_back():
    turtle.back(10)

def turn_left():
    turtle.setheading(turtle.heading()+10)

def turn_right():
    turtle.setheading(turtle.heading()-10)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()

screen.onkey(move_forward,"w")
screen.onkey(move_back,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")

screen.exitonclick()



