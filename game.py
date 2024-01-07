import player
from termcolor import colored

class Game:
    def __init__(self) -> None:
        self.field = ["1", "2", "3","4", "5", "6","7", "8", "9"]
        self.player1, self.player2 = self.start_game()

    def print_field(self):
        print(f"\n {self.field[0]}|{self.field[1]}|{self.field[2]}\n {self.field[3]}|{self.field[4]}|{self.field[5]}\n {self.field[6]}|{self.field[7]}|{self.field[8]}")

    def check_over(self) -> bool:
        for i in [0,3,6]:
            if self.field[i] == self.field[i+1] and self.field[i+1] == self.field[i+2] and self.field[i] != " ":
                print(f'Spieler {self.field[i]} hat gewonnen')
                return True
        
        for i in [0,1,2]:
            if self.field[i] == self.field[i+3] and self.field[i+3] == self.field[i+6] and self.field[i] != " ":
                print(f'Spieler {self.field[i]} hat gewonnen')
                return True

        if self.field[0] == self.field[4] and self.field[4] == self.field[8] and self.field[0] != " ":
            print(f'Spieler {self.field[0]} hat gewonnen')
            return True
        elif self.field[2] == self.field[4] and self.field[4] == self.field[6] and self.field[2] != " ":
            print(f'Spieler {self.field[0]} hat gewonnen')
            return True
        return False
    
    def start_game(self):
        while(True):
            option = int(input("Möchten Sie gegen ein Computer (1) oder gegen einen anderen Spieler (2) spielen?\n"))
            if option != 1 and option != 2:
                print("Das ist keine gültige Eingabe. Bitte versuchen sie es nochmal.")
            else: 
                break
        if option == 1:
            return player.Human_Player(colored('X','red')), player.Computer_Player(colored('O', 'green'))
        else:
            return player.Human_Player(colored('X','red')), player.Human_Player(colored('O', 'green'))

    def game_process(self):
        self.print_field()
        over = False
        turn = 0
        while(not over):
            if turn == 0:
                self.field = self.player1.make_move(self.field)
                turn += 1
            elif turn == 1: 
                self.field = self.player2.make_move(self.field)
                turn -= 1
            self.print_field()
            over = self.check_over()