from turtle import Screen
from pong_paddle import Paddle
from pong_ball import Ball
from pong_score import Score
import time

screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

score = Score()
screen.listen()
screen.onkey(r_paddle.p_up, "Up")
screen.onkey(r_paddle.p_down, "Down")
screen.onkey(l_paddle.p_up, "w")
screen.onkey(l_paddle.p_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.b_speed)
    screen.update()
    ball.move()

#wall collision
    if ball.ycor() > 235 or ball.ycor() < -235:
        ball.bounce_y()

#paddle collision
    if ball.distance(r_paddle) < 40 and ball.xcor() > 320 or ball.distance(l_paddle) < 40 and ball.xcor() < -320:
        ball.bounce_x()

#ball paddle miss
    if ball.xcor() > 380:
        score.l_point()
        ball.ball_reset()

    if ball.xcor() < -380:
        score.r_point()
        ball.ball_reset()

screen.exitonclick()
