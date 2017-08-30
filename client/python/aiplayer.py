from player import Player
import random

class AIPlayer(Player):
    def place(self):
        pos = random.randint(0, 24)
        while not self.game.is_valid_position(pos, has_to_be_empty_position=True):
            pos = random.randint(0, 24)
        return pos

    def move(self):
        pos1, pos2 = random.randint(0, 24), random.randint(0, 24)
        while not self.game.is_valid_move(pos1, pos2):
            pos1, pos2 = random.randint(0, 24), random.randint(0, 24)
        return pos1, pos2