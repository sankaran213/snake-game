from turtle import Screen, Turtle, down, up, width
from paddle import Paddle
from ball import ball
from scoreboard import scoreboard
import time

screen = Screen()


screen = Screen()
screen.setup(width= 800, height = 600)
screen.bgcolor("black")
screen.title("ping pong")
screen.tracer(0)

r_paddle  = Paddle((350,0))
l_paddle = Paddle((-350,0))
game_ball = ball((0,0))
scoreboad = scoreboard()



screen.listen()
screen.onkey( r_paddle.go_up , "Up")
screen.onkey( r_paddle.go_down , "Down")
screen.onkey( l_paddle.go_up , "w")
screen.onkey( l_paddle.go_down , "s")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    game_ball.move()
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.bounce1()

    if game_ball.distance(r_paddle) < 50 and game_ball.xcor() > 320 or game_ball.distance(l_paddle)< 50 and game_ball.xcor() < -320:
        game_ball.bounce_x()
        
    
    if game_ball.xcor() > 380:
       game_ball.reset_position()
       scoreboad.l_point()


    
    if game_ball.xcor() < -380:
       game_ball.reset_position()
       scoreboad.r_point()

    



screen.exitonclick()
