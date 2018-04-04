import Screen
import GameObject
import math
class GameManager():
    def __init__(self):
        pass
    def RunGame(self):
        frame = Screen.Screen(400,300,"Space Invaders")
        frame.Open()
        frame.GameBorder(4,200,150)
        self.player = GameObject.GameObject(0,-130)
        self.player.Create("Player")
        self.enemy1 = GameObject.GameObject(-185,130)
        self.enemy1.Create("Enemy")
        self.bullet = GameObject.GameObject(self.player.player.xcor(),-130)
        self.bullet.Create("Bullet")
        frame.frame.listen()
        frame.frame.onkeypress(self.playerMoveLeft,"Left")
        frame.frame.onkeypress(self.playerMoveRight,"Right")
        frame.frame.onkey(self.playerShot, "space")
        self.GameLoop()
        frame.frame.mainloop()
    def playerMoveLeft(self):
        xPos = self.player.player.xcor()
        xPos -= self.player.playerSpeed
        if(xPos < -185 ):
            xPos = -185
        self.player.player.setx(xPos)
    def playerMoveRight(self):
        xPos = self.player.player.xcor()
        xPos += self.player.playerSpeed
        if(xPos > 185):
            xPos = 185
        self.player.player.setx(xPos)
    def GameLoop(self):
        while True:
            xPos = self.enemy1.enemy.xcor()
            yPos = self.enemy1.enemy.ycor()
            xPos += self.enemy1.enemySpeed
            if (xPos > 185 or xPos < -185):
                self.enemy1.enemySpeed *= -1
                yPos -= self.enemy1.enemyDrop
            if not self.bullet.fireReady:
                bulletY = self.bullet.bullet.ycor()
                bulletY += self.bullet.bulletSpeed
                self.bullet.bullet.sety(bulletY)
            if self.bullet.bullet.ycor() > 130:
                self.bullet.bullet.hideturtle()
                self.bullet.fireReady = True
            if self.collideChecker(self.bullet,self.enemy1):
                self.bullet.bullet.hideturtle()
                self.bullet.fireReady = True
                self.bullet.bullet.setposition(self.player.player.xcor(),self.player.player.ycor()+10)
            self.enemy1.enemy.setx(xPos)
            self.enemy1.enemy.sety(yPos)
    def playerShot(self):
        if self.bullet.fireReady:
            self.bullet.fireReady = False
            x = self.player.player.xcor()
            y = self.player.player.ycor()+10
            self.bullet.bullet.setposition(x,y)
            self.bullet.bullet.showturtle()
    def collideChecker(self,turtle1,turtle2):
        distance = math.sqrt(math.pow(turtle1.bullet.xcor() - turtle2.enemy.xcor(),2)+math.pow(turtle1.bullet.ycor() - turtle2.enemy.ycor(),2))
        if distance < 15:
            return True
        else:
            return False



