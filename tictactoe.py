# Initialize the game board
board = [[" " for _ in range(3)] for _ in range(3)]


# Function to display the game board
def grid():
    print("---------")
    for row in board:
        print(f"| {' '.join(row)} |")
    print("---------")


# Define winning patterns
winning_patterns = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]  # Diagonal
]

# Initialize game variables
queue = 0

# Main game loop
while True:
    grid()

    if queue % 2 == 0:
        player = 'X'
    else:
        player = 'O'

    coor = input()

    # Check if the input is empty (user pressed Enter)
    if not coor:
        print("Please enter coordinates.")
        continue

    # Split input into row and column
    row, col = map(int, coor.split())

    # Check if coordinates are valid
    if not (1 <= row <= 3) or not (1 <= col <= 3):
        print("Coordinates should be from 1 to 3!")
        continue

    # Check if the selected cell is already occupied
    if board[row - 1][col - 1] != " ":
        print("This cell is occupied! Choose another one!")
        continue

    # Update the board with the player's move
    board[row - 1][col - 1] = player

    # Check for a win after the player's move
    for pattern in winning_patterns:
        if all(board[i // 3][i % 3] == player for i in pattern):
            grid()
            print(f"{player} wins")
            exit()

    # Check for a draw
    if all(cell != " " for row in board for cell in row):
        grid()
        print("Draw")
        exit()

    # Switch to the next player
    queue += 1
