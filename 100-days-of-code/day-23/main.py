from turtle import Turtle, Screen
from time import sleep
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

PLAYER_STARTING_POSITION = (0, -SCREEN_WIDTH // 2 + 20)
PLAYER_FINISH_LINE_Y = SCREEN_WIDTH // 2 - 20

CAR_X_COR_STARTING_POSITION = SCREEN_WIDTH // 2
CAR_Y_UP_RANGE = SCREEN_HEIGHT // 2 - 50
CAR_Y_DOWN_RANGE = -SCREEN_HEIGHT // 2 + 50

SCOREBOARD_POSITION = (-SCREEN_WIDTH // 2 + 20, SCREEN_HEIGHT // 2 - 40)

# LEFT_MARGIN = (-SCREEN_WIDTH // 2) + 10
# RIGHT_MARGIN = (SCREEN_WIDTH // 2) - 10
# TOP_MARING = (SCREEN_HEIGHT // 2) - 10
# DOWN_MARING = (-SCREEN_HEIGHT // 2) + 20



def set_up_screen(a_screen: Screen):
    a_screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    a_screen.title("Crossy road")
    a_screen.bgcolor("grey")
    a_screen.listen()
    a_screen.tracer(0)

def check_collision(cars, player):
    for car in cars:
        if car.distance(player) < 20:
            return True
    return False

            


# def draw_lines():
#     for y_position in range(DOWN_MARING, TOP_MARING, 130):
#         for x_position in range(LEFT_MARGIN, RIGHT_MARGIN, 80):
#             line = Turtle(shape="square")
#             line.color("white")
#             line.shapesize(stretch_wid=0.5, stretch_len=2.5)
#             line.penup()
#             line.goto(x_position, y_position)


screen = Screen()
set_up_screen(screen)

player = Player(starting_position=PLAYER_STARTING_POSITION, finish_line=PLAYER_FINISH_LINE_Y)
screen.onkey(key="Up", fun=player.go_up)
# draw_lines()
# car = Car(screen=screen)

car_manager = CarManager(x_cor_starting_position=CAR_X_COR_STARTING_POSITION, y_cor_down_range=CAR_Y_DOWN_RANGE, y_cor_up_range=CAR_Y_UP_RANGE)

scoreboard = Scoreboard(position=SCOREBOARD_POSITION)

game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()

    if check_collision(cars=car_manager.cars, player=player):
        game_is_on = False
        scoreboard.game_over()
    
    if player.is_at_finish_line(PLAYER_FINISH_LINE_Y):
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
