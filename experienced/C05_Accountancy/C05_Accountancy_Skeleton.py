"""
Find a sublist of the list that sums up to the given total
"""
import copy
### INPUT - DO NOT TOUCH ###
possibilities = list(map(int, input().split()))
total = int(input())
### END INPUT ###

def accountancy(possibilities, total):
    answer = answer_backtracking(total, possibilities)
    return answer

def answer_backtracking(total, list_numbers):
    for number in list_numbers:
        new_list = copy.deepcopy(list_numbers)
        new_list.remove(number)
        new_total = total-number

        if new_total == 0:
            return [number]
        elif new_total<0:
            pass
        elif new_total > 0:
            if len(list_numbers)==1:
                return []
            answer = answer_backtracking(new_total, new_list)
            if answer == []:
                pass
            else:
                answer.append(number)

                return answer


    return []
 

### OUTPUT - DO NOT TOUCH ###
answer = sorted(accountancy(possibilities, total), reverse=True) # Make 'answer' a list containing a (sorted) viable combination of values.
print(' '.join(map(str, answer)))
### END OUTPUT ###

### EXAMPLE INPUT - YOU MAY COPY THIS INTO YOUR TERMINAL
### 58 180 350 94 220 52 106 202 545 79 32 33
### 668

### EXAMPLE OUTPUT - UNCOMMENT THIS LINE TO CHECK YOUR CODE
### 545 58 33 32

