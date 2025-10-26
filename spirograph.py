from turtle import Turtle, Screen, colormode
import random

from rgb_colors import RgbColors

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Spirograph")

dess = Turtle()
CIRCLES_count = 50
SIZE = 10

color_generator = RgbColors()
colormode(255)

def draw_spiro(size_gap):
    for _ in range(int(360 / size_gap)):
        dess.speed(0)
        dess.color(color_generator.create_rgb())
        dess.circle(CIRCLES_count)
        dess.setheading(dess.heading() + size_gap)

draw_spiro(SIZE)