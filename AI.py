import team as t
import random


def AI_move(team, hexes):
    if team.value == t.Team.AI.value:
        return _AI_random_move(hexes)
    else:
        return _AI_random_move(hexes)
        

def _AI_random_move(hexes):
    free_hexes = []
    for hex in hexes:
        if hex.owner == 0:
            free_hexes.append(hex)
    return random.choice(free_hexes)

'''
a = field.Field(5)
for _ in range(5):
    x, y = _AI_random_move(a)
    print(x, y)
'''