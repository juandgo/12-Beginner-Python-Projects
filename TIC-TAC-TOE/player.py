import math 
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter
        
    # we want all players to get their next move 
    def get_move(self, game):
        pass
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        supper().__init__(self, letter)
    
    def get_move(self, game):
        # get a random valid spot for our next move
        square = random.choice(game.available_moves)
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        supper().__init__(self, letter)
        
    def get_move(self, game):
        valid_square = False
        val = None 
        while not valid_square:
            square = input(self.letter)