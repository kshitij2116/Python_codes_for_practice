suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
import random
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        #print(f"{self.rank} of {self.suit}")
        return self.rank + ' of ' + self.suit
    def return_rank(self):
        return self.rank
    def return_suit(self):
        return self.suit
class Deck:
    def __init__(self):
        self.cards_dealt = 0
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
        self.deck_shuffle()
    def deck_shuffle(self):
        random.shuffle(self.deck)
    def __str__(self):
        current_deck = ''
        for card in self.deck:
            current_deck += '\n' + card.__str__()#str(print(card))
        return current_deck
    def deal(self):
        dealing_card = self.deck[self.cards_dealt]
        self.deck.pop(self.cards_dealt)
        self.cards_dealt +=1
        return dealing_card
class Hand:
    def __init__(self,money):
        self.money = money
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
        self.value_of_first_ace = values['Ace']
    def add_money(self):
        self.money *=2
    def remove_money(self):
        self.money =0
    def add_card(self,card):
        self.cards.append(card)
        if (card.return_rank() =='Ace'):
            if self.aces==0:
                self.value += values[card.return_rank()] 
            else :
                self.value += 1
            self.aces +=1                                             
        else : 
            self.value += values[card.return_rank()] 
        self.adjust_for_ace()
    def adjust_for_ace(self):
        if self.aces == 0:
            pass
        else :
            if self.value <=21:
                pass
            else :
                if self.value_of_first_ace == values['Ace']:
                    self.value =self.value-values['Ace']+1
                    self.value_of_first_ace = 1
                else :
                    pass
    def __str__(self):  #TAKE CARE THAT THIS PRINTS ALL THE CARDS.WE WANT TO PRINT ONLY 1 CARD OF THE DEALER
        current_hand = ''
        for card in self.cards:
            current_hand += '\n' + card.__str__() #str(print(card))
        return current_hand
    def return_value(self):
        return self.value       
    def print_only_one_card(self):
        print(self.cards[0])
def check_for_bust(hand):
    if hand.return_value() > 21:
        hand.remove_money()
        return True
    else :
        return False
def check_for_perfect_score(hand):
    if hand.return_value() == 21:
        return True
    else :
        return False    
def check_who_wins(hand1,hand2):
    if hand1.return_value()>=hand2.return_value():#CHECK FOR EQUAL SCORE NEEDS TO BE WORKED UPON
        return hand1
    else :
        return hand2
def play_of_hand(deck,hand):  
    current_card = deck.deal()
    print("New card from deck is : ")
    print(current_card)
    hand.add_card(current_card)
    print("The current hand looks like : \n")
    print(hand)
    print(f"The total value of this hand is : {hand.return_value()}")
    return hand
def main():
    deck = Deck()
    money_input = input("Enter the money you want to bet :  ")
    player = Hand(money_input)
    computer = Hand(0)
    next_move = 'h'
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    computer.add_card(deck.deal())
    computer.add_card(deck.deal())
    print("Hand of the player is : ")
    print(player)
    print("Value of player : ")
    print(player.return_value())
    if check_for_perfect_score(player) : 
        print("You have reached a perfect score. BLACK JACK! ")
        player.add_money()
        return True
    if check_for_bust(player) :
        print("Busted! You lose! ")
        return True
    print("First card of dealer's hand is : ")
    computer.print_only_one_card()
    print("Game begins now. Turn of player")
    next_move = input("Do you want to h/s : ")
    while next_move == 'h':
        player = play_of_hand(deck,player)
        if check_for_perfect_score(player) : 
            print("You have reached a perfect score. BLACK JACK! ")
            player.add_money()
            return True
        if check_for_bust(player) :
            print("Busted!! You lose! ")
            return True
        next_move = input("What do you want to do next h/s :")
    print("Now the dealer will make his move. His hand looks like :  ")
    print(computer)
    if check_for_perfect_score(computer) : 
        print("Dealer has reached a perfect score. BLACK JACK! ")
        computer.add_money()
        return True
    while computer.return_value() <=16 :
        play_of_hand(deck, computer)
        if check_for_bust(computer):
            print("The dealer has busted!! You win!! ")
            player.add_money()
            return True
    winner_hand = check_who_wins(player, computer)
    if player == winner_hand:
        print("You Win!! ")
        player.add_money()
    else :
        print("The dealer wins!! ")
        player.remove_money()
    return True
 
if __name__ == '__main__':
	main()