board=["-","-","-",
       "-","-","-",
       "-","-","-"]
game_continues=True
winner=None
current='X'
def display():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play():
   
    display()
    while game_continues:
        handle_turn(current)
        check_game_over()
        flip()
    if winner=='X' or winner=='O':
        print(f"{winner} has won,congrats")
    else:
        print("Game has ended in a draw")


def handle_turn(player):
    print(player +" 's turn")
    spot=input("Enter which position(1-9) do you want to place: ")
    valid=False
    while not valid:
        while spot not in ["1","2","3","4","5","6","7","8","9"]:
            spot=input("Enter which position(1-9) do you want to place")
        spot=int(spot)-1
        if board[spot]=='-':
            valid=True
        else:
            print("You cannot place in that spot,already occupied")   
    board[spot]=player
    display()

def check_game_over():
    check_won()
    check_draw()

def check_won():
    global winner
    row=check_rows()
    column=check_columns()
    diagnol=check_diagnols()
    if row:
        winner=row
    elif column:
        winner=column
    elif diagnol:
        winner=diagnol
    else:
        winner=None
    return 

def check_rows():
    global game_continues
    row1=board[0]==board[1]==board[2]!="-"
    row2=board[3]==board[4]==board[5]!="-"
    row3=board[6]==board[7]==board[8]!="-"
    if row1 or row2 or row3:
        game_continues=False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return 


def check_columns():
    global game_continues
    col1=board[0]==board[3]==board[6]!="-"
    col2=board[1]==board[4]==board[7]!="-"
    col3=board[2]==board[5]==board[8]!="-"
    if col1 or col2 or col3:
        game_continues=False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return  

def check_diagnols():
    global game_continues
    diag1=board[0]==board[4]==board[8]!="-"
    diag2=board[2]==board[4]==board[6]!="-"

    if diag1 or diag2:
        game_continues=False
    if diag1:
        return board[0]
    elif diag2:
        return board[2]
    return  

def check_draw():
    global game_continues
    if '-' not in board and winner==None:
        game_continues=False
    return 

    

def flip():
    global current
    if current=='X':
        current='O'
    else:
        current='X'


play()