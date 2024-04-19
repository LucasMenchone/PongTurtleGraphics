from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time


tela = Screen()
tela.bgcolor("black")
tela.setup(width=800,height=600)
tela.title("Pong")
tela.tracer(0) #deactivate animations, but it is necessary to call an update function to keep display running instead

paddle_direito = Paddle(350,0)
paddle_esquerdo = Paddle(-350,0)

ball = Ball()
text = Turtle()

tela.listen()
tela.onkeypress(paddle_direito.go_up, "Up")
tela.onkeypress(paddle_direito.go_down, "Down")
tela.onkeypress(paddle_esquerdo.go_up, "w")
tela.onkeypress(paddle_esquerdo.go_down, "s")

score_paddle_esquerdo = Score()
score_paddle_direito = Score()

score_paddle_direito.move_score_position(150,200)
score_paddle_esquerdo.move_score_position(-150, 200)

central_line = Turtle()

central_line.penup()
central_line.goto(0, 300)
central_line.pendown()
central_line.color("white")
central_line.width(2)
central_line.setheading(-90)

# Draw a center line
for _ in range(30):
    central_line.forward(20)
    central_line.penup()
    central_line.forward(10)  
    central_line.pendown()   

is_on = True

while is_on:
    time.sleep(0.1)
    tela.update()
    ball.ball_movement()

    #collision with ceiling or bottom 
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce()

    #collision with paddle
    if ball.distance(paddle_direito) < 50 and ball.xcor() > 320 or ball.distance(paddle_esquerdo) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #score count
    if ball.xcor() > 350:
        score_paddle_esquerdo.score_up()
        ball.goto(0,0)
    
    if ball.xcor() < -350:
        score_paddle_direito.score_up()
        ball.goto(0,0)

    #game over
    if score_paddle_direito.score >= 5 or score_paddle_esquerdo.score >= 5:
        text = Turtle()
        text.color("white")
        text.hideturtle()
        text.penup()
        text.goto(-150,0)
        text.write("GAME OVER",font=("Impact Regular",36,"normal"))
        is_on = False 

tela.exitonclick()