

# TODO Control snake
# TODO Detect collision with food
# TODO Create scoreboard
# TODO Detect collision with wall
# TODO Detect collision with tail
import time
from turtle import Turtle, Screen
from snake import Snake
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# turn off tracer so we can use update method to refresh positions and redraw
screen.tracer(0)

# TODO Create snake body
# 3 squares next to each other 20 pixels each
# first square at 0, 0

snake = Snake()

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

# def create_snake():
#     for position in starting_positions:
#         rect = Turtle("square")
#         rect.color("white")
#         rect.penup()
#         rect.goto(position)
#         segments.append(rect)

# def create_snake():
#     snake_3 = []
#     for index in range(0, 3):
#         rect1 = Turtle("square")
#         rect1.color("white")
#         rect1.setx(index*-20)
#         rect1.sety(0)
#         snake_3.append(rect1)
#     return snake_3

is_game_running = True
# create_snake()
while is_game_running:
    # Move snake all segments together only after all have new position
    screen.update()
    # delay next update by 0.1 seconds
    time.sleep(.1)
    # for seg_num in range(start=len(segments)-1, stop=0, step=-1):
    # range does not allow keyword arguments, but above is logic used
    for seg_num in range(len(segments)-1, 0, -1):
        seg_in_front = segments[seg_num-1]
        new_x = seg_in_front.xcor()
        new_y = seg_in_front.ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)


    # is_game_running = False























screen.exitonclick()

