import random
board = [" "," "," "," "," "," "," "," "," "]
def display_board():
        print("")
        print("| "+board[0]+" | "+board[1]+" | "+board[2]+" | ")
        print("| "+board[3]+" | "+board[4]+" | "+board[5]+" | ")
        print("| "+board[6]+" | "+board[7]+" | "+board[8]+" | ")
        print("")
def wincheck(mark):
        return((board[0]==mark and board[1]== mark and board[2]==mark )or #for row1 
            (board[3]==mark and board[4]==mark and board[5]==mark )or
            (board[6]==mark and board[7]==mark and board[8]==mark )or
            (board[0]==mark and board[3]==mark and board[6]== mark )or
            (board[1]==mark and board[4]==mark and board[7]==mark )or
            (board[2]==mark and board[5]==mark and board[8]==mark )or
            (board[0]==mark and board[4]==mark and board[8]==mark )or
            (board[2]==mark and board[4]==mark and board[6]==mark ))
def make_turn(turn, pos):
    if turn:
        letter = "O"
    else:
        letter = "X"
    board[pos-1] = letter
    display_board()
turn = random.randint(0, 1)
#display_board()
print("""
board alignment:

| 1 | 2 | 3 | 
| 4 | 5 | 6 |
| 7 | 8 | 9 |

""")
while True:
    if turn:
        player = "O"
    else:
        player = "X"
    pos= int(input(player + "'s turn: "))
    if board[pos-1] != " ":
        print("Taken, choose another")
        continue
    make_turn(turn, pos)
    if wincheck(player):
        print(player + " wins!")
        break
    elif " " not in board:
        print("Draw")
        break
    turn = not turn
    print("-" * 20)
input("")
