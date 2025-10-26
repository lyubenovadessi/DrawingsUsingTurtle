from turtle import Turtle, Screen, colormode
from rgb_colors import RgbColors

screen = Screen()
screen.setup(800, 500)
screen.bgcolor("black")
screen.title("Shapes")

dess = Turtle(shape="arrow")
colormode(255)
color_generator = RgbColors()
dess.goto(x=-100, y=150)

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        dess.forward(100)
        dess.right(angle)

for shape_side_n in range(3, 11):
    dess.color(color_generator.create_rgb())
    draw_shape(shape_side_n)

screen.exitonclick()