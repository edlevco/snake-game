from scoreboard import Scoreboard
from turtle import Screen
import time
from snake import Snake
from food import Food
import random

snake = Snake()
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake.createSnake()

positions = []
bombs = []




screen.listen()
for i in range(-280, 280, 20):
    positions.append(i)


is_on = True
found = False
food = Food(random.choice(positions), random.choice(positions))
food.createFood()
old_ycor = 0
old_xcor = 0

while is_on:
    screen.onkey(key = "s", fun=snake.turnDown)
    screen.onkey(key = "w", fun=snake.turnUp)
    screen.update()
    time.sleep(0.1)
    screen.onkey(key = "a", fun=snake.turnLeft)
    screen.onkey(key = "d", fun=snake.turnRight)
    
    if round(snake.segments[0].xcor(), 3) == food.xcor and round(snake.segments[0].ycor(), 3) == food.ycor:
        scoreboard.addScore()
        snake.increaseSnake()
        bombCord = (food.xcor, food.ycor)
        bombs.append(bombCord)
        food.changeColor()
        new_xcor = random.choice(positions)
        new_ycor = random.choice(positions)
        food.xcor = new_xcor
        food.ycor = new_ycor
        food.createFood()
        
    snake.move()
    ## checking for bomb losses
    for bomb in bombs:
        if (round(snake.segments[0].xcor(), 3) == bomb[0] and round(snake.segments[0].ycor(), 3) == bomb[1]):
            is_on = False
            break
    
    ## checking for out of bounds loss
    if snake.segments[0].xcor() >=300 or snake.segments[0].xcor() <= -300 or snake.segments[0].ycor() >= 300 or snake.segments[0].ycor() <= -300:
        is_on = False

    ## checking for overlapping loss
    for i in range(1, len(snake.segments)):
        if snake.segments[0].xcor() == snake.segments[i].xcor() and snake.segments[0].ycor() == snake.segments[i].ycor():
            is_on = False
            break

    
    # if not old_xcor == food.xcor and not old_ycor == food.ycor:
    #         bombCord = (old_xcor, old_ycor)
    #         bombs.append(bombCord)
    

        
      



        



screen.exitonclick()