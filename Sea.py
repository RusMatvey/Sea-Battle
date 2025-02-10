import Deck
from Interface import Interface
from Coder import Coder
class Sea :
    def __init__(self) :
        print('Made sea')
    def main(self) :
        [compDeck, userDeck] = [Deck.Deck(), Deck.Deck()]
        seed = Interface.askSeed()
        compDeck.hide()
        print('For now your ships will be random as well')
        userDeck.rnd(seed + 1)
        qt = 0
        qs = 0
        qtc = 0
        qsc = 0
        while(not compDeck.win and not userDeck.win) :
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
            if compDeck.win :
            print('It took you', qt, 'turns and', qs, 'shots to win')
        else :
            compDeck.reveal()
            print('Unfortunately, you lose\nIt took computer', qtc, 'turns and', qsc, 'shots to win')
        Interface.showDeck(compDeck, userDeck)
