############ BOARD SCHEMA ###########
#                                   #
#     0------------1------------2   #
#     |            |            |   #
#     |   8--------9------10    |   #
#     |   |        |       |    |   #
#     |   |   16--17--18   |    |   #
#     |   |   |        |   |    |   #
#     7---15--23      19--11----3   #
#     |   |   |        |   |    |   #
#     |   |   22--21--20   |    |   #
#     |   |        |       |    |   #
#     |   14------13------12    |   #
#     |            |            |   #
#     6------------5------------4   #
#                                   #
#####################################
import copy
BOARD_SIZE = 24
# PLACING: {value: 0, name:'Placing pieces'},
# MOVING:  {value: 1, name:'Moving pieces'},
# FLYING:  {value: 2, name:'Flying'}

class Game:
    def __init__(self):
        self.__graph = [
            [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0],
            [1, 9], [3, 11], [5, 13], [7, 15],
            [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 8],
            [9, 17], [11, 19], [13, 21], [15, 23],
            [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 16]
        ]

        self.__lines = [[0, 1, 2], [2, 3, 4], [4, 5, 6], [0, 7, 6],
                      [8, 9, 10], [10, 11, 12], [12, 13, 14], [14, 15, 8],
                      [16, 17, 18], [18, 19, 20], [20, 21, 22], [22, 23, 16],
                      [1, 9, 17], [3, 11, 19], [5, 13, 21], [7, 15, 23]]

        self.__board = [None for _ in xrange(BOARD_SIZE)]
        self.__round_number = 0
        self.__turn = None
        self.__phase = None
        self.__stocks = {
            'ally': 9,
            'enemy': 9
        }

    def set_game(self, new_board, new_phase):
        self.__board = new_board
        self.__phase = new_phase

        self.__empty_positions = []
        self.__insider_positions = []
        self.__enemy_positions = []
        self.__valid_movements = []

        for index, state in enumerate(self.__board):
            if state is None:
                self.__empty_positions += [index]
            elif state is True:
                self.__insider_positions += [index]
            elif state is False:
                self.__enemy_positions += [index]
            else:
                raise Exception('bad state!')

        for origin in self.__insider_positions:
            for destination in self.__empty_positions:
                is_neighbor_position = self.is_neighbor_position(origin, destination)
                if is_neighbor_position or self.can_fly():
                    self.__valid_movements += [(origin, destination)]

    def change_turn(self):
        self.__turn = False if self.__turn == True else True
        self.__round_number += 1

    def update_phase(self):
        if self.__phase['name'] == 'Placing pieces':
            has_no_piece_in_stock = None
            if self.__turn == True:
                has_no_piece_in_stock = self.__stocks['ally'] <= 0
            else:
                has_no_piece_in_stock = self.__stocks['enemy'] <= 0

            if has_no_piece_in_stock:
                self.__phase = {'value': 1, 'name':'Moving pieces'}
        else:
            has_less_than_three_pieces = len(get_positions(self.__turn)) < 3
            if has_less_than_three_pieces:
                self.__phase = {'value': 2, 'name':'Flying'}

    def set_changes(self, new_board, new_phase, stocks, new_round_number):
        #TODO: check bad changes!
        self.__board = new_board
        self.__phase = new_phase
        self.__stocks = stocks
        self.__round_number = new_round_number

    def place_piece(self, position, piece):
        #TODO: check bad PLACING
        if piece == True:
            self.__stocks['ally'] -= 1
        else:
            self.__stocks['enemy'] -= 1
        self.__board[position] = piece
        self.update_phase()
        self.change_turn()

    def move_piece(self, origin, destination):
        #TODO: check bad MOVING
        self.__board[destination], self.__board[origin] = self.__board[origin], self.__board[destination]
        self.update_phase()
        self.change_turn()

    def remove_piece(self, position):
        #TODO: check bad REMOVING
        self.__board[position] = None

    def is_neighbor_position(self, a, b):
        for edge in self.__graph:
            if edge[0] == a and edge[1] == b:
                return True
            elif edge[0] == b and edge[1] == a:
                return True
        return False

    def get_positions(self, state):
        return [index for index, cell in enumerate(self.__board) if cell == state]

    def get_valid_movements(self, is_ally=True):
        valid_origins = self.get_positions(is_ally)
        valid_destination = self.get_positions(None)

        valid_movements = []
        for origin in valid_origins:
            for destination in valid_destination:
                is_neighbor = self.is_neighbor_position(origin, destination)
                if is_neighbor or self.can_fly():
                    valid_movements += [(origin, destination)]
        return valid_movements

    def get_board(self):
        return copy.deepcopy(self.__board)

    def get_phase(self):
        return copy.deepcopy(self.__phase)

    def can_fly(self):
        return self.__phase['name'] == 'Flying'

    def ended(self):
        #TODO: kamel avaz beshe in ghesmaat!
        return True if (len(self.get_positions(None)) == 0) else False

    def can_complete_line(self, position, piece):
        if self.__board[position] == None:
            contained_lines = [line for line in self.__lines if position in line]
            for line in contained_lines:
                three_piece_complete = sum([1 for p in line if self.__board[p] == piece]) == 2
                if three_piece_complete:
                    return True
        return False

    def get_heriustic(self):
        return 0

    def __str__(self):
        board = []
        for cell in self.__board:
            if cell is None:
                board += [' ']
            elif cell is True:
                board += ['X']
            else:
                board += ['O']

        return "############ BOARD SCHEMA ###########\n\
#                                   #\n\
#     %s----------%s----------%s       #\n\
#     |          |          |       #\n\
#     |   %s------%s------%s   |       #\n\
#     |   |      |      |   |       #\n\
#     |   |   %s--%s--%s   |   |       #\n\
#     |   |   |     |   |   |       #\n\
#     %s---%s---%s     %s---%s---%s       #\n\
#     |   |   |     |   |   |       #\n\
#     |   |   %s--%s--%s   |   |       #\n\
#     |   |      |      |   |       #\n\
#     |   %s------%s------%s   |       #\n\
#     |          |          |       #\n\
#     %s----------%s----------%s       #\n\
#                                   #\n\
#####################################" % (board[0], board[1], board[2], board[8], board[9], board[10], board[16], board[17], board[18], board[7], board[15], board[23], board[19], board[11], board[3], board[22], board[21], board[20], board[14], board[13], board[12], board[6], board[5], board[4])

import time

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
