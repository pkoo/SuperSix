class SuperSix:
    def __init__(self):
        self.sticks = 20
        self.players = []
        self.mode = 1


    def print_main_menu(self):
        print("#"*20)
        print('1) Anzahl Spieler festlegen')
        print('2) Anzahl Stäbe pro Spieler ändern: ', self.sticks)
        if self.mode == 1:
            print('s) Spiel mit einem Würfel starten')
        else:
            print('s) Spiel mit zwei Würfeln starten')
        print('m) Spielmodus ändern')
        print('e) Ende')


if __name__ == "__main__":
    s = SuperSix()
    while True:
        s.print_main_menu()
        auswahl = input(':')
        if auswahl in ['1','2','s','x','m']: # Das e wird hier explizit nicht abgefragt, da es das Programm beenden soll
            print('Legitime Auswahl')
        else:
            if auswahl == 'e': break
            print('Kein valider Menüpunkt.')
else:
    print("Sorry, currently not importable as a module.")