"github.com/lewisgaul/python-tutorial"
# WEEK 5 CHALLENGE - classes

# Work out how the code below works (use print statements or display variables
# in the shell), add in some comments and make some improvements by using better
# variable names and clearer code where you can.

# When you understand the code below, make a card game in a separate file. You
# should include:
# - an import from this file;
# - a 'Game' class (not really necessary, but good practice);
# - a while loop which runs until someone wins;
# - the 'input' function to get what a player wants to do.
# Remember to separate code into functions or the Game class where suitable.
# Recommended card games to try and make (first is easier):
# - Higher or lower (player guesses whether the next card will be higher or
#   lower than the last, should end up with a score for the number correct);
# - Blackjack (a.k.a. 21/pontoon, see wikipedia for rules).


import random as rnd


class Card:
    def __init__(self, num, suit):
        self.num = num
        self.suit = suit

    def __str__(self):
        # Define what happens when you print a card.
        if self.num == 1:
            num_str = 'A'
        elif self.num <= 10:
            num_str = str(self.num)
        elif self.num == 11:
            num_str = 'J'
        elif self.num == 12:
            num_str = 'Q'
        elif self.num == 13:
            num_str = 'K'
        return num_str + self.suit

    def __repr__(self):
        # Define what happens when you display a card (e.g. in a list).
        return self.__str__() #Return the same as the __str__ method


class DeckOfCards:
    def __init__(self):
        self.cards = []
        for s in ['c', 'd', 'h', 's']:
            for i in range(13):
                self.cards.append(Card(i+1, s))

    def __repr__(self):
        return self.cards.__str__()

    def shuffle(self):
        # Use the random module to shuffle the list.
        rnd.shuffle(self.cards)


#print(Card(11, 'd')) #Uses the __str__ method
deck = DeckOfCards()
#print(deck) #Uses the __str__ method
#print(type(deck.cards[0])) #What do you think this will print?



