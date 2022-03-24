### OBJECTIVE ###
"""
Cars are no longer driven by humans in this day and age. Now that all cars are self-driven we can perfectly control
traffic by just  making sure the cars evenly distribute along every road. Consider a city with a checkerboard street
pattern. The grid has a 2x3 size (building blocks, so there are 3x4 streets).
_______
| | | |       N
_______      W E
| | | |       S
_______  Note: Check the pdf for a clearer visualisation

You need to calculate how many routes there are starting from the top left and ending in the bottom right, while only
being able to go south and to east.
"""

### INPUT - DO NOT TOUCH ###
size = eval(input())
### END INPUT ###


def lattice(size):
    # return goFromTo((0,0), size)
    if size == (0,0):
        return 1
    
    if size[0] > 0:
        if size[1] > 0:
            return lattice((size[0]-1, size[1])) + lattice((size[0], size[1]-1))
        else:
            return lattice((size[0]-1, size[1]))
    elif size[1] > 0:
        return lattice((size[0], size[1]-1))


### OUTPUT - DO NOT TOUCH ###
result = lattice(size)
print(result)
### END OUTPUT ###


### EXAMPLE INPUT - YOU MAY COPY THIS INTO YOUR TERMINAL ###
### (3, 2) ###

### EXAMPLE OUTPUT - YOU MAY UNCOMMENT THESE LINES TO CHECK YOUR CODE ###
# assert result == 10