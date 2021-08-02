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

# Create snake object using Snake class
# Initial snake is 3 squares next to each other 20 pixels each
# first square at 0, 0
snake = Snake()

is_game_running = True
# create_snake()
while is_game_running:
    # Move snake all segments together only after all have new position
    screen.update()
    # delay next update by 0.1 seconds
    time.sleep(.1)
    # moves snake
    snake.move()
























screen.exitonclick()

