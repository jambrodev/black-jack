import random

# Create template for a standard deck of cards
stdDeck = ['C-A', 'C-K', 'C-Q', 'C-J', 'C-10', 'C-9', 'C-8', 'C-7', 'C-6', 'C-5', 'C-4', 'C-3', 'C-2',
           'H-A', 'H-K', 'H-Q', 'H-J', 'H-10', 'H-9', 'H-8', 'H-7', 'H-6', 'H-5', 'H-4', 'H-3', 'H-2',
           'S-A', 'S-K', 'S-Q', 'S-J', 'S-10', 'S-9', 'S-8', 'S-7', 'S-6', 'S-5', 'S-4', 'S-3', 'S-2',
           'D-A', 'D-K', 'D-Q', 'D-J', 'D-10', 'D-9', 'D-8', 'D-7', 'D-6', 'D-5', 'D-4', 'D-3', 'D-2']
#stdDeck.remove('C-A')

# Create dictionary that correlates cards to their values
deckVal = {'C-A': 11, 'C-K': 10, 'C-Q': 10, 'C-J': 10, 'C-10': 10, 'C-9': 9, 'C-8': 8, 'C-7': 7, 'C-6': 6, 'C-5': 5,
           'C-4': 4, 'C-3': 3, 'C-2': 2, 'H-A': 11, 'H-K': 10, 'H-Q': 10, 'H-J': 10, 'H-10': 10, 'H-9': 9, 'H-8': 8,
           'H-7': 7, 'H-6': 6, 'H-5': 5, 'H-4': 4, 'H-3': 3, 'H-2': 2, 'S-A': 11, 'S-K': 10, 'S-Q': 10, 'S-J': 10,
           'S-10': 10, 'S-9': 9, 'S-8': 8, 'S-7': 7, 'S-6': 6, 'S-5': 5, 'S-4': 4, 'S-3': 3, 'S-2': 2, 'D-A': 11,
           'D-K': 10, 'D-Q': 10, 'D-J': 10, 'D-10': 10, 'D-9': 9, 'D-8': 8, 'D-7': 7, 'D-6': 6, 'D-5': 5, 'D-4': 4,
           'D-3': 3, 'D-2': 2}

# Create the full deck of cards
fullDeck = stdDeck * 2


class Player(object):

    # Set the starting score
    score = 0
    hand = []

    def __init__(self, bankroll, name):
        self.bankroll = bankroll
        self.name = name

    def win(self, amount):
        self.bankroll += amount

    def lose(self, amount):
        self.bankroll -= amount

    def show_bankroll(self):
        return self.bankroll

    def add_score(self, points):
        Player.score += points

    def new_hand(self):
        Player.score = 0
        Player.hand = []


class Dealer(object):

    # Set the starting score
    score = 0
    hand = []

    def __init__(self, deck, name):
        self.deck = deck
        self.name = name

    def draw_card(self):
        card = self.deck.pop(random.randint(0, len(self.deck)-1))
        return card

    def add_score(self, points):
        Dealer.score += points

    def new_hand(self):
        Dealer.score = 0
        Dealer.hand = []

    def deal(self):
        card1 = self.draw_card()
        card2 = self.draw_card()
        return [card1, card2]


def calc_score(player_object):
    global deckVal
    for card in player_object.hand:
        player_object.add_score(deckVal[card])


def print_hand(player_object):
    hand = ''
    for card in player_object.hand:
        hand = hand + ', ' + card
    print player_object.name + ' hand is ' + hand + ' with a score of: ' + str(player_object.score)

dealer = Dealer(deck=fullDeck, name="Dealer")
player = Player(bankroll=1000, name="Player")

print "Welcome to Black Jack!"
print ""
player.hand = dealer.deal()
calc_score(player)
print_hand(player)

dealer.hand = dealer.deal()
calc_score(dealer)
print_hand(dealer)

while True:


    while player.score <= 21:
        player_move = raw_input("Would you like to hit or stand? ")

        if player_move.lower() == 'hit':
            player.hand.append(dealer.draw_card())
            calc_score(player)
            print_hand(player)
        elif player_move.lower() == 'stand':
            pass
        else:
            player_move = raw_input("Sorry, would you like to hit or stand? ")


    break