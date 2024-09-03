import random

board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

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

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

    player_move = int(input("\n\nEnter your move: "))
            
    if player_move >= 1 and player_move <= 9:
        if player_move >= 1 and player_move <= 3:
            list1 = board[0]
            if player_move in list1:
                for play1 in list1:
                    if play1 == player_move:
                        board[0][play1 - 1] = "O"
            else:
                print("Move Unavailable!")

        elif player_move >= 4 and player_move <= 6:
            list2 = board[1]
            if player_move in list2:
                for play2 in list2:
                    if play2 == player_move:
                        board[1][play2 - 4] = "O"
            else:
                print("Move Unavailable!")

        elif player_move >= 7 and player_move <= 9:
            list3 = board[2]
            if player_move in list3:
                for play3 in list3:
                    if play3 == player_move:
                        board[2][play3 - 7] = "O"
            else:
                print("Move Unavailable!")
        
def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game 

    Win = False 

    if sign == board[0][0] and sign == board[1][1] and sign == board[2][2]:
        Win = True #Win [1, 5, 9]
    elif sign == board[0][2] and sign == board[1][1] and sign == board[2][0]:
        Win = True #Win [3, 5, 7]

    for num in range(3):
        if sign == board[num][0] and sign == board[num][1] and sign == board[num][2]:
            Win = True #Wins [1, 2, 3] [4, 5, 6] [7, 8, 9]
        elif sign == board[0][num] and sign == board[1][num] and sign == board[2][num]:
            Win = True #Wins [1, 4, 7] [2, 5, 8] [3, 6, 9]
    return Win

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    my_tuple = []

    for num in range(len(board)):
        for xen in board[num]:
            subitem_tuple = ()
            
            if isinstance(xen, int):
                if xen >= 1 and xen <= 3:
                    subitem_tuple = (num, xen-1)
                    
                elif xen >= 4 and xen <= 6:
                    subitem_tuple = (num, xen-4)
                    
                elif xen >= 7 and xen <= 9:
                    subitem_tuple = (num, xen-7)

                my_tuple.append(subitem_tuple)

    return my_tuple

def draw_move(board):
    # The function draws the computer's move and updates the board.
    # from random import randrange
    avail_moves = make_list_of_free_fields(board)
    computer_moves = []

    for num in range(3): #Only gives the computer the available moves
        if num == 0:
            for xen1 in range(3):
                if (num, xen1) in avail_moves:
                    computer_moves.append(xen1+1)

        elif num == 1:
            for xen2 in range(3):
                if (num, xen2) in avail_moves:
                    computer_moves.append(xen2+4)

        elif num == 2:
            for xen3 in range(3):
                if (num, xen3) in avail_moves:
                    computer_moves.append(xen3+7)

    if len(computer_moves) > 0: #Ensures there are available moves to play
        move = random.choice(computer_moves)

    if len(computer_moves) > 0:
        if move >= 1 and move <= 9:
            if move >= 1 and move <= 3:
                list1 = board[0]
                if move in list1:
                    for play1 in list1:
                        if play1 == move:
                            board[0][play1 - 1] = "X"

            elif move >= 4 and move <= 6:
                list2 = board[1]
                if move in list2:
                    for play2 in list2:
                        if play2 == move:
                            board[1][play2 - 4] = "X"

            elif move >= 7 and move <= 9:
                list3 = board[2]
                if move in list3:
                    for play3 in list3:
                        if play3 == move:
                            board[2][play3 - 7] = "X"



win = False #Dummy to start the while loop

while win == False:
    available_moves = make_list_of_free_fields(board)
    if len(available_moves) < 1: # Checks if there are moves left to play
        print("\nIt's a Tie!")
        win = True

    else:
        display_board(board)
        enter_move(board)
        player_wins = victory_for(board, "O")
        win = player_wins

        draw_move(board)
        computer_wins = victory_for(board, "X")
        win = computer_wins

if player_wins:
    display_board(board)
    print("\n\nYou Win!!") 

elif computer_wins:
    display_board(board)
    print("\n\nYou Lose!!")