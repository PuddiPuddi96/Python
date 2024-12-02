from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboar

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

PADDLE_X_POS = SCREEN_WIDTH // 2 - 30
PADDLE_Y_POS = 0

TOP_WALL = SCREEN_HEIGHT // 2 - 20
DOWN_WALL = -SCREEN_HEIGHT // 2 + 15

def set_paddle_key(a_screen: Screen, a_paddle: Paddle, key_to_go_up, key_to_go_down):
    a_screen.onkey(fun=a_paddle.go_up, key=key_to_go_up)
    a_screen.onkey(fun=a_paddle.go_down, key=key_to_go_down)

def set_up_screen(a_screen: Screen):
    a_screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    a_screen.title("Pong")
    a_screen.bgcolor("black")
    a_screen.listen()
    a_screen.tracer(0)

def check_wall_collision(ball: Ball):
    if ball.ycor() > TOP_WALL or ball.ycor() < DOWN_WALL:
        ball.bounce(on_y=True)

def check_paddle_collision(ball: Ball, l_paddle:Paddle,  r_paddle: Paddle):
    #TODO MAKE COSTANT
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce(on_x=True, on_paddle=True)

def check_paddle_miss_ball(ball: Ball):
    if ball.xcor() > PADDLE_X_POS + 10:
        ball.reset_position(go_to_left=True)
        scoreboard.score_point(to_left=True)
    if ball.xcor() < -PADDLE_X_POS + 10:
        ball.reset_position(go_to_right=True)
        scoreboard.score_point(to_right=True)

screen = Screen()
set_up_screen(screen)

right_paddle = Paddle((PADDLE_X_POS, PADDLE_Y_POS))
left_paddle = Paddle((-PADDLE_X_POS, PADDLE_Y_POS))

set_paddle_key(screen, right_paddle, key_to_go_up="Up", key_to_go_down="Down")
set_paddle_key(screen, left_paddle, key_to_go_up="w", key_to_go_down="s")

ball = Ball(screen_height=SCREEN_HEIGHT, screen_width=SCREEN_WIDTH)

scoreboard = Scoreboar()

game_is_on = True
while game_is_on:
    screen.update()
    sleep(ball.move_speed)
    ball.move()

    check_wall_collision(ball)
    check_paddle_collision(ball=ball, l_paddle=left_paddle, r_paddle=right_paddle)
    check_paddle_miss_ball(ball)

screen.exitonclick()
