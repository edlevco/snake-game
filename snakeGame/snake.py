from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.createSnake

    def createSnake(self):
        for i in range(3):
            new_turtle = Turtle(shape = "square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(STARTING_POSITIONS[i])
            self.segments.append(new_turtle)

    def increaseSnake(self):
        new_turtle = Turtle(shape = "square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(self.segments[0].xcor(), self.segments[0].ycor())
        self.segments.append(new_turtle)

    
        
    def move(self):
        for seg_number in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_number-1].xcor()
            new_y = self.segments[seg_number-1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    
    def turnUp(self):
        if not self.segments[0].heading() == 270:
            self.segments[0].setheading(90)
        

    def turnDown(self):
        if not self.segments[0].heading() == 90:
            self.segments[0].setheading(270)

    def turnRight(self):
        if not self.segments[0].heading() == 180:
            self.segments[0].setheading(0)

    def turnLeft(self):
        if not self.segments[0].heading() == 0:
            self.segments[0].setheading(180)