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

    def is_valid_position(self, position, has_to_be_empty_position=False):
        is_bad_position = position < 0 or position > (len(self._board)-1)
        if is_bad_position:
            return False

        is_empty = self._board[position] is None
        if has_to_be_empty_position and not is_empty:
            return False

        return True

    def is_neighbor_position(self, a, b):
        for edge in self._graph:
            if edge[0] == a and edge[1] == b:
                return True
            elif edge[0] == b and edge[1] == a:
                return True
        return False

    def can_fly(self):
        return self._phase['name'] == 'Flying'

    def is_valid_move(self, origin, destination):
        is_origin_valid = self.is_valid_position(origin)
        is_destination_valid = self.is_valid_position(destination)
        if not is_origin_valid or not is_destination_valid:
            return False

        origin_is_own_piece = self._board[origin] == True
        is_destination_empty = self._board[destination] == None
        is_neighbor_position = self.is_neighbor_position(origin, destination)

        if origin_is_own_piece and is_destination_empty:
            if is_neighbor_position or self.can_fly():
                return True
        return False
