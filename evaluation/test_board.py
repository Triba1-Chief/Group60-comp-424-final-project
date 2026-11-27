import numpy as np
from helpers import LINES, top_view
from constants import OBSTACLE


BOARD = np.zeros((4, 4, 3), dtype=np.int8)
BOARD[0, 0, 2] = 1  # Blue small
BOARD[0, 1, 0] = 2  # Brown small, covered
BOARD[0, 1, 1] = 1  # Blue medium
BOARD[1, 2, 2] = 2  # Brown large
BOARD[2, 2, :] = 3 # Obstacle
#BOARD[0, 2, 0] = 1 #Blue small piece
#BOARD[0, 2, 0] = 2 #Brown medium piece

LINE_WEIGHTS = [0, 2, 4, 16]
SIZE_WEIGHTS = [0, 3, 6]


#Displaying piece sizes and owners
owners, sizes = top_view(BOARD)
print("Visible owners:")
print(owners)

print("\nVisible sizes:")
print(sizes)


#H1:Giving weight to pieces on possible winning lines. Evaluate assumes non-terminal states only
def evaluateLine(board, reserves, player, opponent): #Uncontested version
    owners, sizes = top_view(BOARD)
    score = 0

    for line in LINES[4]: #10 winning lines
        cells = [owners[r, c] for r, c in line]

        if OBSTACLE in cells: #disqualifies the line from counting towards heuristic as line can't win.
            continue

        my_count = cells.count(player)
        opp_count = cells.count(opponent)

        if opp_count == 0 and my_count < 4:
            score += LINE_WEIGHTS[my_count]

        if my_count == 0 and opp_count < 4:
            score -= LINE_WEIGHTS[opp_count]

    return score

print("\nEvaluation for Blue:", evaluateLine(BOARD, None, 1, 2))
print("Evaluation for Brown:", evaluateLine(BOARD, None, 2, 1))


#H2: Giving weight to lines and size of piece
def evaluateLinesandSize(board, reserves, player, opponent):
    owners, sizes = top_view(BOARD)
    score = 0

    #Line potential
    for line in LINES[4]:
        cells = [int(owners[r, c]) for r, c in line]

        if OBSTACLE in cells:
            continue

        my_count = cells.count(player)
        opp_count = cells.count(opponent)

        if opp_count == 0 and my_count < 4:
            score += LINE_WEIGHTS[my_count]

        if my_count == 0 and opp_count < 4:
            score -= LINE_WEIGHTS[opp_count]

    #Piece size
    for r in range(4):
        for c in range(4):
            owner = owners[r, c]
            size = sizes[r, c]

            if owner == player:
                score += SIZE_WEIGHTS[size]

            elif owner == opponent:
                score -= SIZE_WEIGHTS[size]

    return score

print("\nEvaluation for Blue:", evaluateLinesandSize(BOARD, None, 1, 2))
print("Evaluation for Brown:", evaluateLinesandSize(BOARD, None, 2, 1))




