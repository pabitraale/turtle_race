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

# Loop until is race start is false
while is_race_start:
    for turtle in all_turtles:
        # Declared the winner if turtle exceed x > 270
        if turtle.xcor() > 270:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is winner!!")
            else:
                print(f"You've lose. The {winning_color} turtle won!!")
            is_race_start = False
        # Generate random distance and each turtle move randomly
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()