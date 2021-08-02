from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# default move distance starts is 20, can speed up or slow down by changing this
move_distance = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.segments = self.create_snake()


    def create_snake(self):
        # creates initial 3 segments, first segment is at 0, 0
        first_segments = []
        for position in STARTING_POSITIONS:
            rect = Turtle("square")
            rect.color("white")
            rect.penup()
            rect.goto(position)
            first_segments.append(rect)
        return first_segments



    def move(self):
        # for seg_num in range(start=len(segments)-1, stop=0, step=-1):
        # range does not allow keyword arguments, but above is logic used
        for seg_num in range(len(self.segments) - 1, 0, -1):
            seg_in_front = self.segments[seg_num - 1]
            new_x = seg_in_front.xcor()
            new_y = seg_in_front.ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(move_distance)
