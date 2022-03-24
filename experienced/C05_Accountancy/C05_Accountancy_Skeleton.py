"""
Find a sublist of the list that sums up to the given total
"""

### INPUT - DO NOT TOUCH ###
possibilities = list(map(int, input().split()))
total = int(input())
### END INPUT ###

def accountancy(possibilities, total):
    #TODO
    pass

### OUTPUT - DO NOT TOUCH ###
answer = sorted(accountancy(possibilities, total), reverse=True) # Make 'answer' a list containing a (sorted) viable combination of values.
print(' '.join(map(str, answer)))
### END OUTPUT ###

### EXAMPLE INPUT - YOU MAY COPY THIS INTO YOUR TERMINAL
### 58 180 350 94 220 52 106 202 545 79 32 33
### 668

### EXAMPLE OUTPUT - UNCOMMENT THIS LINE TO CHECK YOUR CODE
### 545 58 33 32

