############ BOARD SCHEMA ###########
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
#####################################
import copy

class Game:
    def __init__(self):
        self._graph = [
            [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0],
            [1, 9], [3, 11], [5, 13], [7, 15],
            [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 8],
            [9, 17], [11, 19], [13, 21], [15, 23],
            [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 16]
        ]
        self._board = 24 * [None]
        self._phase = None

    def set_game(self, new_board, new_phase):
        self._board = new_board
        self._phase = new_phase

        self._empty_positions = []
        self._insider_positions = []
        self._enemy_positions = []
        self._valid_movements = []

        for index, state in enumerate(self._board):
            if state is None:
                self._empty_positions += [index]
            elif state is True:
                self._insider_positions += [index]
            elif state is False:
                self._enemy_positions += [index]
            else:
                raise Exception('bad state!')

        for origin in self._insider_positions:
            for destination in self._empty_positions:
                is_neighbor_position = self.is_neighbor_position(origin, destination)
                if is_neighbor_position or self.can_fly():
                    self._valid_movements += [(origin, destination)]

    def is_neighbor_position(self, a, b):
        for edge in self._graph:
            if edge[0] == a and edge[1] == b:
                return True
            elif edge[0] == b and edge[1] == a:
                return True
        return False

    def can_fly(self):
        return self._phase['name'] == 'Flying'

    def get_empty_positions(self):
        return copy.deepcopy(self._empty_positions)

    def get_insider_positions(self):
        return copy.deepcopy(self._insider_positions)

    def get_enemy_positions(self):
        return copy.deepcopy(self._enemy_positions)

    def get_valid_movements(self):
        return copy.deepcopy(self._valid_movements)