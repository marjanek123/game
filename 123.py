liczbaarab=input("podaj liczbe rzymska: ")
str(liczbaarab)
result=[]
for a in liczbaarab:
    result.append(a)

liczby2 = ["X","L","C"]
liczby1= ["X","L","C"]
liczby3=["I","V","X"]
liczby4=["I","V","X"]
board1=[]
board2=[]
board3=[]
szuflada=0
raz=0
def zmienrzymnaaraba(liczba,result,board,board1):
    for a in liczba:
        board.append(a)
    print(board)
    def zmien(board,board1):
        for e in range(len(board)):
            if(board[e]=="I"):

                try:
                    if(board[e]=="I" and board[e-1]=="V"):
                        board1.append(4)
                    elif (board[e] == "I" and board[e - 1] == "X"):
                        board1.append(9)
                except:
                    board1.append(1)
            elif(e=="V"):
                try:
                    if (board[e] == "V" and board[e +1] == "I"):
                        board1.append(4)
                except:
                    board1.append(5)
            elif (e == "X"):
                try:
                    if (board[e] == "X" and board[e +1] == "I"):
                        board1.append(9)
                    if (board[e] == "X" and board[e -1] == "C"):
                        board1.append(90)
                except:
                    board1.append(10)
            elif (e == "L"):
                try:
                    if (board[e] == "L" and board[e + 1] == "X"):
                        board1.append(40)
                except:
                    board1.append(50)
            elif (e == "C"):
                try:
                    if (board[e] == "C" and board[e + 1] == "X"):
                        board1.append(90)
                    if (board[e] == "C" and board[e - 1] == "M"):
                        board1.append(900)
                except:
                    board1.append(100)
            else:
                pass
        print(board1)
        return board1
    print(zmien(board,board1))






zmienrzymnaaraba(liczbaarab,result,board1,board2)