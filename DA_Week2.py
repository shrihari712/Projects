# Step 1: Initialize the game display
positions = ['G', 'G', 'G', '-', 'B', 'B', 'B']

# Step 2: Accept positions of the frog that you want to move
print("[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]")
print(positions)

def move_frog(pos):
    # Validate position
    if pos < 0 or pos > 6 or positions[pos] == '-':
        return "Invalid Move"

    # Move green frog to the right
    if positions[pos] == 'G':
        if pos + 1 <= 6 and positions[pos + 1] == '-':
            positions[pos], positions[pos + 1] = positions[pos + 1], positions[pos]
        elif pos + 2 <= 6 and positions[pos + 2] == '-' and positions[pos + 1] == 'B':
            positions[pos], positions[pos + 2] = positions[pos + 2], positions[pos]
        else:
            return "Invalid Move"

    # Move brown frog to the left
    elif positions[pos] == 'B':
        if pos - 1 >= 0 and positions[pos - 1] == '-':
            positions[pos], positions[pos - 1] = positions[pos - 1], positions[pos]
        elif pos - 2 >= 0 and positions[pos - 2] == '-' and positions[pos - 1] == 'G':
            positions[pos], positions[pos - 2] = positions[pos - 2], positions[pos]
        else:
            return "Invalid Move"
        
    return "Move Completed"

# Step 3: Check for winning condition
def check_win():
    if positions == ['B', 'B', 'B', '-', 'G', 'G', 'G']:
        return True
    return False

# Step 4: Main game loop
def play_game():  
    while True:
        move = input("Enter position to move (0-6) or 'q' to quit: ")
        if move == 'q':
            print("Game Quit")
            break
        try:
            move = int(move)
        except ValueError:
            print("Invalid Input. Please enter a number between 0-6 or 'q' to quit.")
            continue
        
        result = move_frog(move)
        if result == "Invalid Move":
            print(result)
            continue
        
        if check_win():
            print("You Win!")
            break

# Start the game
play_game()
