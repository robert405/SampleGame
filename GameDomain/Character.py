from GameDomain.Stats import Stats
from GameDomain.Ability import Ability

class Character:

    def __init__(self):

        self.baseStats = Stats()
        self.abilities = [Ability("./Ressource/SwordAttack.jpg"),
                          Ability("./Ressource/LightningAttack.jpg"),
                          Ability("./Ressource/SolarAttack.jpg"),
                          Ability("./Ressource/CloudAttack.jpg")]