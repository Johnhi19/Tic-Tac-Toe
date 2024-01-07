from termcolor import colored

class Player:
    def __init__(self, mark) -> None:
        self.mark = mark
    
    def make_move(self, field):
        pass

class Human_Player(Player):
    def __init__(self, mark) -> None:
        super().__init__(mark)
    
    def make_move(self, field):
        field_number = int(input(f"Spieler {self.mark} ist am Zug. Bitte wählen Sie ein Feld aus: "))
        if field[field_number-1] == "X" or field[field_number-1] == "O":
            print('Dieses Feld ist leider schon belegt. Wählen Sie ein anderes aus.')
        else:
            field[field_number-1] = self.mark
        return field

class Computer_Player(Player):
    def __init__(self, mark) -> None:
        super().__init__(mark)
    
    def make_move(self, field):
        print(f"Spieler {self.mark} ist am Zug.")
        found = False
        number = 0
        while(not found):
            if field[number] != colored('X', 'red') and field[number] != colored('O', 'green'):
                field[number] = self.mark
                found = True
            number += 1
        return field