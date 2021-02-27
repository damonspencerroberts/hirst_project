from turtle import Turtle, Screen, colormode
from random import choice, randint

def hirst(image_url):
  t = Turtle()
  t.speed('fastest')
  # hirst project with kanagawa pic
  colormode(255)
  import colorgram
  colors = colorgram.extract(image_url, 30)

  def get_colors(color):
    return (color.rgb.r, color.rgb.g, color.rgb.b)

  new_colors = list(map(get_colors, colors))
  # create 10x10 dots
  # dots should be 20 in size
  # spaced by 50

  def draw_line(dots, spacing): 
    for _ in range(10):
      t.color(choice(new_colors))
      t.pendown()
      t.dot(dots)
      t.penup()
      t.forward(spacing)

  starting_y = -200
  for _ in range(10):
    t.penup()
    t.hideturtle()
    t.setpos(-200, starting_y)
    draw_line(20, 50)
    starting_y += 50

  screen = Screen()
  screen.exitonclick()

# hirst('mounts.jpg')
hirst('kanagawa.jpg')
