from tkinter import *
from functools import partial
from PIL import ImageTk, Image
import threading
from GameDomain.HumanPlayer import HumanPlayer
from GameDomain.Ai import Ai
from GameDomain.Observer import Observer
from GameDomain.GameEngine import GameEngine

class MainWindow(Observer):

    def __init__(self):

        self.root = Tk()
        self.root.geometry('1000x800')

        self.topFrame = Frame(self.root)
        self.topFrame.pack(side=TOP)

        self.bottomFrame = Frame(self.root)
        self.bottomFrame.pack(side=BOTTOM)

        self.leftFrame = Frame(self.root)
        self.leftFrame.pack(side=LEFT)

        self.rightFrame = Frame(self.root)
        self.rightFrame.pack(side=RIGHT)

        self.labelMsg = StringVar()
        self.labelMsg.set("Allo!!!!!!!!!!")
        self.one = Label(self.topFrame, textvariable=self.labelMsg)
        self.one.pack()

        self.emptyImg = ImageTk.PhotoImage(Image.open("./Ressource/Empty.jpg"))

        self.currentPlayer = None
        self.ability = None
        self.gameEngine = None

        self.launchFightButton = Button(self.topFrame, text="Lauch fight!", command=self.launchFight, height=5, width=10)
        self.launchFightButton.pack()

        self.moveChosenButton = None


    def chooseTarget(self, team, id):

        print("team-" + str(team) + "_id-" + str(id))
        if (self.ability is not None):
            self.ability.set(team, id)

    def startTurn(self):

        self.fightThread = threading.Thread(target=self.gameEngine.oneTurn, args=())
        self.fightThread.start()

    def launchFight(self):

        players = {}
        players[0] = {0: Ai(0), 3: HumanPlayer(self, 0)}
        players[1] = {2: Ai(1), 5: Ai(1)}

        self.gameEngine = GameEngine(self, players)

        self.loadTeamButton(players)
        self.startTurn()


    def loadTeamButton(self, players):

        buttonWith = 100
        buttonHeight = 100

        self.leftButtons = []
        team1 = players[0]

        for i in range(6):

            if (i in team1):
                button = Button(self.leftFrame, image=team1[i].getImage(), command=partial(self.chooseTarget, 1, i), height=buttonHeight, width=buttonWith)
            else:
                button = Button(self.leftFrame, image=self.emptyImg, command=partial(self.chooseTarget, 1, i), height=buttonHeight, width=buttonWith)

            button.grid(row=int(i/2), column=i%2)

            self.leftButtons += [button]

        self.rightButtons = []
        team2 = players[1]

        for i in range(6):

            if (i in team2):
                button = Button(self.rightFrame, image=team2[i].getImage(), command=partial(self.chooseTarget, 1, i), height=buttonHeight, width=buttonWith)
            else:
                button = Button(self.rightFrame, image=self.emptyImg, command=partial(self.chooseTarget, 1, i), height=buttonHeight, width=buttonWith)

            button.grid(row=int(i / 2), column=i % 2)
            self.rightButtons += [button]


        if (self.moveChosenButton is None):
            self.moveChosenButton = Button(self.topFrame, text="Use Move", command=self.useMove, height=2, width=5)
            self.moveChosenButton.pack()


    def useMove(self):

        print("Using move")

        if (self.ability is not None and self.currentPlayer is not None):

            if (self.ability.isSet()):

                self.currentPlayer.move = self.ability
                self.currentPlayer = None
                self.ability = None


    def chooseAbility(self, id):

        print("attack_id-" + str(id))
        self.labelMsg.set("Using attack id-" + str(id))
        self.ability = self.currentPlayer.character.abilities[id]


    def loadAttackButton(self, player):

        self.attackButtons = []
        buttonWith = 100
        buttonHeigh = 100
        playerAbilities = player.character.abilities

        for i in range(len(playerAbilities)):

            image = playerAbilities[i].image
            button = Button(self.bottomFrame, image=image, command=partial(self.chooseAbility, i), height=buttonHeigh, width=buttonWith)
            button.grid(row=i%2, column=int(i/2))

            self.attackButtons += [button]


    def updateTurn(self, allPlayer, moves):

        if (not self.gameEngine.fightIsFinish):

            self.loadTeamButton(allPlayer)
            self.startTurn()


    def getHumanPlayerMove(self, player):

        self.currentPlayer = player
        self.loadAttackButton(player)


    def start(self):

        self.root.mainloop()