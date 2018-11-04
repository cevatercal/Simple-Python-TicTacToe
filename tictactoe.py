import os

board = [["-","-","-"],
         ["-","-","-"],
         ["-","-","-"]]


def printBoard():
        os.system("cls")
        print("    1    2    3")
        for x,y in enumerate(board):
                print (str(x+1) + " "+ str(y))
        print (" ")
        print (20*"-")
        print (" ")

def p1Move():
        p = input("X player : ").split()
        x , y = p
        if board[int(y)-1][int(x)-1] == "X" or board[int(y)-1][int(x)-1] == "O":
                print("Invalid Move")
                p1Move()
        else:
                board[int(y)-1][int(x)-1] = "X"
        printBoard()
        


def p2Move():
        p = input("O player :  ").split()
        x , y = p
        if board[int(y)-1][int(x)-1] == "X" or board[int(y)-1][int(x)-1] == "O":
                print("Invalid Move")
                p2Move()
        else:
                board[int(y)-1][int(x)-1] = "O"
        printBoard()


def check():
        if board[0][0] == board[1][0] == board[2][0] and board[0][0] !="-":
                print ("{} wins ".format(board[0][0]))
                return True
        elif board[0][1] == board[1][1] == board[2][1] and board[0][1] !="-":
                print ("{} wins ".format(board[0][1]))
                return True
        elif board[0][2] == board[1][2] == board[2][2] and board[0][2] !="-":
                print ("{} wins ".format(board[0][2]))
                return True
        elif board[0][0] == board[0][1] == board[0][2] and board[0][0] !="-":
                print ("{} wins ".format(board[0][0]))
                return True
        elif board[1][0] == board[1][1] == board[1][2] and board[1][0] !="-":
                print ("{} wins ".format(board[1][0]))
                return True
        elif board[2][0] == board[2][1] == board[2][2] and board[2][0] !="-":
                print ("{} wins ".format(board[2][0]))
                return True
        elif board[0][0] == board[1][1] == board[2][2] and board[1][1] !="-":
                print ("{} wins ".format(board[1][1]))
                return True
        elif board[0][2] == board[1][1] == board[2][0] and board[1][1] !="-":
                print ("{} wins ".format(board[1][1]))
                return True
        return False
turn=0
printBoard()
while True:
        if turn == 9:
                print ("It's a draw")
                break
        elif turn%2 == 0:
                p1Move()
                if check():
                        break
                
        else:
                p2Move()
                if check():
                        break
        turn+=1
                 



