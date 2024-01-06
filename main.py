from termcolor import colored

def init_field() -> [str]:
    return ["1", "2", "3","4", "5", "6","7", "8", "9"]

def print_field(field: [str]) -> [str]:
    print(f"\n {field[0]}|{field[1]}|{field[2]}\n {field[3]}|{field[4]}|{field[5]}\n {field[6]}|{field[7]}|{field[8]}")

def player_move(field: [str]) -> [str]:
    field_number = int(input(f"Spieler {colored('X', 'red')} ist am Zug. Bitte wählen Sie ein Feld aus: "))
    if field[field_number-1] == "X" or field[field_number-1] == "O":
        print('Dieses Feld ist leider schon belegt. Wählen Sie ein anderes aus.')
    else:
        field[field_number-1] = colored('X', 'red')
    return field

def computer_move(field: [str]) -> [str]:
    print(f"Spieler {colored('O', 'green')} ist am Zug.")
    found = False
    number = 0
    while(not found):
        if field[number] != colored('X', 'red') and field[number] != colored('O', 'green'):
            field[number] = colored('O', 'green')
            found = True
        number += 1
    return field

def check_over(field: [str]) -> bool:
    for i in [0,3,6]:
        if field[i] == field[i+1] and field[i+1] == field[i+2] and field[i] != " ":
            print(f'Spieler {field[i]} hat gewonnen')
            return True
    
    for i in [0,1,2]:
        if field[i] == field[i+3] and field[i+3] == field[i+6] and field[i] != " ":
            print(f'Spieler {field[i]} hat gewonnen')
            return True

    if field[0] == field[4] and field[4] == field[8] and field[0] != " ":
        print(f'Spieler {field[0]} hat gewonnen')
        return True
    elif field[2] == field[4] and field[4] == field[6] and field[2] != " ":
        print(f'Spieler {field[0]} hat gewonnen')
        return True
    return False

def game():
    field = init_field()
    print_field(field)
    over = False
    turn = 0
    while(not over):
        if turn == 0:
            field = player_move(field)
            turn += 1
        elif turn == 1: 
            field = computer_move(field)
            turn -= 1
        print_field(field)
        over = check_over(field)



if __name__ == '__main__':
    game()