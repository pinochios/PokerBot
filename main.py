
import random
from asciicards import assignArt

class player():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.stack = 0
        self.position = ""
        self.card1 = 0
        self.card2 = 0

    def print_register(self):
        print("---------------------------------------------------------------------------------------------------------------------------------")
        print("                                                           Register                                                              ")
        print("---------------------------------------------------------------------------------------------------------------------------------")
        print("poker username: ")
        self.name = input("")
        print("age: ")
        self.age = input("")


class Card(object):
    def __init__(self, value, suit):
            self.value = value
            self.suit = suit
            self.showing = True

    def __repr__(self):
            value_name = ""
            suit_name = ""
            if self.showing:
                if self.value == 0:
                    value_name = "Two"
                if self.value == 1:
                    value_name = "Three"
                if self.value == 2:
                    value_name = "Four"
                if self.value == 3:
                    value_name = "Five"
                if self.value == 4:
                    value_name = "Six"
                if self.value == 5:
                    value_name = "Seven"
                if self.value == 6:
                    value_name = "Eight"
                if self.value == 7:
                    value_name = "Nine"
                if self.value == 8:
                    value_name = "Ten"
                if self.value == 9:
                    value_name = "Jack"
                if self.value == 10:
                    value_name = "Queen"
                if self.value == 11:
                    value_name = "King"
                if self.value == 12:
                    value_name = "Ace"
                if self.suit == 0:
                    suit_name = "Clubs"
                if self.suit == 1:
                    suit_name = "Diamond"
                if self.suit == 2:
                    suit_name = "Hearts"
                if self.suit == 3:
                    suit_name = "Spades"
                return value_name + " of " + suit_name
            else:
                return "[CARD]"


class StandardDeck(list):
        def __init__(self):
            super().__init__()
            suits = list(range(4))
            values = list(range(13))
            [[self.append(Card(i, j)) for j in suits] for i in values]

        def __repr__(self):
            return f"Standard deck of cards\n{len(self)} cards remaining"

        def shuffle(self):
            random.shuffle(self)
            print("\n\n--deck shuffled--")

        def deal(self):
            deal_card = self[0]
            self.pop(0)
            return deal_card
       


class game():
        def __init__(self):
            self.buyin = 0
            self.pot = 0
            self.bigblind = 0
            self.smallblind = 0
            self.numofbot = 0

        def setup(self):

            print("---------------------------------------------------------------------------------------------------------------------------------")
            print("                                                          Game Set-Up                                                            ")
            print("---------------------------------------------------------------------------------------------------------------------------------")
            
            

            checkdigit = True

            while checkdigit:

                self.buyin = input("Enter buy-in amount: ")

                if self.buyin.isdigit():
                    self.buyin = int(self.buyin)
                    self.smallblind = input("Enter small-blind price: ")
                    
                    if self.smallblind.isdigit():
                        self.smallblind = int(self.smallblind)
                        self.bigblind = input("Enter big-blind price: ")

                        if self.bigblind.isdigit():
                            self.bigblind = int(self.bigblind)       
                            self.numofbot = input("Enter the amount of bot(max 5): ")

                            if self.numofbot.isdigit():
                                self.numofbot = int(self.numofbot)
                                if self.numofbot > 5:
                                    print("No more than 5 bot can be selected, please retry")
                                    continue
                                else:
                                    break

                            else:
                                print("Invalid amount")
                                continue

                        else:
                            print("Invalid amount")
                            continue

                    else:
                        print("Invalid amount")
                        continue

                else:
                    print("Invalid amount")
                    continue

        
print("\n\n\n\n")
print("---------------------------------------------------------------------------------------------------------------------------------")
print("\n\n\n")
print("                                         -------------------------------------------                                             ")
print("                                        |                                           |                                            ")
print("                                        |                 Poker Bot                 |                                            ")
print("                                        |                  by Kan                   |                                            ")
print("                                        |                                           |                                            ")
print("                                         -------------------------------------------                                             ")
print("\n\n\n")
print("---------------------------------------------------------------------------------------------------------------------------------")
    


player = player()
player.print_register()

game = game()
game.setup()

#print(player.name,player.age)
print(game.buyin,game.smallblind,game.bigblind)

gamecontinue = True
preflop = False
flop = False
turn = False
river = False


while gamecontinue == True:

    card = Card(0,0)
    deck = StandardDeck()
    deck.shuffle()
    preflop = True

    print("---------------------------------------------------------------------------------------------------------------------------------")
    print("                                                          Preflop                                                                ")
    print("---------------------------------------------------------------------------------------------------------------------------------")

    print(player.name + " hand: ")
    player.card1 = deck.deal()
    player.card2 = deck.deal()

    print(player.card1, " , ",player.card2)

    botplayer = [game.numofbot]

    for i in range(game.numofbot):

        card.showing = False
        print("Bot", i + 1, " hand:")
        for x in range(2):
            deal_card = deck.deal()
        
    break





        

    