from turtle import Turtle, Screen

t = Turtle()
s = Screen()

def clear():
    t.clear()
    t.up()
    t.home()
    t.down()
    

def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def move_counter_clockwise():
    t.left(10)

def move_clockwise():
    t.right(10)



s.listen()

s.onkey(key="w", fun=move_forwards)
s.onkey(key="s", fun=move_backwards)
s.onkey(key="a", fun=move_counter_clockwise)
s.onkey(key="d", fun=move_clockwise)

s.onkey(key="c", fun=clear)

s.exitonclick()
