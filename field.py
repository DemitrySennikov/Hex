import enum
import hex
import team as t


class Field():
    def __init__(self, n):
        self._hexes = [[0 for _ in range(n+2)] for _ in range(n+2)]
        for i in range(1, n+1):
            self._hexes[0][i] = t.Team.player.value
            self._hexes[n+1][i] = t.Team.player.value
            self._hexes[i][0] = t.Team.AI.value
            self._hexes[i][n+1] = t.Team.AI.value
    

    def _in_bounds(self, x, y):
        return 0 < x < len(self._hexes)-1 and 0 < y < len(self._hexes)-1


    def try_move(self, team, x, y):
        if self._in_bounds(x, y):
            if self._hexes[x][y] == 0:
                self._hexes[x][y] = team.value
                return True
        return False
    

    def _in_bounds_global(self, x, y):
        return 0 <= x < len(self._hexes) and 0 <= y < len(self._hexes)


    def _team_neighboring_hexes(self, x, y):
        result = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i+j != 0 and self._in_bounds_global(x+i, y+j):
                    if self._hexes[x+i][y+j] == self._hexes[x][y]:
                        result += [hex.Hex(x+i, y+j)]
        return result


    def is_team_win(self, team):
        if team == t.Team.player:
            start = hex.Hex(0, 1)
        else:
            start = hex.Hex(1, 0)
        visited = [start]
        visiting = [start]
        while len(visiting) > 0:
            current = visiting[-1]
            del visiting[-1]
            neighboring = self._team_neighboring_hexes(current.x, current.y)
            for h in neighboring:
                if h not in visited:
                    visiting += [h]
            visited += neighboring
        if team == t.Team.player:
            finish = hex.Hex(len(self._hexes)-1, len(self._hexes)-2)
        else:
            finish = hex.Hex(len(self._hexes)-2, len(self._hexes)-1)
        return finish in visited

a = Field(5)
print(a.is_team_win(t.Team.AI))