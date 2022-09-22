def make_board():
    # Define a 2D array to store the state of the game board. Initially, the board consists of six rows of entries, each with seven columns, and all entries are empty.
    game_board = [[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ']]
    return game_board

def print_board(my_board):
    # Generate a board in the terminal by printing a grid made up of hyphens and pipes.
    column_info = ''
    for i in range(0, len(my_board)):
        column_info += '   ' + str(i) + '  '
    print(column_info)
    for i in range(0, 4*len(my_board[0])+1):
        if (i % 4 == 0 ):
            print('x-----' * len(my_board) + 'x')
        elif (i % 4 == 2):
            line = '|'
            for j in range(0, len(my_board)):
                line += '  ' + str(my_board[j][i//4]) + '  |'
            print(line)
        else:
            line = '|'
            for j in range(0,len(my_board)):
                line += '     |'
            print(line)
    return None

def make_move(my_board, symbol, column):
    #Check to see if the select move is vaild. If not, return a message and re-prompt. If move is valid, implment the change to game board.
    if (column not in range(0, len(my_board))):
        print('The selected column does not exist. Please select a column number between ' + str(0) + ' and ' + str(len(my_board)-1) + '.')
        return my_board, False
    elif (my_board[column][0] != ' '):
          print('Column ' + str(column) + ' is full. Please select a different column.')
          return my_board, False
    else:
          for row in range(len(my_board[0])-1, -1, -1):
              #Starting with the row, check each row for an empty slot until one is found, set that entry to symbol and break out of the loop to prevent multiple entries from being added.
              if (my_board[column][row] == ' '):
                  my_board[column][row] = symbol
                  break
    return my_board, True

def has_won(symbol, board):
    #check for vertical matches
    for i in range(0,len(board)-3):
        for j in range(0,len(board[0])):
            if (board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == symbol):
                return True

    #check for horizontal matches
    for i in range(0,len(board)):
        for j in range(0,len(board[0])-3):
            if (board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == symbol):
                return True

    #check diagonals 
    for i in range(0,len(board)-3):
        for j in range(0,len(board[0])-3):
            if (board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == symbol):
                return True
    
    for i in range(0,len(board)-3):
        for j in range(3, len(board[0])):
            if (board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] == symbol):
                return True
                
    return False

def no_valid_moves(board):
    #Check if all columns are filled.
    if all(board[i][0] != ' ' for i in range(len(board))):
        return True
    else:
        return False 

def game_over(symbol, board):
    #Check if either the board has been filled or a winner has been found.
    if (has_won(symbol, board) or no_valid_moves(board)):
        return True
    else:
        return False


my_board = make_board() #Create an empty board.

print_board(my_board) #Print to board for visual reference.
symbol = 'X'
turn = 1 
while (not game_over(symbol, my_board)):
    if (turn >= 45):
      break
    column = ''
    move_made = False

    if (turn % 2 == 1):
        symbol = 'X'
        column = int(input("It is X's turn. Please select a column in which to place piece.")) #Ask for interger input from the terminal.
        my_board, move_made = make_move(my_board, symbol, column) #Make the desired move is allowed and update the move_made variable to progress to next turn.
        print_board(my_board) #Print the updated game board.

        if (has_won(symbol,my_board)):
            print("Winner!")
            print(symbol + " has won the game!")

        if (no_valid_moves(my_board)):
            print("It's a tie. No winner could be found.")
        
    
    if (turn % 2 == 0):
        symbol = 'O'
        column = int(input("It is O's turn. Please select a column in which to place piece.")) #Ask for interger input from the terminal.
        my_board, move_made = make_move(my_board, symbol, column) #Make the desired move is allowed and update the move_made variable to progress to next turn.
        print_board(my_board) #Print the updated game board.

        if (has_won(symbol,my_board)):
            print("Winner!")
            print(symbol + " has won the game!")

        if (no_valid_moves(my_board)):
            print("It's a tie. No winner could be found.")
    if (move_made):
        turn += 1
