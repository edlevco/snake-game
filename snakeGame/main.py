from turtle import Turtle, Screen
import time
from snake import Snake

snake = Snake()
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake.createSnake()
screen.listen()


is_on = True
while is_on:
    screen.onkey(key = "w", fun=snake.turnUp)
    screen.onkey(key = "s", fun=snake.turnDown)
    screen.onkey(key = "a", fun=snake.turnLeft)
    screen.onkey(key = "d", fun=snake.turnRight)
    screen.update()
    time.sleep(0.1)
      

    snake.move()

        



screen.exitonclick()