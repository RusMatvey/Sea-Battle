from Deck import Deck
from Coder import Coder
trans = {
    '~' : ' ', # shot cell without a ship
    '0' : '█', # not shot cell with a ship (not hidden)
    '.' : '·', # not shot cell without a ship
    '?' : '·', # not shot cell with a ship (hidden)
    '*' : 'X', # shot cell with a ship
    '^' : '░', # not shot cell with a ship (revealed)
    '!' : 'X', # cell with a ship (can't be placed due to rules)
    '#' : '░'  # cell with a ship (cofiguring ship)
}
forma = [
    [" 12345678910"],
    ["A", [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], ' '],
    ["B", [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10], ' '],
    ["C", [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10], ' '],
    ["D", [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10], ' '],
    ["E", [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10], ' '],
    ["F", [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [6, 10], ' '],
    ["G", [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9], [7, 10], ' '],
    ["H", [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9], [8, 10], ' '],
    ["I", [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9], [9, 10], ' '],
    ["J", [10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10], ' ']
]
class Interface :
    @staticmethod
    def showDeck(dck1, dck2 = -1) :
        #print(dck1)
        for i in forma :
            for t in i :
                if type(t) is not str :
                    print(trans[dck1.deck[t[0]][t[1]]], sep = '', end = '')
                else :
                    print(t, sep = '', end = '')
            if dck2 != -1 :
                print('    ', end='')
                for t in i :
                    if type(t) is not str :
                        print(trans[dck2.deck[t[0]][t[1]]], sep = '', end = '')
                    else :
                        print(t, sep = '', end = '')
            print()
        #print(forma)
    
    @staticmethod
    def askSeed() :
        print('Please enter game seed:')
        res = 0
        while res == 0 :
            try:
                res = int(input())
                break
            except ValueError :
                print('Thats not a number... Try again:')
                res = 0
        return res
    
    @staticmethod
    def askTurn() :
        print('''Now it's your turn! Choose where to shoot:''')
        res = [-100, -100]
        while(res == [-100, -100]) :
            inp = input()
            if inp == 'End Of Everything' :
                return 'End'
            if inp == 'Skip This Turn' :
                return 'Skip'
            res = Coder.decode(inp)
            if res == 'InvalidNotation' :
                print('Invalid cell notation. Try again:')
                res = [-100, -100]
        return res
    
    @staticmethod
    def confDeck(dck, seed) :
        print('For now your ships will be random')
        dck.rnd(seed)
        
