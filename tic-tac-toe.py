board = ["1","2","3","4","5","6","7","8","9"]
def printboard():
    print(board[0],"!",board[1],"!",board[2])
    print(board[3],"!",board[4],"!",board[5])
    print(board[6],"!",board[7],"!",board[8])

printboard()
player1 = "x"
player2 = "o"

for i in range (5):
    position = int(input("enter the post:"))

    if position < 1 or position >9:
        print("invalid position")
        continue

    if board[position-1] not in ["x","o"]:
        board[position-1] = "x"
    else:
        print("already taken")
        continue
    printboard()
    
    if (board[0]==board[1]==board[2]or
        board[3]==board[4]==board[5]or
        board[6]==board[7]==board[8]or
        board[0]==board[4]==board[8]or
        board[6]==board[4]==board[2]or
        board[0]==board[3]==board[6]or
        board[1]==board[4]==board[7]or
        board[5]==board[8]==board[2]):
        print("player1 is winner")
        break
    sec_position = int(input("enter the sec player post:"))

    if sec_position < 1 or sec_position >9:
        print("invalid position")
        continue
    if board[sec_position-1] not in ["x","o"]:
        board[sec_position-1] = "o"
    else:
        print("already taken")
        continue
    printboard()
    if (board[0]==board[1]==board[2]or
        board[3]==board[4]==board[5]or
        board[6]==board[7]==board[8]or
        board[0]==board[4]==board[8]or
        board[6]==board[4]==board[2]or
        board[0]==board[3]==board[6]or
        board[1]==board[4]==board[7]or
        board[5]==board[8]==board[2]):
        print("player2 is winner")
        break
else:
        print("print draw")



