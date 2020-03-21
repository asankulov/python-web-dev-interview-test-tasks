from turtle import *


def draw_curve(size, n):
    if n == 0:
        forward(size)
    else:
        draw_curve(size / 3, n - 1)
        left(60)
        draw_curve(size / 3, n - 1)
        right(120)
        draw_curve(size / 3, n - 1)
        left(60)
        draw_curve(size / 3, n - 1)


def draw_koch_snowflake(size, n):
    for i in range(3):
        draw_curve(size, n)
        right(120)


draw_koch_snowflake(400, 3)
done()
