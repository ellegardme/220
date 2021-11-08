"""
Name: Madeleine Ellegard
lab10.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def display_board(board):
    print("--------")
    counter = 0
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(board[counter], end="|")
            counter = counter + 1
        print("")
    print("--------")


def place_spot(board, spot, marker):
    board[spot - 1] = marker


def legal_spot(board, spot):
    if (board[spot] == "x" or board[spot] == "y") or (spot < 1 or spot > 9):
        return False
    else:
        return True


def game_won(board):
    winCon = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 9], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for condition in winCon:
        counter = 0
        for spot in condition:
            if board[spot - 1] == "x":
                counter = counter + 1
        if counter == 3:
            return "x wins"
        counter = 0
        for spot in condition:
            if board[spot - 1] == "y":
                counter = counter + 1
        if counter == 3:
            return "y wins"


def game_over(board, turn_count):
    if (game_won(board) == "x wins" or game_won(board) == "y wins") or (turn_count > 9):
        return True
    else:
        return False


def play_game():
    g_board = build_board()
    display_board(g_board)
    turn_count = 0
    player_x = "x"
    player_y = "y"
    while not game_over(g_board, turn_count):
        placement_x = eval(input("Where does player X want to place their mark? "))
        if legal_spot(g_board, placement_x):
            place_spot(g_board, placement_x, player_x)
            turn_count += 1
            display_board(g_board)
            if game_won(g_board):
                print("Game over X won!")
                break
        else:
            print("Not a legal spot")
        placement_y = eval(input("Where does player y want to place their mark? "))
        if legal_spot(g_board, placement_y):
            place_spot(g_board, placement_y, player_y)
            turn_count += 1
            display_board(g_board)
            if game_won(g_board):
                print("Game over Y won!")
                break
        else:
            print("Not a legal spot")





def main():
    play_game()


main()



