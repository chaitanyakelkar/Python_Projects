import random
board = [" " for x in range(10)]
board[0] = None
def boardreset():
    global board
    for i in range(len(board)):
        board[i] = " "
def printboard():
    print("\t"+board[1],board[2],board[3],sep=" | ")
    print("\t"+"---------")
    print("\t"+board[4],board[5],board[6],sep=" | ")
    print("\t"+"---------")
    print("\t"+board[7],board[8],board[9],sep=" | ")
def isfull():
    if " " in board[1:9]:
        return False
    else:
        return True
def wins(bo,let):
    return (bo[1] == let and bo[2] == let and bo[3] == let) or \
            (bo[4] == let and bo[5] == let and bo[6] == let) or \
            (bo[7] == let and bo[8] == let and bo[9] == let) or \
            (bo[1] == let and bo[4] == let and bo[7] == let) or \
            (bo[2] == let and bo[5] == let and bo[8] == let) or \
            (bo[3] == let and bo[6] == let and bo[9] == let) or \
            (bo[1] == let and bo[5] == let and bo[9] == let) or \
            (bo[3] == let and bo[5] == let and bo[7] == let)
def playermove():
    run = True
    while run:
        try:
            move = int(input("enter a move(1-9)"))
            if move > 9 or move < 1:
                print("enter a number in range")
            else:
                if board[move] == " ":
                    board[move] = "X"
                    printboard()
                    run = False
                else:
                    print("the place is already occupied")
        except ValueError:
            print("ENter a number")
def compmove():
    move = 0
    possibilities = [x for x,y in enumerate(board) if y == " " and x != 0]
    copyboard = board[:]
    for i in ["O","X"]:
        for j in possibilities:
            copyboard[j] = i
            if wins(copyboard,i):
                move = j
                return move
            else:
                copyboard[j] = " "
    if 5 in possibilities:
        move = 5
        return move
    for i in [1,3,7,9]:
        if i in possibilities:
            move  = i
            return move
    if not isfull():
        move = possibilities[random.randrange(0,len(possibilities))]
        return move
    return move
def game():
    boardreset()
    print("this is a tic tac toe game yoo will be 'X' and pc will be'O'")
    printboard()
    while True:
        if (not wins(board,"O")) or (not isfull()):
            playermove()
        else:
            if wins(board,"O"):
                print("Pc wins")
                boardreset()
                break
            elif isfull():
                print("its a tie")
                boardreset()
                break
        if (not wins(board,"X")) or (not isfull()):
            move = compmove()
            if move == 0:
                print("Its a tie")
                break
            else:
                board[move] = "O"
                print(f"PC played a move and inserted 'O' at {move}")
                printboard()
        elif wins(board,"X"):
            print("Congrats you win")
            boardreset()
            break
        else:
            print("Its a tie")
            boardreset()
            break
while True:
    game()
    ans = input("Do you want to play again?(y/n)")
    if ans == 'N' or ans == 'n':
        break