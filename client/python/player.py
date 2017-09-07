from abc import ABCMeta, abstractmethod

class Player:
    __metaclass__ = ABCMeta
    def __init__(self, game):
        self.game = game

    def can_i_fly(self):
        return self.game.can_fly()

    @abstractmethod
    def place(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def select_enemy_piece(self):
        pass