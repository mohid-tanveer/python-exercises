# Exercise: Connect the Dots

# Description: 
# This program reads lines from a text file of the user's choice given by their input 
# and draws the picture using the instructions. It first starts by reading the canvas size and opens
# a canvas using these values and proceeds to read each line and using its instructions draws the 
# piece.

from cs1.graphics import *
import math

# This function recieves the starting and ending coordinates and draws a dotted line between the coordinates
# Parameters: (x1, y1), (x2, y2) - integer values representing the coordinates of the start and end point of
# the dotted line
# Returns: no value
def draw_dotted_line(x1, y1, x2, y2):
    dist = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    num_circ = (dist / 10)
    num_circ = int(num_circ)
    x_step = (x2 - x1) / num_circ
    y_step = (y2 - y1) / num_circ
    draw_filled_circle(x1, y1, 2)
    for i in range(0, num_circ - 1):
        x1 += x_step
        y1 += y_step
        draw_filled_circle(x1, y1, 2)
    draw_filled_circle(x2, y2, 2)


def main():
    # prompts the user for a file to use
    file_name = input("What file would you like to use? ")
    # opens the file in read mode and reads the first line to get the canvas size by splitting its contents into variables
    file = open(file_name, 'r')
    canvas_size = file.readline()
    canvas_size = canvas_size.rstrip()
    canvas, xcan, ycan = canvas_size.split(" ")
    open_canvas(xcan, ycan)
    set_line_thickness(2)
    for line in file:
        # strips white lines from the line and splits the line into the line type and the end coordinates of the line or where to         # jump to
        line = line.rstrip()
        linetype, x2, y2 = line.split(' ')
        x2 = int(x2)
        y2 = int(y2)
        if linetype == 'jumpto':
            # sets start coordinates to given coordinates from the jumpto instruction
            x1 = x2
            y1 = y2
        elif linetype == 'lineto':
            draw_line(x1, y1, x2, y2)
            x1 = x2
            y1 = y2
        elif linetype == 'dlineto':
            draw_dotted_line(x1, y1, x2, y2)
            x1 = x2
            y1 = y2
            
main()