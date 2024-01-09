from turtle import Turtle, Screen
import random


is_race_start = False
screen = Screen()
# Resize the screen
screen.setup(width=600, height=500)
# Ask user to enter turtle color they are betting on
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# List of y coordinates
y = [25, 75, 125, -25, -75, -125]
all_turtles = []
# Loop to create 6 turtle having 6 different color
for i in range(6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-250, y[i])
    all_turtles.append(new_turtle)
# If user entered turtle color set race start equal ture
if user_bet:
    is_race_start = True