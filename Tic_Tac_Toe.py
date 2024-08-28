

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    for i in range(4):
        for num in range(3):
            if num == 0:
                print("\n+", end="")
            print("-------+", end="") 
            
        for xen1 in range(3):
            if i == 3:
                break
            if xen1 == 0:
                print("\n|", end="")
            print(f"       |", end="")
        
        for xen in range(3):
            if i == 3:
                break
            if xen == 0:
                print("\n|", end="")
            print(f"   {board[i][xen]}   |", end="")
        
        for xen2 in range(3):
            if i == 3:
                break
            if xen2 == 0:
                print("\n|", end="")
            print(f"       |", end="")
board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
#display_board(board)

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    pass


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    pass


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    pass


def draw_move(board):
    # The function draws the computer's move and updates the board.
    pass


# from random import randrange

# for i in range(10):
#     print(randrange(8))

