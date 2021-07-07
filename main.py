
import random
from asciicards import assignArt


class Player():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.stack = 0
        self.position = ""
        self.card = []

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

        def deal_fromdeck(self):
            deal_card = self[0]
            self.pop(0)
            return deal_card
            
        
       


class Game():
        def __init__(self):
            self.buyin = 0
            self.pot = 0
            self.bigblind = 0
            self.smallblind = 0
            self.numofbot = 0
            self.positionList = []
            self.tableList = []
            self.activeplayer = []
            self.handtoplay = 0
            self.handcount = 0


        def setup(self,player_name,player_age):

            checkdigit = True

            while checkdigit:

                print("---------------------------------------------------------------------------------------------------------------------------------")
                print("                                                          Game Set-Up                                                            ")
                print("---------------------------------------------------------------------------------------------------------------------------------")

                self.buyin = input("Enter buy-in amount: ")

                if self.buyin.isdigit():
                    self.buyin = int(self.buyin)
                    self.smallblind = input("Enter small-blind price: ")
                    
                    if self.smallblind.isdigit():
                        self.smallblind = int(self.smallblind)
                        self.bigblind = self.smallblind * 2

                        if self.bigblind == self.smallblind * 2:
                            self.bigblind = int(self.bigblind)       
                            self.numofbot = input("Enter the amount of bot(max 5): ")

                            if self.numofbot.isdigit():
                                self.numofbot = int(self.numofbot)
                                if self.numofbot > 5 or self.numofbot < 1:
                                    print("Invalid amount of bot, please retry")
                                    continue
                                else:
                                    self.handtoplay = input("Please enter the amount of hand to play(Minimum-10 Maximum-30): ")
                                    
                                    if self.handtoplay.isdigit():
                                        self.handtoplay = int(self.handtoplay)
                                        
                                        if self.handtoplay >= 10:

                                            if self.handtoplay > 30:
                                                print("Maximum of 30 hands, please retry")
                                            else:
                                                print("---------------------------------------------------------------------------------------------------------------------------------")
                                                print("                                                       Selected settings                                                         ")
                                                print("---------------------------------------------------------------------------------------------------------------------------------")
                                                print("--Player Profile--")
                                                print("Name:",player_name)
                                                print("Age:",player_age)
                                                print("\n")
                                                print("--Game settings--")
                                                print("Buy-in:",self.buyin)
                                                print("Small-blind:",self.smallblind)
                                                print("Big-blind:",self.bigblind)
                                                print("Number of bot:",self.numofbot)
                                                print("Playing hand:",self.handtoplay)
                                                print("\n")


                                                setup_complete = input("Press 'y' to confirm, 'n' to reset...")
                                                
                                                if setup_complete == "y":
                                                    print("--Setup completed--")
                                                    break
                                                elif setup_complete == "n":
                                                    continue
                                                else:
                                                    print("Invalid decision, game reset")
                                                    continue

                                            
                                            
                                        else:
                                            print("Minimum of 10 hands, please retry")
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

                else:
                    print("Invalid amount")
                    continue

        def setup_position(self,player,numofbot,handcount):

            if handcount == 0:

                if numofbot > 0:
                    self.positionList.append("Dealer")
                    self.positionList.append("Smallblind")
                    
                    if numofbot > 1:
                        self.positionList.append("Bigblind")

                        if numofbot > 2:
                            self.positionList.append("UTG")

                            if numofbot > 3:
                                self.positionList.append("Middle Postion")

                                if numofbot > 4:
                                    self.positionList.append("Late Postion")


            
            #--------player--------
            self.tableList.append(player)
            #set starting stack equals table buy-in
            if handcount == 0:
                player.stack = game.buyin
            
            #-------init bot-------
            for i in range(numofbot):
                bot = Player()
                bot.name = "Bot " + str(i+1)
                self.tableList.append(bot)
                #set starting stack equals table buy-in
                if handcount == 0:
                    bot.stack = game.buyin

            #shuffle seating
            random.shuffle(self.tableList)

            #asssign position
            for i, ply in enumerate(self.tableList):
                ply.position = self.positionList[i]

        

       


        
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
    


player = Player()
player.print_register()
game = Game()
game.setup(player.name,player.age)
bot = Player()

#print(player.name,player.age)

gamecontinue = True
preflop = False
flop = False
turn = False
river = False


while gamecontinue == True and game.handcount <= game.handtoplay:

    game.pot = 0

    card = Card(0,0)
    deck = StandardDeck()
    deck.shuffle()
    preflop = True

    print("---------------------------------------------------------------------------------------------------------------------------------")
    print("                                                          Preflop                                                                ")
    print("---------------------------------------------------------------------------------------------------------------------------------")

    #____________________init bot__________________________
    """
    botList = []

    for i in range(game.numofbot):
        bot = Player()
        botList.append(bot)
        
    """

    #_______________init table position________________

    game.setup_position(player,game.numofbot,game.handcount)



    # _____________Deal all player & bot 2 cards____________________
    """
    print(player.name + " hand: ")

    #deal 2 cards and store in list for player
    player.card.append(deck.deal())
    player.card.append(deck.deal()) 

    print(player.card[0], ",",player.card[1])
    """
    
    #deal 2 cards for each bot
    for i, bot in enumerate(game.tableList):
        print(bot.name , "hand:",)
        bot.card.append(deck.deal_fromdeck())
        bot.card.append(deck.deal_fromdeck())
        print(bot.card[0],",",bot.card[1])
        print("Position:", bot.position)
        print("Stack:", bot.stack)

    #reset all player to active
    game.activeplayer = game.tableList

    #_______________________Bet Preflop____________________________

    x = Player()
    bet_amount = game.bigblind
    game.pot += (game.smallblind + game.bigblind)
    preflop = True

    while preflop == True:

        actionlist = []
        

        for x in game.tableList:

            valid_bet = False

            print("----------------",x.name, "'s turn ----------------")


            print("'c' - call | 'f' - fold | 'r' - raise | 'a' - allin")

            decision = input("Decision: ")
            
            if decision == 'c':

                x.stack -= bet_amount
                game.pot += bet_amount
                actionlist.append(False)

            if decision == 'f':
                
                if x.position == 'Smallblind':
                    x.stack -= game.smallblind
                    
                if x.position == 'Bigblind':
                    x.stack -= game.bigblind

                actionlist.append(False)

                #game.activeplayer.remove(x)


            if decision == 'r':

                while valid_bet == False:

                    input_amount = input("Please enter the amount of raise: ")
                    
                    if input_amount.isdigit():
                        input_amount = int(input_amount)
                        
                        if input_amount >= bet_amount * 2:
                            bet_amount = input_amount
                            game.pot += bet_amount
                            x.stack -= bet_amount
                            actionlist.append(True)
                            valid_bet = True
                        else:
                            print("Raise need to be at least 2 times of the last bet")
                            continue
                    
                    else:
                        print("Invalid amount")
                        continue

            if decision == 'a':
                
                bet_amount += x.stack
                x.stack = 0

        for i, bot in enumerate(game.tableList):
            print(bot.name)
            print("Stack:", bot.stack)

        if True in actionlist:
            continue
        else:
            preflop = False


    print("End Preflop")
        






    break

