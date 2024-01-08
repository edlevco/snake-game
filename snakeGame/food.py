from turtle import Turtle

class Food:
    def __init__(self, xcor, ycor):
        self.xcor = xcor
        self.ycor = ycor
        self.createFood
        self.changeColor

    def createFood(self):
        food = Turtle(shape = "square")
        food.penup()
        food.color("green")
        food.goto(self.xcor, self.ycor)
    def changeColor(self):
        bomb = Turtle(shape = "square")
        bomb.penup()
        bomb.color("red")
        bomb.goto(self.xcor, self.ycor)



    
        

        

  

    
    
        