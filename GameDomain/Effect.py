from abc import ABC, abstractmethod

class Effect(ABC):

    @abstractmethod
    def apply(self, character):
        pass


    @abstractmethod
    def isFinnish(self):
        pass


class Attack(Effect):

    def __init__(self):

        self.dmg = 10
        self.time = 1


    def apply(self, character):

        character.baseStats.life -= self.dmg


    def isFinnish(self):

        self.time -= 1

        return self.time <= 0