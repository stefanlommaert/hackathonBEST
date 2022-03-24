### OBJECTIVE
"""
Tambeur is the delivery service for sandwiches we use at Twipe.
For a company event everybody ordered their preferred sandwich, but the list with chosen orders got lost.
Try and match the right sandwich to the right Twipee given these set of dietary constraints:
# Stijn does not eat tomatos nor chicken
# Tobie only eats something that has at most 2 topping different from stijn's. (Symmetric difference is used) (e.g. sandwich club ham and sandwich club cheese differ 3 toppings: ham, cheese and tomato)
# Tom does not eat clubs nor wraps
# Joris only has a budget of 3.7
# Jeroen does not want a sandwich (only wraps and burgers are not served on a sandwich)
# Simon wants at most 2 different toppings
# Eveline and stefanies choice can differ at most 2 toppings, unless the topping is lettuce, that does not count. (Symmetric difference is used)
# Stefanie does not like americain
# Hanne needs club ham or club cheese

Note: The test case will use different combinations of pricing and toppings to get a different outcome.

Write the function get_combination that allocates the sandwiches below to the correct Twipee.

Output is expected as an ordered list of (name, sandwich name) tuples (ordered by name)
"""

### INPUT - DO NOT TOUCH
import itertools

input_names = ["Stijn", "Eveline", "Tobie", "Tom", "Joris", "Jeroen", "Simon", "Stefanie", "Hanne"]
input_tambeur = eval(input())
### END INPUT ###

def get_combination():
    # TODO
    pass

### OUTPUT - DO NOT TOUCH
print(get_combination())
### END OUTPUT

### EXAMPLE INPUT - YOU MAY COPY THIS INTO THE TERMINAL TO TEST YOUR CODE
### [{"name": "sandwich club ham","topping": {"ham", "lettuce"},"price": 4,},{"name": "sandwich club cheese","topping": {"cheese", "lettuce", "tomato"},"price": 3.8}, {"name": "sandwich club americain","topping": {"americain", "tomato"},"price": 5}, {"name": "sandwich tomato mozzarella","topping": {"mozzarella", "pesto","tomato"},"price": 2}, {"name": "sandwich italiano","topping": {"mozzarella", "parma ham", "pesto", "rucola"},"price": 4.6}, {"name": "sandwich crab salad","topping": {"crab salad"},"price": 3.6}, {"name": "sandwich chicken curry","topping": {"chicken curry"},"price": 3.2}, {"name": "veggie burger","topping": {"veggie", "tomato", "rucola"},"price": 4.6}, {"name": "wrap salmon","topping": {"salmon", "herb cheese"},"price": 3.9}]

### EXAMPLE OUTPUT - YOU MAY UNCOMMENT THIS LINE TO CHECK THE INPUT
### assert get_combination() == [('Eveline', 'sandwich club americain'), ('Hanne', 'sandwich club ham'), ('Jeroen', 'veggie burger'), ('Joris', 'sandwich tomato mozzarella'), ('Simon', 'wrap salmon'), ('Stefanie', 'sandwich club cheese'), ('Stijn', 'sandwich crab salad'), ('Tobie', 'sandwich chicken curry'), ('Tom', 'sandwich italiano')]