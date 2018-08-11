from Player import Player
from Board import Board


class SuperSix:
    def __init__(self):
        self.sticks = 20
        self.players = []
        self.mode = 1
        self.run = True
        self.turn = 0
        self.board = Board()

    def game_move(self, user):
        dice = user.throwDice()
        ret = self.board.putStick(dice-1)

        if ret is True:
            user.sticks -= 1
        else:
            user.sticks += 1

        print(user)
        print(self.board)

        # In der ersten Runde würfelt jeder Spieler nur einmal und hat keine Entscheidungsmöglichkeit
        # danach kann der Spieler entscheiden, noch einmal zu würfeln
        if ret is True and self.turn > 1:
            if user.sticks > 0 and user.makeChoice() is True:
                self.game_move(user)

    def game_loop(self):
        while self.run:
            self.turn += 1
            print("#"*5 + " Runde " + str(self.turn) + " " + "#"*5)
            for current_player in self.players:
                input('Nächster Spieler')
                self.game_move(current_player)
                if current_player.sticks <= 0:
                    self.run = False
                    break

            if self.run is True: input('Nächste Runde')


########################################################################################################################
if __name__ == "__main__":
    s = SuperSix()
    s.sticks = int(input('Mit wie vielen Stäben soll jeder Spieler beginnen? '))
    player = int(input('Wie viele Spieler wollen mitmachen? [2-4] '))
    if player < 2 or player > 4:
        print('Es muss eine Zahl zwischen 2 und 4 sein.')
        exit(1)

    for i in range(player):
        name = input('Wie soll Spieler {0} heißen? '.format(i+1))
        s.players.append(Player(name, s.sticks))

    s.game_loop()

    print("#"*25 + "\n")
    print('Es wurden {0} Stäbe in die Kiste geworfen.'.format(s.board.board[5]))
    for p in s.players:
        print(p)

else:
    print("Sorry, currently not importable as a module.")