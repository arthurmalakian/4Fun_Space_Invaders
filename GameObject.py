import turtle
class GameObject():
    def __init__(self,xPos,yPos):
        self.xPos = xPos
        self.yPos = yPos
    def Create(self,type):
        if(type == "Player"):
            self.player = turtle.Turtle()
            self.player.color("Blue")
            self.player.shape("triangle")
            self.player.penup()
            self.player.speed(0)
            self.player.setposition(self.xPos,self.yPos)
            self.player.setheading(90)
            self.playerSpeed = 15
        elif(type == "Enemy"):
            self.enemy = turtle.Turtle()
            self.enemy.color("Red")
            self.enemy.shape("circle")
            self.enemy.penup()
            self.enemy.speed(0)
            self.enemy.setposition(self.xPos,self.yPos)
            self.enemyDrop = 5
            self.enemySpeed = 2
        elif(type == "Bullet"):
            self.bullet = turtle.Turtle()
            self.bullet.color("yellow")
            self.bullet.shape("circle")
            self.bullet.penup()
            self.bullet.speed(0)
            self.bullet.shapesize(0.3)
            self.bullet.setposition(self.xPos,self.yPos)
            self.bullet.hideturtle()
            self.bulletSpeed = 10
            self.fireReady = True
