from turtle import Screen, Turtle
import turtle
import time
import random

segments = []

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
segments.append(new_segment)

#Comida // 
food = turtle.Turtle("circle")
food.color("red")
food.penup()
x = random.randint(-280, 280)
y = random.randint(-280, 280)
food.goto(x, y) #Posiciona la comida en una posición aleatoria

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

screen.listen()

while True:
    screen.update() #Actualiza la animación
    time.sleep(0.3)

# Detectar toque comida
    if new_segment.distance(food) < 15:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y) #Mueve la comida a una posición aleatoria

        next_segment = turtle.Turtle("square")
        next_segment.color("white")
        next_segment.penup()
        segments.append(next_segment)

    # Hacer que los segmentos sigan al primero
    if len(segments) > 1:
        for i in range(len(segments) - 1, 0, -1):
            segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor()) #Mueve el segmento a la posición del anterior


    new_segment.forward(20)

screen.exitonclick()