from GameDomain.Effect import *
import random

class Ability:

    def __init__(self):

        self.effect = Attack()
        self.accuracy = 0.95
        self.teamTarget = None
        self.idTarget = None
        self.targetIsSet = False


    def set(self, teamTarget, idTarget):

        self.teamTarget = teamTarget
        self.idTarget = idTarget
        self.targetIsSet = True

    def isSet(self):

        return self.targetIsSet


    def apply(self, character):

        if (random.random() <= self.accuracy):

            self.effect.apply(character)