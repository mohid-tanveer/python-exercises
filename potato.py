# Exercise: Potato Heads

# Description: 
# Draws potato heads. Focuses on learning functions imported from cs1.graphics library

from cs1.graphics import *

# Draw the eyes on a potato of radius 150 pixels.
# Parameters: (centerx, centery): the (x, y) coordinates of the potato center.
# Returns: None
def draw_eyes(centerx, centery):
    set_color("white")
    draw_filled_oval(centerx - 40, centery - 30, 25, 20)
    draw_filled_oval(centerx + 40, centery - 30, 25, 20)
    set_color("SaddleBrown")
    draw_filled_circle(centerx - 40, centery - 30, 12.5)
    draw_filled_circle(centerx + 40, centery - 30, 12.5)
    set_color("black")
    set_line_thickness(5)
    draw_oval(centerx - 40, centery - 30, 25, 20)
    draw_oval(centerx + 40, centery - 30, 25, 20)
    draw_filled_circle(centerx - 40, centery - 30, 6.25)
    draw_filled_circle(centerx + 40, centery - 30, 6.25)
    
# Draw the hair on a potato of radius 150 pixels.
# Parameters: (centerx, centery), the (x, y) coordinates of the potato center.
# Returns: None
def draw_hair(centerx, centery):
    set_color("white")
    draw_filled_rect(centerx - 75, centery - 150, 200, 40)
    set_color("black")
    draw_filled_polygon(centerx - 130, centery - 74.833, centerx - 130, centery - 150, centerx - 100, centery - 140, centerx -       75, centery - 150, centerx - 50, centery - 140, centerx - 25, centery - 150, centerx, centery - 140, centerx + 25, centery -     150, centerx + 50, centery - 140,centerx + 75, centery - 150, centerx + 100, centery - 140, centerx + 130, centery - 150,         centerx + 130, centery - 74.833, centerx - 130, centery - 74.833)

# Draw the mouth on a potato of radius 150 pixels.
# Parameters: (centerx, centery), the (x, y) coordinates of the potato center.
# Returns: None
def draw_mouth(centerx, centery):
    set_color("white")
    draw_filled_oval(centerx, centery + 50, 60, 30)
    set_color_rgb(224, 144, 76)
    draw_filled_rect(centerx - 61, centery + 19, 122, 30)
    set_color("black")
    set_line_thickness(2)
    draw_line(centerx - 40, centery + 50, centerx - 40, centery + 72.361)
    draw_line(centerx - 20, centery + 50, centerx - 20, centery + 78.284)
    draw_line(centerx, centery + 50, centerx, centery + 80)
    draw_line(centerx + 20, centery + 50, centerx + 20, centery + 78.284)
    draw_line(centerx + 40, centery + 50, centerx + 40, centery + 72.361)
    set_color_rgb(205, 92, 92)
    draw_filled_oval(centerx, centery + 17.5, 22, 15)
    
# Change this value to False if you want to stop the potatoes changing locations,
# but I will turn this back on before grading.  Normally you shouldn't need to change this.
MOVE_HEADS = True

# *** DO NOT CHANGE ANY OF THE CODE BELOW. ***
import random

def reset_pen():
    set_color("black")
    set_background_color("white")
    set_line_thickness(1)

def main():
    open_canvas(800, 400)

    # Draw the left potato:
    # Draw a potato-colored circle, centered approximately at (200, 200).
    mj = 0
    if MOVE_HEADS:
        mj = 40
    cx = random.randint(-mj, mj) + 200
    cy = random.randint(-mj, mj) + 200
    set_background_color_rgb(224, 144, 76)
    set_color_rgb(224, 144, 76)
    draw_filled_circle(cx, cy, 150)

    # Draw the features of the left potato.
    reset_pen()
    draw_eyes(cx, cy)
    reset_pen()
    draw_hair(cx, cy)
    reset_pen()
    draw_mouth(cx, cy)
    reset_pen()

    # Draw the right potato:
    # Draw a potato-colored circle, centered approximately at (600, 200).
    cx = random.randint(-mj, mj) + 600
    cy = random.randint(-mj, mj) + 200
    set_color_rgb(224, 144, 76)
    set_background_color_rgb(224, 144, 76)
    draw_filled_circle(cx, cy, 150)

    # Draw the features of the right potato.
    reset_pen()
    draw_eyes(cx, cy)
    reset_pen()
    draw_hair(cx, cy)
    reset_pen()
    draw_mouth(cx, cy)

# Start program.
main()
