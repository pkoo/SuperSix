from random import randint

class Player:
    def __init__(self, name, sticks):
        self.name = name
        self.sticks = sticks
        self.countDiceThrows = 0

    def __str__(self):
        if self.sticks > 0:
            return "{0} hat bereits {1} mal gewürfelt und noch {2} Stäbe".format(self.name, self.countDiceThrows, self.sticks)
        else:
            return "{0} hat mit {1} würfen alle Stäbe untergebracht".format(self.name, self.countDiceThrows)

    def throwDice(self):
        value = randint(1,6)
        self.countDiceThrows += 1
        print("{0} würfelt eine {1}".format(self.name, value))
        return value

    def makeChoice(self):
        value = input('Möchtest du erneut würfeln? [ja, (n)ein] ')
        if value in ['ja', 'j', '1','J','Ja']:
            return True
        else:
            return False