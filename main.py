from random import random
from math import floor, sin
from string import ascii_lowercase


# Controls how many times the smooth functions are applied
smooth_amount = 10

# How big the generated pattern should be.
# The size will [size]x[size]
size = 50


# Simple clamp function
def clamp(val:int, min_v:int, max_v:int)->int:
    if val >= max_v:
        return max_v
    if val <= min_v:
        return min_v
    return val


# returns the cell's neighbours in a list
def get_neighbours(matrix:list, x:int, y:int)->list:
    # Get the neighboring cells
    numbers = []
    if x - 1 >= 0:
        numbers.append(matrix[y][x-1])
    if x + 1 < len(matrix[0]):
        numbers.append(matrix[y][x+1])
    if y - 1 >= 0:
        numbers.append(matrix[y-1][x])
    if y + 1 < len(matrix):          
        numbers.append(matrix[y+1][x])

    return numbers


# Uses average smoothing to smoothen out the matrix
def avg_smooth(matrix: list)->list:
    # Smoothen the matrix
    output = []
    for y in range(0,len(matrix)):
        output.append([])
        for x in range(0, len(matrix[0])):
    
            numbers = get_neighbours(matrix, x, y)
            numbers.append(mat[y][x])
                
            # Get the average of the root cell and its neighbours
            avg = sum(numbers) / len(numbers)
            
            # Append it to the matrix
            output[-1].append(avg)

    return output


# A sin smooth function. Just does what the avg_smoot does, but instead of a average
# it uses a sin function
def sin_smooth(matrix:list)->list:

    output = []

    for y in range(0,len(matrix)):
        output.append([])
        for x in range(0, len(matrix[0])):

            numbers = get_neighbours(matrix, x, y)
            numbers.append(matrix[y][x])

            v = sum(numbers)
            v = sin(v)
            v = abs(v)
            output[-1].append(v)

    return output



# Generate a matrix full of random values
mat = []
for _ in range(0, size):
    mat.append([])
    for _ in range(0,size):
        mat[-1].append(random())



# This section smoothens the matrix
for i in range(0, smooth_amount):
    mat = sin_smooth(mat)
    mat = avg_smooth(mat)





# Print the matrix
gradient = "              .,'\"-:+!?&#@"
for y in range(0,size):
    for x in range(0,size):

        # Get the character index
        v = mat[y][x]
        v = v * len(gradient)
        v = floor(v)
        v = clamp(v, 0, len(gradient)-1)


        print(gradient[v], end="")
    print()

