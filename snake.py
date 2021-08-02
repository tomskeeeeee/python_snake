from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# default move distance starts is 20, can speed up or slow down by changing this
move_distance = 20

# directions - east is 0, moves ccw
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # creates initial 3 segments, first segment is at 0, 0
        first_segments = []
        for position in STARTING_POSITIONS:
            self.grow(position)

        return first_segments

    def move(self):
        # for seg_num in range(start=len(segments)-1, stop=0, step=-1):
        # range does not allow keyword arguments, but above is logic used
        for seg_num in range(len(self.segments) - 1, 0, -1):
            seg_in_front = self.segments[seg_num - 1]
            new_x = seg_in_front.xcor()
            new_y = seg_in_front.ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)

# do not allow snake to turn onto itself, that would kill it
# handle turning on itself separately
    def up(self):
        # Only move if not turning onto itself
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def grow(self, position):
        rect = Turtle("square")
        rect.color("white")
        rect.penup()
        rect.setposition(position)
        self.segments.append(rect)

    def extend(self):
        self.grow(self.segments[-1].position())

    def reset(self):
        # move old snakes off the scree
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]