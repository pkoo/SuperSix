class Board:
    def __init__(self):
        # in dem 6ten Slot zählern wir die Anzahl an Sticks die dort eingeworfen werden
        self.board = [0, 0, 0, 0, 0, 0]

    # Der 6te Slot im Board sammelt alle Stäbe und ist ein Zähler
    # Dieser wird daher für die Ausgabe nicht benötigt
    def __str__(self):
        return str(self.board[:-1])

    def putStick(self, position):
        if position == 5:
            self.board[position] += 1
            return True
        else:
            if self.board[position] == 0:
                self.board[position] = 1
                return True
            else:
                self.board[position] = 0
                return False