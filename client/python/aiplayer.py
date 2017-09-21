from player import Player
import random
from game import Game

import copy
INF = float("inf")




def minimax(game, depth, maximizingPlayer):
    # print game
    # time.sleep(.1)

    if depth == 0 or game.ended():
        return (game.get_heriustic(), None)

    best_value, best_select = -INF if maximizingPlayer else INF, None

    childs = []
    if game.get_phase()['name'] == 'Placing pieces' or game.get_phase()['name'] == 'Flying':
        empty_positions = game.get_positions(None)
        for ep in empty_positions:
            new_child = copy.deepcopy(game)
            placing_value = 1 if new_child.can_complete_line(ep, maximizingPlayer) else 0 #TODO: -1?
            new_child.place_piece(ep, maximizingPlayer)
            childs.append( (new_child, placing_value, ('placing', ep)) )

    else:
        valid_movements = game.get_valid_movements(maximizingPlayer)
        for vm in valid_movements:
            new_child = copy.deepcopy(game)
            movement_value = 1 if new_child.can_complete_line(vm[1], maximizingPlayer) else 0 #TODO: -1?
            new_child.move_piece(vm, maximizingPlayer)
            childs.append( (new_child, movement_value, ('movement', vm)) )

    for child in childs:
        child_value = minimax(child[0], depth-1, not maximizingPlayer)[0]
        self_value = child[1]
        # print 'child_value', child_value
        # print 'self_value', self_value
        # print 'maximizingPlayer', maximizingPlayer
        v = child_value + self_value

        if maximizingPlayer and v > best_value:
            best_value, best_select = v, child
        elif not maximizingPlayer and v < best_value:
            best_value, best_select = v, child

    # print '------'
    # print best_value, best_select
    # print '------'
    return best_value, best_select

# if __name__ == '__main__':
#     g = Game()
#     g.set_changes([None for _ in xrange(24)],{'value': 0,'name':'Placing pieces'},{'ally': 9,'enemy': 9},0)
#
#     g.place_piece(2, True)
#     g.place_piece(3, True)
#     # g.place_piece(2, False)
#
#     # print g.can_complete_line(2, False)
#     print minimax(g, 2, False)

import time
class AIPlayer(Player):
    def place(self):
        game_copy = copy.deepcopy(self.game)
        print 'placing requested!'
        m = minimax(game_copy, 3, True)
        if m[1][2][0] == 'placing':
            return m[1][2][1]
        else:
            print m
            raise Exception('bad minimax!')

        # empty_positions = self.game.get_positions(None)
        # return random.choice(empty_positions)

    def move(self):
        # origin, destination = 0, 5
        # can_move = self.game.is_neighbor_position(origin, destination)
        valid_movements = self.game.get_valid_movements(True)
        return random.choice(valid_movements)

    def select_enemy_piece(self):
        # board = self.game.get_board()
        # do something whit board!
        enemy_positions = self.game.get_positions(False)
        return random.choice(enemy_positions)