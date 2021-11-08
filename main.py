import turtle
from turtle import Turtle, Screen
import random

race_on_flag = False
screen = Screen()
screen.setup(width=500, height=400) #intern function resize screen

user_bet = screen.textinput(title="Make your bet", prompt="Choose your turtle (color):")
print(f"Your bet: {user_bet}")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)


if user_bet:
    race_on_flag = True

while race_on_flag:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on_flag = False # zeby nie bylo wiecej zwyciezcow
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win. The {winning_color} turtle is the winner!")
            else:
                print(f"You lose. The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
