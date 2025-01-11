from turtle import Screen, Turtle
import turtle
import time
import random

segments = []


# Funciones para mover la serpiente con las teclas
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

# Pantalla // Configuración pantalla de juego
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # Interrumpe la animación (evitar giro del segmento)


# Serpiente // Configuración serpiente
new_segment = turtle.Turtle()
new_segment.shape("square")
new_segment.color("white")
new_segment.penup()
new_segment.goto(0,0)
segments.append(new_segment)

# Comida // Configuración comida
food = turtle.Turtle("circle")
food.color("red")
food.penup()
x = random.randint(-280, 280)
y = random.randint(-280, 280)
food.goto(x, y) #Posiciona la comida en una posición aleatoria


# Score // Configuración marcador de puntuación
score = turtle.Turtle()
score.color("white")
score.penup()
score.goto(0, 265)
score.hideturtle()
score_board = 0
score.write(f"Score: {score_board}", align="center", font=("Arial", 24, "bold"))

# Movimiento de la serpiente
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen() # Escucha las teclas

# Bucle de juego
game_is_on = True
while game_is_on:
    screen.update() #Actualiza la animación
    time.sleep(0.3)

    # Detectar toque comida // Aumentar tamaño de la serpiente y mover comida a posición aleatoria
    if new_segment.distance(food) < 15:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y) 

        next_segment = turtle.Turtle("square")
        next_segment.color("white")
        next_segment.penup()
        segments.append(next_segment)

        # Actualizar puntuación
        score.clear()
        score_board += 1
        score.write(f"Score: {score_board}", align="center", font=("Arial", 24, "bold"))


    # Hacer que los segmentos sigan al primero
    if len(segments) > 1:
        for i in range(len(segments) - 1, 0, -1):
            segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor()) #Mueve el segmento a la posición del anterior
    new_segment.forward(20)

    # Detectar colisión con la pared
    head = segments[0]
    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        game_is_on = False
        score.goto(0, 0)
        score.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

    # Detectar colisión con la cola
    for segment in segments[1:]:
        if segment == head:
            pass
        elif head.distance(segment) < 10:
            game_is_on = False
            score.goto(0, 0)
            score.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

screen.exitonclick()