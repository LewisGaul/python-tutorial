# Aces are low for simplicity (treated as number 1).

from cards import DeckOfCards

"""
# The game can be written without a classes or even functions, as follows:
deck = DeckOfCards()
deck.shuffle()

score = 0
max_score = 0
curr_card = deck.cards[0]
print(curr_card)
for next_card in deck.cards[1:11]:
    response = input("Higher or lower? ")
    while response not in ['h', 'l', 'stop']:
        response = input("Type 'H' or 'L' for 'higher' or 'lower', or 'stop' to stop. ")
        response = response.lower() #lowercase, for comparison
    if response == 'stop':
        break
    print(next_card)
    if ((next_card.num < curr_card.num and response == 'l') or
        (next_card.num > curr_card.num and response == 'h')):
        score += 1
    max_score += 1
    curr_card = next_card

print("You scored {}/{}.".format(score, max_score))
"""    

# Here's how a similar thing can be written using a class and splitting it up
# into methods:
class Game:
    def __init__(self, players, num_of_cards=10):
        # Initialise a game (get it ready to be played).
        self.players = players
        full_deck = DeckOfCards()
        full_deck.shuffle()
        self.deck = full_deck.cards[:num_of_cards]
        self.scores = [0 for i in self.players]

    def start(self):
        curr_card = self.deck.pop()
        print(curr_card)
        i = 0
        while len(self.deck) > 0:
            player = self.players[i % len(self.players)]
            response = self.get_response(player)
            if response == 'stop':
                self.end()
                return #Stop here
            next_card = self.deck.pop()
            print(next_card)
            if ((next_card.num < curr_card.num and response == 'l') or
                (next_card.num > curr_card.num and response == 'h')):
                self.scores[i % len(self.players)] += 1
                # print(self.scores)
            curr_card = next_card
            i += 1
        self.end()

    def get_response(self, player):
        response = input("{}, higher or lower? ".format(player))
        while response not in ['h', 'l', 'stop']:
            response = input("Type 'H' or 'L' for 'higher' or 'lower', or 'stop' to stop. ")
            response = response.lower() #lowercase, for comparison
        return response

    def end(self):
        print("Final scores are")
        for i, player in enumerate(self.players):
            print("{}: {}".format(player, self.scores[i]))

            
if __name__ == '__main__':
    players = []
    user_input = input("Enter number of players or first player's name: ")
    if user_input.isdigit():
        num_players = max(1, int(user_input)) #In case 0 is entered
        players = ['Player ' + str(i+1) for i in range(num_players)]
    else:
        while user_input:
            players.append(user_input)
            user_input = input("Next player's name (press enter to start): ")
            
    g = Game(players)
    g.start()

        
