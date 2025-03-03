import random
import time
from Coder import Coder
#from Interface import Interface
#~0.?*
ships = [
    [[[0, 0]]],
    [[[0, 0]]],
    [[[0, 0]]],
    [[[0, 0]]],
    [[[0, 0], [0, 1]], [[0, 0], [1, 0]]],
    [[[0, 0], [0, 1]], [[0, 0], [1, 0]]],
    [[[0, 0], [0, 1]], [[0, 0], [1, 0]]],
    [[[0, 0], [0, 1], [0, 2]], [[0, 0], [1, 0], [2, 0]]],
    [[[0, 0], [0, 1], [0, 2]], [[0, 0], [1, 0], [2, 0]]],
    [[[0, 0], [0, 1], [0, 2], [0, 3]], [[0, 0], [1, 0], [2, 0], [3, 0]]]
]
rcross = [[-1, 0], [1, 0], [0, -1], [0, 1]]
bcross = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
aura = [
    [[[[*rcross, *bcross]], []]],
    [[[[*rcross, *bcross]], []]],
    [[[[*rcross, *bcross]], []]],
    [[[[*rcross, *bcross]], []]],
    [[[[*bcross], list(map(lambda a: [a[0], a[1] + 1], bcross))], [[0, -1], [0, 2]]], [[[*bcross], list(map(lambda a: [a[0] + 1, a[1]], bcross))], [[-1, 0], [2, 0]]]],
    [[[[*bcross], list(map(lambda a: [a[0], a[1] + 1], bcross))], [[0, -1], [0, 2]]], [[[*bcross], list(map(lambda a: [a[0] + 1, a[1]], bcross))], [[-1, 0], [2, 0]]]],
    [[[[*bcross], list(map(lambda a: [a[0], a[1] + 1], bcross))], [[0, -1], [0, 2]]], [[[*bcross], list(map(lambda a: [a[0] + 1, a[1]], bcross))], [[-1, 0], [2, 0]]]],
    [[[[*bcross], list(map(lambda a: [a[0], a[1] + 1], bcross)), list(map(lambda a: [a[0], a[1] + 2], bcross))], [[0, -1], [0, 3]]], [[[*bcross], list(map(lambda a: [a[0] + 1, a[1]], bcross)), list(map(lambda a: [a[0] + 2, a[1]], bcross))], [[-1, 0], [3, 0]]]],
    [[[[*bcross], list(map(lambda a: [a[0], a[1] + 1], bcross)), list(map(lambda a: [a[0], a[1] + 2], bcross))], [[0, -1], [0, 3]]], [[[*bcross], list(map(lambda a: [a[0] + 1, a[1]], bcross)), list(map(lambda a: [a[0] + 2, a[1]], bcross))], [[-1, 0], [3, 0]]]],
    [[[[*bcross], list(map(lambda a: [a[0], a[1] + 1], bcross)), list(map(lambda a: [a[0], a[1] + 2], bcross)), list(map(lambda a: [a[0], a[1] + 3], bcross))], [[0, -1], [0, 4]]], [[[*bcross], list(map(lambda a: [a[0] + 1, a[1]], bcross)), list(map(lambda a: [a[0] + 2, a[1]], bcross)), list(map(lambda a: [a[0] + 3, a[1]], bcross))], [[-1, 0], [4, 0]]]]
]
class Deck:
    
    deck = []
    realDeckSize = 0
    ships = []
    rotstate = []
    aura = []
    win = False
    
    def __init__(self, deckSize = 10) :
        self.win = False
        self.realDeckSize = deckSize
        self.deck = [['.' for i in range(self.realDeckSize + 5)] for t in range(self.realDeckSize + 5)]
        self.rotstate = []
        self.ships = []
        self.aura = []
        self.win = False
    
    def clear(self) :
        self.deck = [['.' for i in range(self.realDeckSize + 5)] for t in range(self.realDeckSize + 5)]
        self.ships = []
        self.rotstate = []
        self.aura = []
        self.win = False
                
    def good(self) :
        for i in self.deck :
            for t in i :
                if t == '!' :
                    return False
        return True
        #for ship in self.ships : 
        #    for shipPart in ship :
        #        if shipPart[0] < 1 or shipPart[1] < 1 or shipPart[0] > self.realDeckSize or shipPart[1] > self.realDeckSize :
        #            return False
        #for i in range(len(self.ships)) :
        #    for s1 in self.ships[i] :
        #        for t in range(i + 1, len(self.ships)) :
        #            for s2 in range(len(self.ships[t])) :
        #                if s1 == self.ships[t][s2] :
        #                    return False
        #            for t in range(i + 1, len(self.ships)) :
        #                for s2 in self.ships[t] :
        #                    if abs(s1[0] - s2[0]) <= 1 and abs(s1[1] - s2[1]) <= 1 :
        #                        return False
        #return True
    
    def nextShip(self, shipi) :
        return (shipi + 1) % len(self.ships)
    
    def inDeck(self, ship) :
        for i in ship :
            for t in i :
                if t < 1 or t > self.realDeckSize :
                    return False
        return True
    
    def moveShip(self, shipi, d) :
        ship = self.ships[shipi]
        for i in range(len(ship)) :
            ship[i] += d
        if not self.inDeck(ship) :
            return False
        for t in range(len(self.ships[shipi])) :
            self.ships[shipi][t] += d
        for t in range(len(self.aura[shipi][1])) :
            self.aura[shipi][1][t] += d
        for i in range(len(self.aura[shipi][0])) :
            for t in range(len(self.aura[shipi][0][i])) :
                self.aura[shipi][0][i][t] += d
    
    def rotateShip(self, shipi) :
        if len(ships[shipi]) == 1 :
            return False
        st = self.ships[shipi][0]
        nrot = (self.rotstate[shipi] + 1) % len(ships[shipi])
        //
        
        
    
    def rnd(self, cseed = []) :
        if cseed != [] :
            random.seed(cseed)
        while True :
            self.clear[]
            for shipSeti in range(len(ships)) :
                shipVari = random.randrange(0, len(ships[shipSeti]))
                self.rotState
                shipCoord = [random.randrange(1, self.realDeckSize + 1), random.randrange(1, self.realDeckSize + 1)]
                self.ships.append([])
                self.aura.append([[], list(map(lambda a: [a[0] + shipCoord[0], a[1] + shipCoord[1]], aura[shipSeti][shipVari][1]))])
                for shipPart in ships[shipSeti][shipVari] :
                    self.ships[len(self.ships) - 1].append([shipCoord[0] + shipPart[0], shipCoord[1] + shipPart[1]])
                    self.aura[len(self.aura) - 1][0].append(list(map(lambda a: [a[0] + shipCoord[0], a[1] + shipCoord[1]], aura[shipSeti][shipVari][0][len(self.aura[len(self.aura) - 1][0])])))
            self.render()
            if self.good() :
                return
                        
    
    def render(self, si = -1) :
        self.clear()
        for ship in self.ships :
            for shipPart in ship :
                if self.deck[shipPart[0]][shipPart[1]] == '.' :
                    self.deck[shipPart[0]][shipPart[1]] = '0'
                else :
                    self.deck[shipPart[0]][shipPart[1]] = '!'
                    
        for saura in self.aura :
            for caura in saura[0] :
                for forb in caura :
                    if self.deck[forb[0]][forb[1]] == '0' :
                        self.deck[forb[0]][forb[1]] = '!'
            for forb in saura[1] :
                if self.deck[forb[0]][forb[1]] == '0' :
                    self.deck[forb[0]][forb[1]] = '!'
        if si != -1 :
            for shipPart in ships[si] :
                self.deck[shipPart[0]][shipPart[1]] = '#'
        for i in range(len(self.deck)) :
            for t in range(len(self.deck[i])) :
                if (i < 1 or i > self.realDeckSize or t < 1 or )
                
    
    def hide(self) :
        for i in self.ships :
            for t in i :
                self.deck[t[0]][t[1]] = '?'
    
    def reveal(self) :
        for i in self.ships :
            for t in i :
                self.deck[t[0]][t[1]] = '^'

    def shoot(self, f, request, qt, qs, show, a, b) :
        while(True) :
            show(a, b)
            print(request)
            wh = f()
            if wh == 'Skip' :
                return [qt, qs]
            if wh == 'End' :
                for x in range(1, self.realDeckSize + 1) :
                    for y in range(1, self.realDeckSize + 1) :
                        if self.deck[x][y] == '.' :
                            self.deck[x][y] = '~'
                        elif self.deck[x][y] == '?' :
                            self.deck[x][y] = '*'
                self.ships = []
                self.aura = []
                self.win = True
                return [qt, qs]
            [x, y] = wh
            if self.deck[x][y] == '~' :
                qs += 1
                print('    That cell was empty anyway')
                continue
            if self.deck[x][y] == '.' :
                self.deck[x][y] = '~'
                qs += 1
                qt += 1
                print('    Miss')
                return [qt, qs]
            if self.deck[x][y] == '*' :
                qs += 1
                print('    This part has already drowned')
                continue
            self.deck[x][y] = '*'
            qs += 1
            res = 0
            for shipi in range(len(self.ships)) :
                for parti in range(len(self.ships[shipi])) :
                    if self.ships[shipi][parti] == [x, y] :
                        for also in self.aura[shipi][0][parti] : 
                            self.deck[also[0]][also[1]] = '~'
                        self.aura[shipi][0].pop(parti)
                        self.ships[shipi].pop(parti)
                        res = 1
                        if self.ships[shipi] == [] :
                            for also in self.aura[shipi][1] : 
                                self.deck[also[0]][also[1]] = '~'
                            self.aura.pop(shipi)
                            self.ships.pop(shipi)
                            print('    Drowned')
                            res = 2
                            if self.ships == [] :
                                self.win = True
                                return [qt + 1, qs]
                            break
                        print('    Shot')
                        break
                if res != 0 :
                    break    
            if res == 0 :
                return ['err', 'Error: ship not found']
    
    def rndStrat(self) :
        self.deck[0][0] = '~'
        x = 0
        y = 0
        while(self.deck[x][y] == '~' or self.deck[x][y] == '*') :
            x = random.randrange(1, self.realDeckSize + 1)
            y = random.randrange(1, self.realDeckSize + 1)
        time.sleep(1)
        print(Coder.code(x, y))
        return [x, y]
    
    def simpStrat(self) :
        toshoot = []
        for x in range(1, self.realDeckSize + 1) : 
            for y in range(1, self.realDeckSize + 1) :
                if self.deck[x][y] == '*' or self.deck[x][y] == '.' :
                    for [dx, dy] in rcross :
                        if self.deck[x + dx][y + dy] == '.' and x + dx > 0 and y + dy > 0 and x + dx <= self.realDeckSize and y + dy <= self.realDeckSize :
                            toshoot.append([x + dx, y + dy])
        if toshoot == [] :
            return self.rndStrat()
        [x, y] = random.choice(toshoot)
        print(Coder.code(x, y))
        return [x, y]
        
    
    
