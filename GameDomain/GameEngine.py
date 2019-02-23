import queue
import threading

class GameEngine:

    def __init__(self, mainWindow, allPlayers):

        self.mainWindow = mainWindow
        self.allPlayers = allPlayers
        self.oneTurnThread = None
        self.fightIsFinish = False


    def applyAbility(self, ability, allPlayer):

        print("Apply ability")
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

        self.removeDeadPlayer()
        self.checkIfFinish()

        print("Finish one turn!!!!!")

        self.mainWindow.updateTurn(self.allPlayers, moves)

    def removeDeadPlayer(self):

        deadPlayer = []
        for team, players in self.allPlayers.items():

            for id, player in players.items():

                if (player.character.isDead()):
                    deadPlayer += [(team, id)]

        for team, id in deadPlayer:

            self.allPlayers[team].pop(id, None)

    def checkIfFinish(self):

        finish = False
        humanPresent = False
        for team, players in self.allPlayers.items():

            ids = list(players.keys())
            finish = finish or not ids

            if (not finish):

                for id, player in players.items():

                    humanPresent = humanPresent or player.playerType == 0


        self.fightIsFinish = finish or not humanPresent




