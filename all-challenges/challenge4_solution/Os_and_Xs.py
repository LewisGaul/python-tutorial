# Noughts and crosses game to play in shell/command line.
# There are a couple of built-in functions I have used which I haven't
# introduced so far, check what they do by typing in shell:
# help(str.format)
# help(str.join)
# help(str.strip)
# help(str.split)
# help(str.replace)
# help(str.isdigit)
# help(all)
# I also make a lot of use of defining functions (as is good practice), and
# use a nested list (list of lists) for the board, and list comprehensions.


def print_board(grid):
    cell = ' {} '
    row = '|'.join(3*[cell])
    sep = '+'.join(3*['---'])
    board = '\n'.join([row, sep, row, sep, row])
    # Flatten the list of lists (grid).
    print(board.format(*[i for r in grid for i in r]))

def parse_move(user_input):
    # Return None if invalid form of input, otherwise parse into a list of
    # two coordinates.
    # Transform to list of 2 strings which were separated by comma or spaces.
    user_input = user_input.strip(" ([)]'").replace(',', ' ').split(maxsplit=1)
    move = []
    for i in user_input:
        if not i.isdigit(): #invalid input
            return None
        i = int(i) #Convert string to integer
        if i < 1 or i > 3: #out of bounds integer
            return None
        move.append(int(i)-1)
    if len(move) != 2:
        return None
    else:
        return move

def is_valid_move(grid, move):
    # Return True or False depending on whether the given move is valid.
    if move is None:
        return False
    if grid[move[1]][move[0]] == ' ':
        return True
    else:
        return False

def check_winner(grid):
    # If there is a winner, return who it is, otherwise return None.
    # Check horizontals:
    for row in grid:
        if row[0] != ' ' and all([cell==row[0] for cell in row]):
            return row[0]
    # Check verticals:
    for j in range(3):
        col = [grid[i][j] for i in range(3)]
        if col[0] != ' ' and all([cell==col[0] for cell in col]):
            return col[0]
    # Check diagonals:
    diag1 = [grid[i][i] for i in range(3)]
    diag2 = [grid[i][-i-1] for i in range(3)]
    if diag1[0] != ' ' and all([cell==diag1[0] for cell in diag1]):
        return diag1[0]
    if diag2[0] != ' ' and all([cell==diag2[0] for cell in diag2]):
        return diag2[0]
    return None

player = 'X' #player X goes first
grid = [[' ', ' ', ' '] for i in range(3)]
winner = None
print("")
print_board(grid)
while winner is None:
    # Convert the input to a list of two integer indices if possible.
    move = parse_move(input("Choose a cell to go in: "))
    # Check if we have been given a valid move.
    while not is_valid_move(grid, move):
        print("Invalid choice, choose empty cell in format 'col row'.")
        move = parse_move(input("Choose a cell to go in: "))
    # Move has been checked, we can now assign that cell to the current player.
    grid[move[1]][move[0]] = player
    print_board(grid)
    # If there's a winner stop the game.
    if check_winner(grid) is not None:
        print("Winner is {}!".format(check_winner(grid)))
        break
    # If all cells are taken the game is over.
    elif len([c for r in grid for c in r if c == ' ']) == 0:
        print("It's a draw!")
        break
    # Switch player.
    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'




