import Deck
from Interface import Interface
from Coder import Coder
class Sea :
    def __init__(self) :
        print('Made sea')
    def main(self) :
        #userDeck = Deck()
        #gameSeed = Interface.askSeed()
        [compDeck, userDeck] = [Deck.Deck(), Deck.Deck()]
        #print(compDeck.win)
        #print(userDeck.win)
        #compDeck.win = True
        #print(compDeck.win)
        #print(userDeck.win)
        #userDeck = Deck.Deck()
        seed = Interface.askSeed()
        
        #Interface.showDeck(userDeck)
        
        #print(userDeck.deck)
        compDeck.rnd(seed)
        #compDeck.bomba()
        userDeck.clear()
        #print(userDeck.deck)
        #print([1, 1] + [2, 2])
        
        #userDeck = Deck()
        
        #Interface.showDeck(compDeck)
        #print(Deck())
        #print(compDeck)
        #print(userDeck)
        #print(Deck())
        #print(Deck())
        #print(userDeck.deck)
        #Interface.showDeck(Deck.Deck(35))
        
        compDeck.hide()
        
        #Interface.showDeck(compDeck)
        
        #Interface.
        print('For now your ships will be random as well')
        #Interface.showDeck(userDeck)
        userDeck.rnd(seed + 1)
        #print('\n\n\n')
        #for i in range(100) :
        #    compDeck.rnd(i)
        #    Interface.showDeck(compDeck)
        #return
        #print('\n\n\n')
        #compDeck.hide()
        #print('\n\n\n')
        qt = 0
        qs = 0
        qtc = 0
        qsc = 0
        #Interface.showDeck(compDeck)
        while(not compDeck.win and not userDeck.win) :
            #Interface.showDeck(compDeck, userDeck)
            #Interface.showDeck(userDeck)
            [qt, qs] = compDeck.shoot(Interface.askTurn, "", qt, qs, Interface.showDeck, compDeck, userDeck)
            if qt == 'err' :
                print('Error with shooting', qs)
                break
            if compDeck.win :
                print("You win!")
                break
            [qtc, qsc] = userDeck.shoot(userDeck.simpStrat, "Computer's turn:", qtc, qsc, Interface.showDeck, compDeck, userDeck)
            if qtc == 'err' :
                print('Error whith shooting', qs)
                break
            #print('\n\n\n')
            #if ph == 'err' :
            #        print('''Error: ship not found. Enter "quit" if you want to quit:''')
            #        ext = input()
            #        if ext == 'quit' :
            #            return
            #elif ph == 'blank' :
            #        print('That cell was empty anyway')
            #        qt += 1
            #        qs += 1
            #        qtc += 1
            #        qsc += userDeck.selfShoot()
            #elif ph == 'miss' :
            #        print('You missed')
            #        qt += 1
            #        qs += 1
            #        qtc += 1
            #        qsc += userDeck.selfShoot()
            #elif ph == 'alr' :
            #        print('You have already shot this cell')
            #        qt += 1
            #        qs += 1
            #        qtc += 1
            #        qsc += userDeck.selfShoot()
            #elif ph == 'hit' :
            #        print('You shot a ship!')
            #        qs += 1
            #elif ph == 'kill' :
            #        print('You drowned a ship')
            #        qs += 1
            #elif ph == 'win' :
            #        Interface.showDeck(compDeck)
            #        print('You won! Congratulations')
            #        qs += 1
            #        break
            #else :
            #        print('''Error: unexpected case. Enter "quit" if you want to quit:''')
            #        ext = input()
            #        if ext == 'quit' :
            #            return
        if compDeck.win :
            print('It took you', qt, 'turns and', qs, 'shots to win')
        else :
            compDeck.reveal()
            print('Unfortunately, you lose\nIt took computer', qtc, 'turns and', qsc, 'shots to win')
        Interface.showDeck(compDeck, userDeck)