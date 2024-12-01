from turtle import Turtle


SEGMENT_SIZE = 20
STARTING_POSITIONS = [(0, 0), (-SEGMENT_SIZE, 0), (-SEGMENT_SIZE * 2, 0)]
MOVE_DISTANCE = 20

UP_DIRECTION = 90
DOWN_DIRECTION = 270
LEFT_DIRECTION = 180
RIGHT_DIRECTION = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.up()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x_cor = self.segments[segment_number - 1].xcor()
            new_y_cor = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x_cor, new_y_cor)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN_DIRECTION:
            self.head.seth(UP_DIRECTION)

    def down(self):
        if self.head.heading() != UP_DIRECTION:
            self.head.seth(DOWN_DIRECTION)

    def right(self):
        if self.head.heading() != LEFT_DIRECTION:
            self.head.seth(RIGHT_DIRECTION)

    def left(self):
        if self.head.heading() != RIGHT_DIRECTION:
            self.head.seth(LEFT_DIRECTION)
