# Exercise: Plant Simulation

# Description: 
# This program simulates the growing patterns of two different plants: A and B. It starts with a user provided
# starting garden, a user provided number of generations to grow for, and a user provided neighborhood side if
# the plant being grown is plant B. The program prints the gardens including the starting garden along with the 
# number of dormant, small, and big plants if applicable.

# Returns the number of small plants (*) in this garden.
# garden: a string containing a row of plants.
def count_small(garden):
    cnt = 0
    for i in garden:
        if i == '*':
            cnt += 1
    return cnt

# Returns the number of big plants (^) in this garden.
# garden: a string containing a row of plants.
def count_big(garden):
    cnt = 0
    for i in garden:
        if i == '^':
            cnt += 1
    return cnt

# Returns the number of dormant plants (.) in this garden.
# garden: a string containing a row of plants.
def count_dormant(garden):
    cnt = 0
    for i in garden:
        if i == '.':
            cnt += 1
    return cnt

# Creates the next generation of a garden of Plant A from the current generation.
# garden: a string containing a row of plants.
# Returns a string containing the next generation of the garden.  This string should
# be the same length as the previous generation.
def next_generation_A(garden):
    newgarden = ""  
    for i in range(len(garden)):
        # makes sure that the leftmost and rightmost plants are always dormant
        if i == 0 or i == (len(garden) - 1):
            newgarden += '.'
        elif (garden[i] == '.' or garden[i] == '*') and (garden[i - 1] == '*' and garden[i + 1] != '*'):
            newgarden += '*'
        elif (garden[i] == '.' or garden[i] == '*') and (garden[i + 1] == '*' and garden[i - 1] != '*'):
            newgarden += '*'
        elif (garden[i] == '.' or garden[i] == '*') and (garden[i + 1] == '*' and garden[i - 1] == '*'):      
            newgarden += '.'
        elif (garden[i] == '.' or garden[i] == '*') and (garden[i + 1] == '.' and garden[i - 1] == '.'):      
            newgarden += '.'                                                     
    return newgarden

# Runs the simulation for plant A for the given number of generations, given a
# starting garden. Note that this function doesn't return anything.
def run_garden_A(garden, generations):
    dorm = count_dormant(garden)
    small = count_small(garden)
    # prints the starting garden
    print("{} {} {}".format(garden, dorm, small))
    # prints the gardens of the number of generations requested
    for i in range(generations):
        garden = next_generation_A(garden)
        dorm = count_dormant(garden)
        small = count_small(garden)
        print("{} {} {}".format(garden, dorm, small))

# Creates the next generation of a garden of Plant B from the current generation.
# garden: a string containing a row of plants.
# nsize: the size of the neighborhood that Plant B will use.
# Returns a string containing the next generation of the garden.  This string should
# be the same length as the previous generation.
def next_generation_B(garden, nsize):
    newgarden = ""  
    for i in range(len(garden)):
        ngarden = garden[(i-nsize):(i+nsize+1)]
        # makes sure that the certain number of leftmost and certain number of rightmost plants are always dormant. The number
        # is determined by the neighborhood size
        if i in range(nsize) or i in range((len(garden) - nsize), len(garden)):
            newgarden += '.'
        elif garden[i] == '^' and (count_big(ngarden) + count_small(ngarden)) % 2 == 0:
            newgarden += '*'
        elif garden[i] == '^' and (count_big(ngarden) + count_small(ngarden)) % 2 != 0:               
            newgarden += '^'
        elif garden[i] == '*' and (count_big(ngarden) + count_small(ngarden)) % 2 == 0:
            newgarden += '.'
        elif garden[i] == '*' and (count_big(ngarden) + count_small(ngarden)) % 2 != 0:               
            newgarden += '^'
        elif garden[i] == '.' and (count_big(ngarden) + count_small(ngarden)) % 2 == 0:
            newgarden += '.'
        elif garden[i] == '.' and (count_big(ngarden) + count_small(ngarden)) % 2 != 0:               
            newgarden += '*'                                   
    return newgarden

# Runs the simulation for plant B for the given number of generations, given a
# starting garden. nsize is the size of the neighborhood. 
# Note that this function doesn't return anything.
def run_garden_B(garden, nsize, generations):
    dorm = count_dormant(garden)
    small = count_small(garden)
    big = count_big(garden)
    # prints the starting garden
    print("{} {} {} {}".format(garden, dorm, small, big))
    # prints the gardens of the generations requested
    for i in range(generations):
        garden = next_generation_B(garden, nsize)
        dorm = count_dormant(garden)
        small = count_small(garden)
        big = count_big(garden)
        print("{} {} {} {}".format(garden, dorm, small, big))

def main():
    ptype = input("Are you growing plant A or B? ")
    strt_garden = input("What is the starting garden? ")
    sidenum = int(input("How many dormant plants are on either side? "))
    numgens = int(input("How many generations do you want to see? (not including the first) "))
    # concatenates the true starting garden depending on the number of dormant plants on each side
    garden = ('.' * sidenum) + strt_garden + ('.' * sidenum)
    # if the plant type is A it runs the garden simulator with no further givens
    if ptype == 'A':
        run_garden_A(garden, numgens)
    # if the plant type is B it requests the neighborhood size and then runs the garden simulator
    else:
        nsize = int(input("What is the neighborhood size? "))
        run_garden_B(garden, nsize, numgens)

main()