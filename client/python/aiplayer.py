from player import Player
import random

class AIPlayer(Player):
    def place(self):
        empty_positions = self.game.get_empty_positions()
        return random.choice(empty_positions)

    def move(self):
        # origin, destination = 0, 5
        # can_move = self.game.is_neighbor_position(origin, destination)
        valid_movements = self.game.get_valid_movements()
        return random.choice(valid_movements)

    def select_enemy_piece(self):
        # board = self.game.get_board()
        # do something whit board!
        enemy_positions = self.game.get_enemy_positions()
        return random.choice(enemy_positions)