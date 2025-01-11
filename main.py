from turtle import Screen, Turtle
import turtle
import time
import random

def up():
    if new_segment.heading() != 270:
        new_segment.setheading(90)
def down():
    if new_segment.heading() != 90:
        new_segment.setheading(270)
def left():
    if new_segment.heading() != 0:
        new_segment.setheading(180)
def right():
    if new_segment.heading() != 180:
        new_segment.setheading(0)

# Pantalla
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #Interrumpe la animación


#Serpiente
new_segment = turtle.Turtle()
new_segment.shape("square")
new_segment.color("white")
new_segment.penup()
new_segment.goto(0,0)

#Comida
food = turtle.Turtle("circle")
food.color("red")
food.penup()


screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

screen.listen()

while True:
    screen.update() #Actualiza la animación
    new_segment.forward(20)
    time.sleep(0.4)

# Detectar toque de la serpiente con la comida
    if new_segment.distance(food) < 15:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y) #Mueve la comida a una posición aleatoria


screen.exitonclick()