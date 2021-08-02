from turtle import Turtle


class Snake:

    # segments = []
    def create_snake(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        segments = []
        for position in starting_positions:
            rect = Turtle("square")
            rect.color("white")
            rect.penup()
            rect.goto(position)
            segments.append(rect)
        return segments

    def __init__(self):
        self.segments = self.create_snake()

    def snake_move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            seg_in_front = self.segments[seg_num - 1]
            new_x = seg_in_front.xcor()
            new_y = seg_in_front.ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
