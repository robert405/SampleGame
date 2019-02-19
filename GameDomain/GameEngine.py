import queue
import threading

class GameEngine:

    def __init__(self, mainWindow, allPlayers):

        self.mainWindow = mainWindow
        self.allPlayers = allPlayers
        self.oneTurnThread = None


    def applyAbility(self, ability, allPlayer):

        ability.apply(allPlayer[ability.teamTarget][ability.idTarget].character)


    def oneTurn(self):

        moves = queue.Queue()
        threadPool = []

        for team, players in self.allPlayers.items():

            for pos, p in players.items():

                thread = threading.Thread(target=p.getMove, args=(self.allPlayers, moves))
                thread.start()
                threadPool += [thread]

        for thread in threadPool:
            thread.join()

        while (not moves.empty()):

            move = moves.get()
            self.applyAbility(move, self.allPlayers)

        self.mainWindow.updateTurn(self.allPlayers, moves)



