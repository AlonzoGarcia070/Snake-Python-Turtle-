from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('light blue')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()

# class Head(Turtle):
#   def __init__(self, screen, body):
#     super().__init__()
#     self.alive = True

class Head(Turtle):
  def __init__(self,screen):
    super().__init__()
    self.ht()
    self.speed(0)
    self.color("brown")
    self.penup()
    self.setheading(90)
    self.shape("turtle")
    self.alive = True
    self.st()
    screen.onkeypress(self.turn_left, "Left")
    screen.onkeypress(self.turn_right, "Right")
    screen.onkeypress(self.up, "Up")
    screen.onkeypress(self.down, "Down")

  def turn_left(self):
    self.left(10)

  def turn_right(self):
    self.right(10)

  def down(self):
    self.down(10)

  def up(self):
    self.up(10)

  def up(self):
    global player
    player.setheading(90)
    if player.ycor()!=240:
        player.sety(player.ycor()+10)
  def down(self):
    global player
    player.setheading(-90)
    if player.ycor()!=-240:
      player.sety(player.ycor()-10)

  def left(self):
    global player
    player.setheading(180)
    if player.xcor()!=-240:
        player.setx(player.xcor()-10)

  def right(self):
    global player
    player.setheading(0)
    if player.xcor()!=240:
        player.setx(player.xcor()+10)

  def move(self):
    self.forward(20)
    if t.xcor() > 240 or t.xcor() < -240 or t.ycor()> 240 or t.ycor()<-240:
        self.die()

  def die(self):
    pass

class Segment(Turtle):
  def __init__(self, other):
    super().__init__()
    pass

  def move(self, other):
    pass

class Apple(Turtle):
  def __init__(self):
    super().__init__()
    self.ht()
    self.speed(0)
    self.color("red")
    self.shape("circle")
    self.penup()
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    self.goto(x,y)
    self.setheading(90)
    self.st()

  def relocate(self):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    self.goto(x,y)



def update():
  if head.alive:
    head.move()

    if head.distance(apple) <20:
      apple.relocate()

  screen.ontimer(update, 120)

# while head.alive:

screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
screen.listen()
screen.onkey(update, "space")


head = Head(screen)
body = [head]
apple = Apple()

screen.exitonclick()