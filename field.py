from team import Team as T
from math import sin, pi
from hex import Hex


class Field():
    def __init__(self, n, op, screen):
        self.size = n
        self.hexes = self._init_hexes(n, op, screen)
    

    def _in_bounds(self, x, y):
        return 0 < x <= self.size and 0 < y <= self.size


    def try_move(self, team, x, y):
        if self._in_bounds(x, y):
            if self.hexes[x][y].owner == 0:
                self.hexes[x][y].owner = team.value
                return True
        return False
    

    def _in_bounds_global(self, x, y):
        return 0 <= x < self.size+2 and 0 <= y < self.size+2


    def _team_neighboring_hexes(self, x, y):
        result = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i+j != 0 and self._in_bounds_global(x+i, y+j):
                    if self.hexes[x+i][y+j].owner == self.hexes[x][y].owner:
                        result.append((x+i, y+j))
        return result


    def is_team_win(self, team):
        if team == T.player:
            start = (0, 1)
            finish = (self.size+1, self.size)
        else:
            start = (1, 0)
            finish = (self.size, self.size+1)
        visited = [start]
        visiting = [start]
        while len(visiting) > 0:
            x, y = visiting.pop()
            neighboring = self._team_neighboring_hexes(x, y)
            for h in neighboring:
                if h not in visited:
                    visiting.append(h)
            visited += neighboring
        return finish in visited
            

    def _init_hexes(self, n, op, screen):
        hexes = []
        side = min(25, 160/n)
        Y = 320-((n+2)//2)*side*sin(pi/3)
        X = 480-((n+2)//2)*side*3/2
        for x in range(n+2):
            hexes.append([])
            for y in range(n+2):
                center_x = X + x*side*3/2
                center_y = Y + y*2*side*sin(pi/3)-x*side*sin(pi/3)
                hex = Hex(x, y, center_x, center_y, screen, side)
                if x == 0 or x == n+1:
                    hex.assign(T.player, screen)
                elif y == 0 or y == n+1:
                    hex.assign(op, screen)
                hexes[x].append(hex)
        return hexes
    

'''
a = Field(5)
for i in range(7):
    print(a._hexes[i])
print(a.is_team_win(t.Team.AI))
print(a.is_team_win(t.Team.player))
for i in range(5):
    a.try_move(t.Team.player, i+1, 1)
print(a.is_team_win(t.Team.AI))
print(a.is_team_win(t.Team.player))
for i in range(5):
    a.try_move(t.Team.AI, i+1, 1)
print(a.is_team_win(t.Team.AI))
print(a.is_team_win(t.Team.player))
'''