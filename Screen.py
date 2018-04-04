#Screen Setup
import turtle
import GameObject
class Screen():
    def __init__(self, width,height,title):
        self.height = height
        self.width = width
        self.title = title
    def Open(self):
        self.frame = turtle.Screen()
        self.frame.bgcolor("black")
        self.frame.title(self.title)
    def GameBorder(self,penSize,borderX,borderY):
        self.border = turtle.Turtle()
        self.border.speed(0)
        self.border.color("white")
        self.border.penup()
        self.border.setposition(borderX * -1,borderY* -1)
        self.border.pendown()
        self.border.pensize(penSize)
        for side in range(4):
            if (side % 2 == 0):
                self.border.fd(self.width)
                self.border.lt(90)
            else:
                self.border.fd(self.height)
                self.border.lt(90)
        self.border.hideturtle()



