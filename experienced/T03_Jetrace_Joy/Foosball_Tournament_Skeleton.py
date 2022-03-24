### OBJECTIVE
"""
# Jetrace Joy

Twipe is a very competitive company. They could put that competitive drive to use in a lot of areas, but they chose to do jet races instead of something productive. They do this so often that they can use statistics and leaderboards to estimate how strong each player is.

We can use these strengths to determine the probability that player _A_ beats player _B_: P(_A_ beats _B_) = strength(_A_) / (strength(_A_) + strength(_B_))

Now we want to organize a jetracing tournament with the following properties:
- It's a 1v1 tournament
- It's a knockout tournament

A possible 1v1 knockout tournament could go like this:
# _Matthieu_
#           \_Matthieu_
# _Kasper___/          \
#                       \_Matthieu_
# _Jan______            /
#           \_Jan______/
# _Riccardo_/

The goal is to be able to compute the probability that a given player wins the tournament.
To do this a function `player_wins(player, players)` must be implemented in the following way:
- `player` is the player for which we want to compute the probability of winning the entire tournament
- `players` is the list of all players who participate in the tournament.
    - The length determines how many rounds there are (e.g. a length of 2 means we only have a final. A length of 8 means we have a quarter final, semifinal and final). You can assume the length is always a power of two.
    - The order determines who faces who in the first round. For example `['Matthieu', 'Kasper', 'Jan', 'Riccardo']` corresponds to the tournament in the example above.
- The function should return the probability that the given player wins the entire tournament
"""

### INPUT - DO NOT TOUCH

strengths = {
        "Matthieu": 10.0,
        "Kasper": 10.0,
        "Jan": 9.0,
        "Riccardo": 6.0,
        "Tom": 5.0,
        "Hanne": 4.0,
        "Danny": 2.0,
        "Tobie": 8.0
}

parameters = eval(input())

### END INPUT

def player_wins(player, players) -> float:
    # TODO
    pass

### OUTPUT - DO NOT TOUCH
print(f"{player_wins(*parameters):.4f}")
### END OUTPUT

### EXAMPLE OUTPUT - YOU MAY UNCOMMENT THESE LINES TO CHECK YOUR CODE
### assert f"{player_wins('Matthieu', ['Matthieu']):.4f}" == '1.0000'
### assert f"{player_wins('Matthieu', ['Matthieu', 'Kasper']):.4f}" == '0.5000'
### assert f"{player_wins('Matthieu', ['Matthieu', 'Jan']):.4f}" == '0.5263'
### assert f"{player_wins('Matthieu', ['Matthieu', 'Jan', 'Kasper', 'Riccardo']):.4f}" == '0.2878'
### assert f"{player_wins('Kasper', ['Matthieu', 'Jan', 'Kasper', 'Riccardo']):.4f}" == '0.3203'
### assert f"{player_wins('Tom', ['Matthieu', 'Kasper', 'Danny', 'Riccardo', 'Tom', 'Tobie', 'Jan', 'Hanne']):.4f}" == '0.0617'
