from abc import ABC, abstractmethod

class Player(ABC):

    @abstractmethod
    def getMove(self, players, queue):
        pass

    @abstractmethod
    def getImage(self):
        pass

