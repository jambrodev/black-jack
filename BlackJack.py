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
    stand = False

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

    def sub_score(self, points):
        Player.score -= points

    def new_hand(self):
        Player.score = 0
        Player.hand = []


class Dealer(object):

    # Set the starting score
    game_on = False
    score = 0
    hand = []
    stand = False

    def __init__(self, deck, name):
        self.deck = deck
        self.name = name

    def draw_card(self):
        card = self.deck.pop(random.randint(0, len(self.deck)-1))
        return card

    def add_score(self, points):
        Dealer.score += points

    def sub_score(self, points):
        Dealer.score -= points

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
        hand = hand + card + ', '
    print player_object.name + ' hand is ' + hand + 'with a score of: ' + str(player_object.score)


def has_ace(player_object):
    num_aces = 0
    for card in player_object.hand:
        if card in ['C-A', 'D-A', 'S-A', 'H-A']:
            num_aces += 1
    return num_aces


def new_game(player_object, dealer_object):
    print "Welcome to Black Jack!"
    print ""
    player_object.hand = dealer_object.deal()
    calc_score(player_object)
    print_hand(player_object)
    dealer_object.hand = dealer_object.deal()
    calc_score(dealer_object)
    print_hand(dealer_object)
    dealer_object.game_on = True


def hit_me(player_object, dealer_object):
    player_object.hand.append(dealer_object.draw_card())
    calc_score(player_object)
    print_hand(player_object)

dealer = Dealer(deck=fullDeck, name="Dealer")
player = Player(bankroll=1000, name="Player")


while True:

    if not dealer.game_on:
        new_game(player, dealer)

    while dealer.game_on:

        if player.score <= 21:
            player_move = raw_input("Would you like to hit or stand? ").lower()

            if player_move == 'hit' or player_move == 'h':
                hit_me(player, dealer)

                print_hand(player)

                if player.score > 21 and has_ace(player) == 0:
                    dealer.game_on = False
                    print "Sorry, you have lost the game with a score of over 21."
                    break
                elif player.score > 21 and has_ace(player) > 0:
                    player.sub_score(10 * has_ace(player))

            else:
                pass

        if dealer.score < 17:
            hit_me(dealer, dealer)

            print_hand(dealer)

            if dealer.score > 21 and has_ace(dealer) == 0:
                dealer.game_on = False
                print "Sorry, you have lost the game with a score of over 21."
                break
            elif dealer.score > 21 and has_ace(dealer) > 0:
                dealer.sub_score(10 * has_ace(dealer))
