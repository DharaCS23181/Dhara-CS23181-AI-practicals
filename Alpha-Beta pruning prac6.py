board = [" "," "," ",
         " "," "," ",
         " "," "," "]
def show():
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])
    print()
def winner(p):
    win = [(0,1,2),(3,4,5),(6,7,8),
           (0,3,6),(1,4,7),(2,5,8),
           (0,4,8),(2,4,6)]
    for a,b,c in win:
        if board[a]==board[b]==board[c]==p:
            return True
    return False
def alphabeta(isMax, alpha, beta):
    if winner("X"):
        return 1
    if winner("O"):
        return -1
    if " " not in board:
        return 0
    if isMax:
        best = -100
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = alphabeta(False, alpha, beta)
                board[i] = " "
                best = max(best, score)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = alphabeta(True, alpha, beta)
                board[i] = " "
                best = min(best, score)
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best
while True:
    show()
    move = int(input("Enter position (0-8): "))
    if board[move] != " ":
        print("Position already filled!")
        continue
    board[move] = "O"
    if winner("O"):
        show()
        print("You Win!")
        break
    if " " not in board:
        show()
        print("Game Draw!")
        break
    bestVal = -100
    bestMove = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            moveVal = alphabeta(False, -100, 100)
            board[i] = " "
            if moveVal > bestVal:
                bestMove = i
                bestVal = moveVal
    board[bestMove] = "X"
    print("AI Move:", bestMove)
    if winner("X"):
        show()
        print("AI Wins!")
        break
    if " " not in board:
        show()
        print("Game Draw!")
        break