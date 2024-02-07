from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_POSITION_Y = 280


class Player(Turtle):
    def __init__(self):
      super().__init__()
      self.penup()
      self.shape("turtle")
      self.color("green")
      self.goto_start_position()
    def move(self):
       self.forward(MOVE_DISTANCE)
    def reached_finish_line(self):
       if self.ycor() > FINISH_POSITION_Y:
          return True
       else:
          return False
    def goto_start_position(self):
       self.goto(STARTING_POSITION)
       self.setheading(90)