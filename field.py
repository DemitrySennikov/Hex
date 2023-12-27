from team import Team as T
from math import sin, pi
from hex import Hex


class Field():
    def __init__(self, n, op):
        self.size = n
        self.hexes = self._init_hexes(n, op)

    def try_move(self, team, x, y):
        if self._in_bounds(x, y):
            if self.hexes[x][y].owner is None:
                self.hexes[x][y].owner = team
                return True
        return False

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
    
    def AI_solver(self):
        left_red = self._find_bound_hexes(1, 0)
        right_red = self._find_bound_hexes(1, self.size+1)
        left_blue = self._find_bound_hexes(0, 1)
        right_blue = self._find_bound_hexes(self.size+1, 1)
        min_d = 10000000
        is_attack = True
        hexes = []
        for hex_row in self.hexes:
            for hex in hex_row:
                if hex.owner is not None:
                    continue
                d_red = (self._distance_to_zone(hex, left_red, T.AI) +
                         self._distance_to_zone(hex, right_red, T.AI)-1)
                d_blue = (self._distance_to_zone(hex, left_blue, T.player) +
                          self._distance_to_zone(hex, right_blue, T.player)-1)
                if min(d_red, d_blue) < min_d:
                    hexes = [hex]
                    is_attack = (d_red <= d_blue)
                    min_d = min(d_blue, d_red)
                elif min(d_red, d_blue) == min_d:
                    if min_d == d_red:
                        if not is_attack:
                            hexes = []
                            is_attack = True
                        hexes.append(hex)
                    elif not is_attack:
                        hexes.append(hex)
        return hexes
                
    def _distance_to_zone(self, hex, zone, team):
        d = 0
        area = {(hex.x, hex.y)}
        while len(set.intersection(area, zone)) == 0:
            new_area = set.union(set(), 
                            *(self._neighboring_hexes(x, y)
                            for x, y in area))
            while len(new_area) != 0:
                x, y = new_area.pop()
                if (x, y) in area:
                    continue
                if self.hexes[x][y].owner == team:
                    new_area = set.union(new_area, 
                                         self._neighboring_hexes(x, y))
                elif self.hexes[x][y].owner is not None:
                    continue
                area.add((x, y))
            d += 1
        return d

    def _find_bound_hexes(self, x, y):
        result = set([(x, y)])
        order = set([(x, y)])
        while len(order) > 0:
            p = order.pop()
            neighboring = self._team_neighboring_hexes(p[0], p[1])
            for q in neighboring:
                if q not in result:
                    order.add(q)
                    result.add(q)
        return result
    
    def _in_bounds(self, x, y):
        return 0 < x <= self.size and 0 < y <= self.size

    def _in_bounds_global(self, x, y):
        return 0 <= x < self.size+2 and 0 <= y < self.size+2

    def _team_neighboring_hexes(self, x, y):
        result = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i+j != 0 and self._in_bounds_global(x+i, y+j):
                    if (self.hexes[x+i][y+j].owner == 
                        self.hexes[x][y].owner):
                        result.append((x+i, y+j))
        return result

    def _neutral_neighboring_hexes(self, x, y):
        result = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i+j != 0 and self._in_bounds_global(x+i, y+j):
                    if self.hexes[x+i][y+j].owner is None:
                        result.append((x+i, y+j))
        return result
    
    def _neighboring_hexes(self, x, y):
        result = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i+j != 0 and self._in_bounds_global(x+i, y+j):
                    result.append((x+i, y+j))
        return result

    def _init_hexes(self, n, op):
        hexes = []
        side = min(25, 160/n)
        Y = 320-((n+2)//2)*side*sin(pi/3)
        X = 480-((n+2)//2)*side*3/2
        for x in range(n+2):
            hexes.append([])
            for y in range(n+2):
                center_x = X + x*side*3/2
                center_y = Y + y*2*side*sin(pi/3)-x*side*sin(pi/3)
                hex = Hex(x, y, center_x, center_y, side)
                if x == 0 or x == n+1:
                    hex.assign(T.player)
                elif y == 0 or y == n+1:
                    hex.assign(op)
                hexes[x].append(hex)
        return hexes
    
    def draw(self, screen):
        for hex_row in self.hexes:
            for hex in hex_row:
                hex.draw(screen)
