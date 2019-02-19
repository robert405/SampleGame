from GameDomain.Character import Character
from GameDomain.Player import Player
import time
import PIL
import numpy as np

class HumanPlayer(Player):

    def __init__(self, mainWindow, team):

        self.character = Character()
        self.move = None
        self.mainWindow = mainWindow
        self.image = self.getBaseImage(team)
        self.currentImage = None


    def getMove(self, players, queue):

        self.mainWindow.getHumanPlayerMove(self)

        while (self.move is None):
            time.sleep(0.5)

        queue.put(self.move)
        self.move = None


    def getImage(self):

        copy = np.copy(self.image)
        maxLife = 100
        currentLife = self.character.baseStats.life

        shape = copy.shape
        maxLifeLine = shape[1]
        currentLifeLine = int((currentLife/maxLife)*maxLifeLine)

        height = shape[0] - 30
        margin = 10

        copy[height:height+margin,:] = [150,150,150]
        copy[height:height+margin, 0:currentLifeLine] = [255, 0, 0]

        self.currentImage = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(copy))

        return self.currentImage


    def getBaseImage(self, team):

        if (team == 0):
            return np.asarray(PIL.Image.open("./Ressource/Team1.jpg"))
        else:
            return np.asarray(PIL.Image.open("./Ressource/Team2.jpg"))
