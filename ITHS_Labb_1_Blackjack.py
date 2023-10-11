# Labb 1 - Projekt 4: Blackjack

# 1) Import random module för att blanda korten
import random

# 2) Skapa variabler för att behålla info om korten
_suits = {'Clubs', 'Diamonds', 'Hearts', 'Spades'} # set
_ranks = {'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'} # set
_values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11} # dictionary


# 3) Skapa Card-class och Deck-class och funktioner som skriver ut strings under spelet genom att definerar __str__ methoder
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank+ ' of ' + self.suit

class Deck:
    def __init__(self):
        self.deck = [] # tom lista som kommer att innehålla de blandade korten under spelet
        for suit in _suits:
             for rank in _ranks:
                self.deck.append(Card(suit, rank)) # bygg upp korten-objeckterna och lägga till deck-listen

    def __str__(self):
        deck_comp = '' # tom string
        for card in self.deck:
            deck_comp += '\n ' +card.__str__()
        return 'The deck has: ' +deck_comp # iterera över sets _suit och _rank för att bygga upp info för varje kort
  
    
# 4) Skapa methoder för att blanda och deala ut korten

    def shuffle(self):
        random.shuffle(self.deck) # blanda decken innan det deala

    def deal(self):
        deal_card = self.deck.pop() # pop-funktionen ta bort korten från decken som dealas
        return deal_card
    
# 5) Skapa Hand-class som tar hänsyn till Ace's värde under spelet

class Hand:
    def __init__(self):
        self.cards = [] # tom lista
        self.value = 0 # börja från 0
        self.aces = 0 # börja från 0 - hålla koll på Aces
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += _values[card.rank] # lägga till _values to self.value variable
        if card.rank == 'Ace':
            self.aces += 11 # om card.rank är Ace, då lägga till 11 till self.aces variable

    def adjust_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10 # ta bort höger operand från vänster operand, alltså self.value - 10
            self.aces -= 1  # igen ta bort höger från vänster, alltså self.aces - 1

_deck = Deck() # lägga till Deck-klassen till variable
_deck.shuffle() # anropa shuffle-methoden
_player = Hand() # lägga till Hand-klassen till _player variable
_player.add_card(_deck.deal()) # anropa add_card-methoden och deal-methoden, append värde till _player/Hand
_player.add_card(_deck.deal()) # göra en gång till

for card in _player.cards:
    print(card)

# 6) Skapa funktioner för att ta Hits och som ber player att Hit eller Stand

    def hit(deck, hand):
        hand.add_card(deck.deal())
        hand.adjust_aces
    
    def hit_stand(deck, hand):
        global playing

        while True:
            x = input ("Please enter 'h' for Hit or 's' for Stand.")
            if x[0].lower() == 'h':
                hit(deck, hand) # om 'h' anropa hit funktionen
            
            elif x[0].lower() == 's':
                print ("Player stands. The dealer is playing.")
                playing = False # player status för player är false men dealer fortsätter

            else:
                print("Please try again.") # vid fel inmatning
                continue
            break

# 7) Skapa funktioner för att visa korten

def show_one(player, dealer):
    print("\n Dealer's Hand:")
    print(" (card is hidden)")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand=", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

# 8) Skapa funktioner som hanterar vad hander/skriver ut vid spelslut

def player_busts(player,dealer):
    print("Player busts")
def player_wins(player,dealer):
    print("Player wins")
def dealer_busts(player,dealer):
    print("Dealer busts")
def dealer_wins(player,dealer):
    print("Dealer wins")
def push(player,dealer):
    print("Dealer and Player tie - it's a push")



# 9) Spela Blackjack

playing = True # boolean för att kontrollera while loops läge

while True:

    deck = Deck()
    deck.shuffle()

    _player = Hand()
    _player.add_card(deck.deal())
    _player.add_card(deck.deal())

    _dealer = Hand()
    _dealer.add_card(deck.deal())
    _dealer.add_card(deck.deal())

    show_one(_player, _dealer)

    while playing:
        hit_stand(deck, _player)
        show_one(_player, _dealer)
    
    if _player.value > 21:
        player_busts(_player, _dealer)
        break

    if _player.value <= 21:

        while _dealer.value < 17:
            hit(deck, _dealer)

    show_all(_player, _dealer)

    if _dealer.value > 21:
        dealer_busts(_player, _dealer)

    elif _dealer.value > _player.value:
        dealer_wins(_player, _dealer)
    
    elif _dealer.value < _player.value:
        player_wins(_player, _dealer)
    
    else:
        push(_player, _dealer)