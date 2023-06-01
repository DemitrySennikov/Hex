from team import Team as T


class Field():
    def __init__(self, n, op):
        self.size = n
        self._hexes = [[0 for _ in range(n+2)] for _ in range(n+2)]
        for i in range(1, n+1):
            self._hexes[0][i] = T.player.value
            self._hexes[n+1][i] = T.player.value
            self._hexes[i][0] = op.value
            self._hexes[i][n+1] = op.value
    

    def _in_bounds(self, x, y):
        return 0 < x <= self.size and 0 < y <= self.size


    def try_move(self, team, x, y):
        if self._in_bounds(x, y):
            if self._hexes[x][y] == 0:
                self._hexes[x][y] = team.value
                return True
        return False
    

    def _in_bounds_global(self, x, y):
        return 0 <= x < self.size+2 and 0 <= y < self.size+2


    def _team_neighboring_hexes(self, x, y):
        result = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i+j != 0 and self._in_bounds_global(x+i, y+j):
                    if self._hexes[x+i][y+j] == self._hexes[x][y]:
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