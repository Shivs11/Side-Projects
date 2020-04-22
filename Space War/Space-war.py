import os
import turtle
import random
import time

turtle.title("Space War!")
turtle.forward(0)
turtle.speed(0)
turtle.bgcolor("black")
#turtle.bgpic('background.gif')
turtle.tracer(1)
turtle.ht()
#Speeding up the Drawing
turtle.setundobuffer(1)
turtle.tracer(4) #Speeds up the animation

class Sprite(turtle.Turtle): #Child class of the turtle class.
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.forward(0)
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
        self.forward(self.speed)

        # Boundary detection
        if self.xcor() > 290:
            self.setx(290)
            self.right(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.right(60)
        if self.ycor() > 290:
            self.sety(290)
            self.right(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.right(60)

    def isCollision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
        (self.xcor() <= (other.xcor() + 20)) and \
        (self.ycor() >= (other.ycor() - 20)) and \
        (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
            return False


# Class for the player:
class Player(Sprite):#Inherits from the sprite class (Grandchild of the turtle class)
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)#Sprite has been initialised with these parameters
        self.shapesize(stretch_wid = 0.6, stretch_len = 1.1, outline = None)

        self.speed = 4 #Players speed
        self.lives = 3

    def turn_left(self):
        self.left(45)

    def turn_right(self):
        self.right(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1

class Enemy(Sprite):#Inherits from the sprite class (Grandchild of the turtle class)
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)#Sprite has been initialised with these parameters
        self.speed = 6
        self.setheading(random.randint(0, 360))

class Ally(Sprite):#Inherits from the sprite class (Grandchild of the turtle class)
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)#Sprite has been initialised with these parameters
        self.speed = 8
        self.setheading(random.randint(0, 360))

    def move(self):
        self.forward(self.speed)

        # Boundary detection
        if self.xcor() > 290:
            self.setx(290)
            self.left(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.left(60)
        if self.ycor() > 290:
            self.sety(290)
            self.left(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.left(60)


class Missile(Sprite):#Inherits from the sprite class (Grandchild of the turtle class)
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid = 0.3, stretch_len = 0.4, outline = None)
        self.speed = 20
        self.status = "ready"
        #self.hideturtle()

    def fire(self):
        if self.status == "ready": #If the bullet is ready
            self.goto(player.xcor(), player.ycor())
            self.status = "firing"
            self.setheading(player.heading())

    def move(self):
        if self.status == "ready":
            self.goto(-1000, 1000)
        if self.status == "firing":
            self.forward(self.speed)

            # Border Checking
            if self.xcor() < -290 or self.xcor() > 290 or \
            self.ycor()< -290 or self.ycor() > 290:
                self.goto(-1000, 1000)
                self.status = "ready"

class Particle(Sprite):#Inherits from the sprite class (Grandchild of the turtle class)
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid = 0.3, stretch_len = 0.4, outline = None)
        self.goto(-1000, -1000)
        self.frame = 0

    def explode(self, startx, starty):
        self.goto(startx, starty)
        self.setheading(random.randint(0, 360))
        self.frame = 1

    def move(self):
        if self.frame > 0:
            self.forward(10)
            self.frame += 1

        if self.frame > 15:
            self.frame = 0
            self.goto(-1000, -1000)



class Game(): #Class for storing the information about the game and stuff.
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3

    def border_time(self):
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.forward(600)
            self.pen.right(90)
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.pendown()

    def status(self):
        self.pen.undo() #Undoes the pendown function which was called earlier
        message = "Score: {}".format(self.score)
        self.pen.penup()
        self.pen.goto(-300, 310)
        self.pen.write(message, font = ("Arial", 16, "normal"))



game = Game()
game.border_time()

# Showing the game status
game.status()

# enemy = Enemy("circle", "red", -100, 0)
missile = Missile("triangle", "yellow", 0, 0)
#ally = Ally("square", "blue", 100, 0)

# Creating a sprites from the class.
player = Player("triangle", "white", 0 , 0)

enemies = []
for i in range(6):
    enemies.append(Enemy("circle", "red", -100, 0))

allies = []
for i in range(6):
    allies.append(Ally("square", "blue", 100, 0))

particles = []
for i in range(20):
    particles.append(Particle("circle", "orange", 0, 0))

# Keyboard bindings
turtle.listen()
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(player.turn_left, "Left")
turtle.onkey(missile.fire, "space")

# Main game loop
while True:
    turtle.update()
    time.sleep(0.002)
    player.move()
    #enemy.move()
    missile.move()
    #ally.move()

    for enemy in enemies:
        enemy.move()
        # Checking for a Collision
        if player.isCollision(enemy):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            missile.status = "ready"
            game.score -= 100
            game.status()

        # Checking for a collision between enemy and Missile
        if missile.isCollision(enemy):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            game.score += 100
            game.status()
            # Showing the explosion
            for particle in particles:
                particle.explode(missile.xcor(), missile.ycor())

    for ally in allies:
        ally.move()
        if missile.isCollision(ally):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            ally.goto(x,y)
            missile.status = "ready"
            game.score -= 50
            game.status()

    for particle in particles:
        particle.move()

turtle.Screen().exitonclick()
