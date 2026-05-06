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
    pass

  def relocate(self):
    pass

screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()

body = []


screen.exitonclick()






screen.exitonclick()
screen.exitonclick()
