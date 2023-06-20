# Exercise : Image Filter

# Description: 
# This program receives an input file to read that translates RGB pixels to an image. The program allows the reader 
# to choose one of the available filters to apply to the file and writes the new RGB values to a new output file
# and prints the filtered picture out. 

from cs1.ppm import display_ppm
from cs1.notebooks import *

#This function returns a new filename based on the original and a filter.
#Parameters:
#    original_filename: The original name of the file: something.ppm
#    filter: The filter that was applied (an integer 1-9)
#Returns:
#    A new filename based on the filter.
def make_output_filename(original_filename, filter):
    mods = ['negate_red', 'negate_green', 'negate_blue',
            'negate_all', 'remove_red', 'remove_green',
            'remove_blue', 'flip_horizontally', 'grayscale']
    temp_name = ''
    for i in original_filename:
        if i == '.':
            break
        temp_name += i
    return temp_name + '_' + mods[filter - 1] + '.ppm'

  
# This function takes in a list and negates each value in the list
# To negate a value, subtract the value from 255
# Parameters: lst, a 1-D list of integers
# Returns: a list with the modified values (negatives of the original values)
def negate(lst):
    for i in range(len(lst)):
        lst[i] = 255 - lst[i] 
    return lst

# This function takes in a list and flattens each value in the list
# To flatten a value, set it equal to zero 
# Parameters: lst, a 1-D list of integers
# Returns: a list of the same length as (lst) with all zeros
def flatten(lst):
    for i in range(len(lst)):
        lst[i] = 0 
    return lst

# This function takes in a list and reverses the order of the list
# Parameters: lst, a 1-D list of integers
# Returns: the original list in reverse order
def flip(lst):
    new_lst = []
    for i in range(len(lst) - 1, -1, -1):
        new_lst.append(lst[i])
    return new_lst

# This function takes in three 1-D lists, and returns 3 lists that contain the average 
# of the original values at each index
# To calculate the new value for each list, we need to take the average of the values
# and replace the value with the average in all 3 lists (these values must be integers)
# Example: red[0] = 30, green[0] = 100, blue[0] = 74, average = (30 + 100 + 74) / 3 = 68
# so we set red[0] = 68, green[0] = 68 and blue[0] = 68.
# Hint: Use parallel lists
# Parameters: red, green, blue (3 1-D lists with the same number of elements in them)
# Returns: a list of the same length, whose values are averages.
def grayscale(red, green, blue):
    new_lst = []
    for i in range(len(red)):
        new_lst.append(int(((red[i] + green[i] + blue[i]) / 3)))
    return new_lst

# This function copies the first 3 lines of input into output
# Parameters: input_file (fileObject that you're reading from),
#             output_file (fileObject that you're writing to)
# Returns: None
def process_header(input_file, output_file):
    for i in range(3):
        line = input_file.readline()
        output_file.write(line)

# This function applies the specified filter to each pixel in input, writing it to output.
# Parameters: input_file: the input file with the header already read
#             output_file: the output file with the header already written
#             filter: the filter to apply
# Returns: None
def process_body(input_file, output_file, filter):
    for line in input_file:
        line = line.rstrip()
        red = []
        green = []
        blue = []
        values = line.split(' ')
        for i in range(0, len(values), 3):
            red.append(int(values[i]))
        for i in range(1, len(values), 3):
            green.append(int(values[i]))
        for i in range(2, len(values) + 1, 3):
            blue.append(int(values[i]))
        if filter == 1:
            red = negate(red)
        elif filter == 2:
            green = negate(green)
        elif filter == 3:
            blue = negate(blue)
        elif filter == 4:
            red = negate(red)
            green = negate(green)
            blue = negate(blue)
        elif filter == 5:
            red = flatten(red)
        elif filter == 6:
            green = flatten(green)
        elif filter == 7:
            blue = flatten(blue)
        elif filter == 8:
            red = flip(red)
            green = flip(green)
            blue = flip(blue)
        else:
            temp = grayscale(red, green, blue)
            red = temp
            green = temp
            blue = temp
        color_string = ""
        for i in range(len(red)):
            color_string += str(red[i]) + ' ' + str(green[i]) + ' ' + str(blue[i]) + ' '
        color_string += '\n'
        output_file.write(color_string)


def main():
    # get input from user
    input_filename = input('PPM file? ')
    mod = int(input("""Select a filter:
    1. Negate red
    2. Negate green
    3. Negate blue
    4. Negate all
    5. Remove red
    6. Remove green
    7. Remove blue
    8. Flip horizontally
    9. Grayscale
    """))
    while mod not in range(1, 10):
        mod = int(input("""Select a valid filter:
    1. Negate red
    2. Negate green
    3. Negate blue
    4. Negate all
    5. Remove red
    6. Remove green
    7. Remove blue
    8. Flip horizontally
    9. Grayscale
    """))
            
    # open the file
    input_file = open(input_filename, 'r')

    # get output filename
    output_filename = make_output_filename(input_filename, mod)
    output_file = open(output_filename, 'w')

    # process the file
    process_header(input_file, output_file)
    process_body(input_file, output_file, mod)

    # close both files, print filename, and display image
    input_file.close()
    output_file.close()
    print('Output file with filter', mod, 'applied is named', output_filename)
    display_ppm(output_filename)
    

    

main()
