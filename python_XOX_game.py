
print(""" 0 1 2
 3 4 5
 6 7 8""", " \n Please consider the numbers here when making your selection.")

game_area = ["-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-"]

def draw_board(game_area):
    print("**********")
    print(" {} | {} | {}".format(game_area[0], game_area[1], game_area[2]))
    print("----------")
    print(" {} | {} | {}".format(game_area[3], game_area[4], game_area[5]))
    print("----------")
    print(" {} | {} | {}".format(game_area[6], game_area[7], game_area[8]))
    print("**********")

def get_move(player):
    while True:

        move = int(input(" Where you want to put X or O please enter that number (0-8): "))
        if game_area[move] == "-":
            game_area[move] = player
            break
        else:
            print("This point is already occupied. Please  be carefull.")


def won_control(player):

    # Row control
    if game_area[0] == player and game_area[1] == player and game_area[2] == player:
        return True
    if game_area[3] == player and game_area[4] == player and game_area[5] == player:
        return True
    if game_area[6] == player and game_area[7] == player and game_area[8] == player:
        return True

    # Column control
    if game_area[0] == player and game_area[3] == player and game_area[6] == player:
        return True
    if game_area[1] == player and game_area[4] == player and game_area[7] == player:
        return True
    if game_area[2] == player and game_area[5] == player and game_area[8] == player:
        return True
    # croswise control
    if game_area[0] == player and game_area[4] == player and game_area[8] == player:
        return True
    if game_area[2] == player and game_area[4] == player and game_area[6] == player:
        return True
# My main goal in this section is to find the winner of the game (x-o) if any 3 rows or 3 columns have the same character
# Therefore the system will return True if the rows and columns contain the same character and crosswise the same character.
def main():
    PLAYER1 = "X"
    while True:
        draw_board(game_area)
        get_move(PLAYER1)
        if won_control(PLAYER1):
            print(f"Player {PLAYER1} has won!")
            break
        PLAYER1 = "O" if PLAYER1 == "X" else "X"

main()
