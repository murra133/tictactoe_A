
from ast import Yield



def display(arr):
    print('\n')
    bottom = "   ------------"
    l=0
    print('   x0| x1 | x2')
    print(bottom)
    for x in arr:
        res = "y"+str(l)+" "+x[0]+" | "+x[1]+"  |  "+x[2]
        l=l+1
        print(res)
        print(bottom)

def check_choice(input):
    # Checks if Symbol is legit
    if input != "O" and input != "X":
        print("Invalid input, input must be O or X")
        return 0
    else:
        return 1
    
def max_(v1,v2):
    if v1>v2:
        return v1
    else:
        return v2

def check_symbol(value_matrix,matrix,symbol,x,y):
    #check left
    if y-1>=0:
        if matrix[x][y-1]==symbol:
            value_matrix[x][y] = max_(value_matrix[x][y],value_matrix[x][y-1]+1)
        #check top left
        if x-1>=0:
            if matrix[x-1][y-1]==symbol:
                value_matrix[x][y] = max_(value_matrix[x][y],value_matrix[x-1][y-1]+1)
    #check top
    if x-1>=0:
        if matrix[x-1][y]==symbol:
            value_matrix[x][y] = max_(value_matrix[x][y],value_matrix[x-1][y]+1)
    #check right
    if y+1<=2:
        if matrix[x][y+1]==symbol:
            value_matrix[x][y] = max_(value_matrix[x][y],value_matrix[x][y+1]+1)
        #check top left
        if x-1>=0:
            if matrix[x-1][y+1]==symbol:
                value_matrix[x][y] = max_(value_matrix[x][y],value_matrix[x-1][y+1]+1)
    value_matrix[x][y] = max_(value_matrix[x][y],1)
    if value_matrix[x][y]>max_(x+1,y+1):
        value_matrix = max_(x+1,y+1)
    return value_matrix

def range_(x,y,sum):
    xn=x+sum
    yn=y+sum
    yl=y-sum
    if (x+sum<0 or x+sum>2):
        xn = -1
    if (y+sum<0 or y+sum>2):
        yn = -1
    if(y-sum<0 or y-sum>2):
        yl=-1
    return[xn,yn,yl]
        
    
def check_winners(matrix,x,y,symbol):
    cT  = 0
    cS = 0
    cDR = 0
    cDL = 0
    win = 0    
    for i in range(-2,3):
        v = range_(x,y,i)
        xn=v[0]
        yn=v[1]
        yl=v[2]
        #Side Check
        if(yn!=-1 and matrix[x][yn]==symbol):
                cS= cS+1

        #Top Check
        if(xn!=-1 and matrix[xn][y]==symbol):
                cT=cT+1
        #Diagonal Left Check
        if(yn!=-1 and xn!=-1 and matrix[xn][yn]==symbol):
                cDL = cDL+1

        #Side Check
        if(yl!=-1 and xn!=-1 and matrix[xn][yl]==symbol):
                cDR = cDR+1
    if(cT ==3):
        # matrix[0][y] = "["+matrix[0][y]+"]"
        # matrix[1][y] = "["+matrix[1][y]+"]"
        # matrix[2][y] = "["+matrix[2][y]+"]"
        win =1
    if(cS ==3):
        # matrix[x][0] = "["+matrix[x][0]+"]"
        # matrix[x][1] = "["+matrix[x][1]+"]"
        # matrix[x][2] = "["+matrix[x][2]+"]"
        win=1
    if(cDR ==3):
        # matrix[0][0] = "["+matrix[0][0]+"]"
        # matrix[1][1] = "["+matrix[1][1]+"]"
        # matrix[2][2] = "["+matrix[2][2]+"]"
        win =1
    if(cDL ==3):
        # matrix[0][2] = "["+matrix[0][2]+"]"
        # matrix[1][1] = "["+matrix[1][1]+"]"
        # matrix[2][0] = "["+matrix[2][0]+"]"
        win = 1
        
    return [win,matrix]
        
    #
        
    
    
    # value_matrix = [[0,0,0],[0,0,0],[0,0,0]]
    # # cycles through x values
    # for x in range(len(matrix)):
    #     #cycles through y values
    #     for y in range(len(matrix[x])):
    #         if matrix[x][y]=="X":
    #             value_matrix = check_symbol(value_matrix,matrix,"X",x,y)
    #         elif matrix[x][y] =="O":
    #             value_matrix = check_symbol(value_matrix,matrix,"O",x,y)
    # print(value_matrix)
    
                
            
    
#Add Change
#   y0,y1,y2
#x0[- ,- ,-]
#x1[- ,- ,-]
#x2[- ,- ,-]

# moves will be the number of moves max is 9 moves due to 3X3 grid.
def game():
    # Initiate Values
    moves=0
    win =0
    # Requests Players Choice of Starting Symbol
    k=input('Player 1 please Choose X or O: ')
    while(not check_choice(k)):
        k=input('Player 1 please Choose X or O: ')
    #Chooses sympols for player
    player1 = k
    if (player1=="O"):
        player2 ="X"
    else:
        player2 ="O"
    player = str(1)
    # Inititates an empty array    
    arr = [["-","-","-"],["-","-","-"],["-","-","-"]]
    display(arr)
    while(moves < 9):
        if k == player1:
            player = str(1)
        else:
            player = str(2)
        print("Player "+player+" it is now your turn\n")
        y = int(input("Please input the X Value of your attack: "))
        x = int(input("Please input the Y Value of your attack: "))
        
        # Abdullahi - Check if Input is Valid (Need to check if there is not already a value there or if input is not within a matrix) 
        
        arr[x][y] = k
        display(arr)
        
        #round ends
        moves=moves+1
        # check for Winners
        if (moves>4):
            v = check_winners(arr,x,y,k)
            win=v[0]
            arr=v[1]
            if win==1:
                display(arr)
                moves = 10
                continue
        # Changes from one Player to the other
        if k=='O':
            k="X"
        else:
            k="O"
    
    if win==1:
        print("WINNER!!! Player "+player+" has won\n")
    else:
        print("It's a Draw")
    #Check if Players want to play again
    play_again = input("Want to Play Again Y/N: ")
    while(play_again!="Y" and play_again!="N"):
        print("Invalid Input")
        play_again = input("Want to Play Again Y/N: ")

    return play_again    
    
if __name__ == '__main__':
    # Initiate game
    play_again = game()
    while play_again=="Y":
        play_again = game()
    
     
## Win Condition (A)-Sorry I completed this one when I did the double win

##Draw Conditions ( Draw Conditions Completed)

#Modes 2 Players or 1 Player (A)

#Double Win (Complete -Win Conditions Completed)

#Listener to not place item in already filled slot Ex. If X exists O cannot be placed (A)

# Listener to swap players (Complete)