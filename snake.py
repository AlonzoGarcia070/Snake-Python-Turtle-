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
    
class Head(Turtle):
  def __init__(self, screen, body):
    super().__init__()
    self.alive = True
    self.shape("square")
    self.color("green")
    self.pu
    self.goto(0,0)
    self.direction("up","down","left","right")
    
  def up(self):
    global player
    player.setheading(90)
    if player.ycor()!=240:
        player.sety(player.ycor()+10)
        if player.heading==270:
          player.setheading!=90

  def down(self):
    global player
    player.setheading(-90)
    if player.ycor()!=-240:
      player.sety(player.ycor()-10)
      if player.heading==-90:
        player.setheading!=270

  def left(self):
    global player
    player.setheading(180)
    if player.xcor()!=-240:
        player.setx(player.xcor()-10)
        if player.heading==180:
          player.setheading!=0

  def right(self):
    global player
    player.setheading(0)
    if player.xcor()!=240:
        player.setx(player.xcor()+10)
        if player.heading==0:
          player.setheading!=180

  def move(self):
    self.forward(20)
    if t.xcor() > 240 or t.xcor() < -240 or t.ycor()> 240 or t.ycor()<-240:
        self.die()
        self.ht

  def die(self):
    pass


class Segment(Turtle):
  def __init__(self, other):
    super().__init__()


  def move(self):
    self.forward(4)
    if self.xcor() > 230 or self.xcor() < -230:
      self.setheading(180 - self.heading())
    if self.ycor() > 230 or self.ycor() < -230:
      self.setheading(-self.heading())


class Apple(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("red")
    self.pu
    self.goto(random.randint(-230,230), random.randint(-230,230))

  def relocate(self):
    self.goto(random.randint(-230,230), random.randint(-230,230))

  def update():
    if head.alive:
      head.move()

      if head.distance(apple) <20:
        apple.relocate()

  # Screen.ontimer(update, 120)

# while head.alive:





screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
screen.listen
screen.onkey(create_player, "space" )
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(right, "Right")
screen.onkeypress(left, "Left")

# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()

body = []








screen.exitonclick()
