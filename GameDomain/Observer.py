from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def updateTurn(self, allPlayer, moves):
        pass

    @abstractmethod
    def getHumanPlayerMove(self, player):
        pass