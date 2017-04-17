import random

# Create template for a standard deck of cards
stdDeck = ['C-A', 'C-K', 'C-Q', 'C-J', 'C-10', 'C-9', 'C-8', 'C-7', 'C-6', 'C-5', 'C-4', 'C-3', 'C-2',
           'H-A', 'H-K', 'H-Q', 'H-J', 'H-10', 'H-9', 'H-8', 'H-7', 'H-6', 'H-5', 'H-4', 'H-3', 'H-2',
           'S-A', 'S-K', 'S-Q', 'S-J', 'S-10', 'S-9', 'S-8', 'S-7', 'S-6', 'S-5', 'S-4', 'S-3', 'S-2',
           'D-A', 'D-K', 'D-Q', 'D-J', 'D-10', 'D-9', 'D-8', 'D-7', 'D-6', 'D-5', 'D-4', 'D-3', 'D-2']

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
    stand = False
    hand = []
    score = 0
    bet = 0

    def __init__(self, name, bankroll):
        self.name = name
        self.bankroll = bankroll

    def win(self, amount):
        self.bankroll += amount

    def lose(self, amount):
        self.bankroll -= amount

    def show_bankroll(self):
        return self.bankroll

    def add_score(self, points):
        self.score += points

    def sub_score(self, points):
        self.score -= points

    def new_hand(self):
        self.score = 0
        self.hand = []
        self.bet = 0

    def get_score(self):
        return self.score


class Dealer(object):
    stand = False
    hand = []
    score = 0
    game_on = False

    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

    def draw_card(self):
        card = self.deck.pop(random.randint(0, len(self.deck) - 1))
        return card

    def deal(self):
        card1 = self.draw_card()
        card2 = self.draw_card()
        return [card1, card2]

    def add_score(self, points):
        self.score += points

    def sub_score(self, points):
        self.score -= points

    def new_hand(self):
        self.score = 0
        self.hand = []

    def get_score(self):
        return self.score


def calc_score(player_object):
    global deckVal
    player_object.score = 0
    for card in player_object.hand:
        player_object.add_score(deckVal[card])

    if has_ace(player_object) > 0 and player_object.score > 0:
        player_object.sub_score(10 * has_ace(player_object))


def print_hand(player_object):
    hand = ''
    for card in player_object.hand:
        hand = hand + card + ', '
    print player_object.name + ' hand is ' + hand + 'with a score of: ' + str(player_object.get_score())


def has_ace(player_object):
    num_aces = 0
    for card in player_object.hand:
        if card in ['C-A', 'D-A', 'S-A', 'H-A']:
            num_aces += 1
    return num_aces


def new_game(player_object, dealer_object):
    print ""
    print "==============================="
    print "Welcome to Black Jack!"
    print "==============================="
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


def reset_hand(player_object):
    player_object.stand = False
    player_object.score = 0
    player_object.hand = []
    if type(player_object) == Player:
        player_object.bet = 0


dealer = Dealer(deck=fullDeck, name="Dealer")
player = Player(bankroll=1000, name="Player")

while True:

    if not dealer.game_on:
        new = raw_input("Would you like to play a game of Black Jack? Yes or No? ").lower()
        if new == 'yes' or new == 'y':
            new_game(player, dealer)
        else:
            print "Goodbye!"
            break

    while dealer.game_on:

        while player.score <= 21:

            player_move = raw_input("Would you like to hit or stand? ").lower()
            print "Player bankroll: $" + str(player.show_bankroll())
            if player.bet == 0:
                try:
                    player_bet = int(raw_input("How much would you like to bet? "))
                except:
                    print "Sorry, please enter an numeric amount."
                    player_bet = int(raw_input("How much would you like to bet? "))
                if player_bet > player.bankroll:
                    print "Sorry, you do not have enough in your bankroll. Please enter " \
                          "an amount smaller than " + str(player.bankroll)
                    player_bet = int(raw_input("How much would you like to bet? "))
                player.bet = player_bet

            if player_move == 'hit' or player_move == 'h':
                hit_me(player, dealer)

                if player.score > 21:
                    dealer.game_on = False
                    print "Sorry, you have lost the game with a score of over 21."
                    break

            elif player_move == 'stand' or player_move == 's':
                player.stand = True
                break

        while dealer.score < 17:
            hit_me(dealer, dealer)

            if dealer.score > 21 and has_ace(dealer) == 0:
                dealer.game_on = False
                print "Sorry, you have lost the game with a score of over 21."
                break
            elif dealer.score > 21 and has_ace(dealer) > 0:
                dealer.sub_score(10 * has_ace(dealer))

        dealer.stand = True

        if player.stand and dealer.stand:
            print_hand(player)
            print_hand(dealer)
            if player.score > dealer.score:
                print "Player wins!"
                player.win(player.bet)
                print "Player bankroll: $" + str(player.show_bankroll())
            elif player.score < dealer.score:
                print "Dealer wins!"
                player.lose(player.bet)
                print "Player bankroll: $" + str(player.show_bankroll())
            else:
                print "It was a draw!"
                print "Player bankroll: $" + str(player.show_bankroll())
            reset_hand(player)
            reset_hand(dealer)
            dealer.game_on = False
