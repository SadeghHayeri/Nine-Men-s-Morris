from abc import ABCMeta, abstractmethod

class Player:
    __metaclass__ = ABCMeta
    def __init__(self, game):
        self.game = game

    def can_i_fly(self):
        return self.game.can_fly()

    @abstractmethod
    def place(self):
        return 0

    @abstractmethod
    def move(self):
        return 0, 1