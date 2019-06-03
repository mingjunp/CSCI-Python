#<Mingjun Pan, 5256622>

# I understand this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing
# any aspect of the examination with anyone will result in failing the course.
# I further certify that this program represents my own work none it was
# obtained from any source other than material presented as part of the
# course.

import turtle
import math
import random

# choose the start point and gap between each cell
# these are constants
startX = -350
startY = 320
gap = 95

# draw the board
def draw_board():
    # turtle.screensize(2000, 1500)
    # set the turtle speed and penup
    turtle.speed(0)
    turtle.penup()


    turtle.goto(startX, startY)
    turtle.hideturtle()

    # write line and row number
    for i in range (0,8):
        turtle.goto(startX + i * gap, startY + 50)
        turtle.write(i)

    for i in range(0,8):
        turtle.goto(startX - 60,startY- i * gap)
        turtle.write(i)

    # change turtle shape to square
    turtle.shape("square")
    # change color and size
    turtle.color("green")
    turtle.shapesize(4, 4, 12)
    turtle.goto(startX,startY)

    # draw the board
    for j in range(0,8):
        turtle.goto(startX, startY - j * gap)
        for i in range(0,8):
            turtle.stamp()
            turtle.forward(gap)

# if the row, col is in grid
def inGrid(row,col):
    if row >=0 and row<=7 and col>=0 and col<=7:
        return True
    else:
        return False

# return the neighbours of the row, col
def neighbours(row,col):
    # not in the corner and border
    if row>0 and row<7  and col>0 and col<7:
        # print(row,col)
        neighbour = [[row-1,col-1],[row-1,col],[row-1,col+1],
                     [row,col-1],[row,col+1],
                     [row+1,col-1],[row+1,col],[row+1,col+1]]
        # print(neighbour)
        return neighbour
    else:
        # four corners
        if row==0 and col==0:
            neighbour = [[row,col+1],[row+1,col],[row+1,col+1]]
            return neighbour
        if row==0 and col==7:
            neighbour = [[row, col - 1], [row + 1, col], [row + 1, col - 1]]
            return neighbour
        if row==7 and col==0:
            neighbour = [[row, col + 1], [row - 1, col], [row - 1, col + 1]]
            return neighbour
        if row==7 and col==7:
            neighbour = [[row, col - 1], [row - 1, col], [row - 1, col - 1]]
            return neighbour
        # four borders
        if row == 0 or row ==7:
            if row == 0 and col>0 and col<7:
                neighbour = [[row,col-1],[row,col+1],[row+1,col-1],[row+1,col],[row+1,col+1]]
                return neighbour
            if row ==7 and col>0 and col<7:
                neighbour = [[row,col-1],[row,col+1],[row-1,col-1],[row-1,col],[row-1,col+1]]
                return  neighbour
        if col==0 or col==7:
            if col ==0 and row>0 and row<7:
                neighbour = [[row - 1, col], [row + 1, col], [row - 1, col + 1], [row, col + 1], [row - 1, col + 1]]
                return neighbour
            if col==7 and row>0 and row<7:
                neighbour = [[row - 1, col], [row + 1, col], [row - 1, col - 1], [row, col - 1], [row - 1, col - 1]]
                return neighbour

# convert the row and col to turtle coordinates
def helper(row,col):
    x = startX + col * gap
    y = startY - row * gap
    # turtle.showturtle()
    # turtle.color("red")
    # turtle.goto(x,y)
    return [x,y]

def hasOppnentToken(board,neighbour,color):
    # print(neighbour)
    hasOppnent = False
    for i in neighbour:
        if board[i[0]][i[1]] != color and board[i[0]][i[1]]!=0:
            hasOppnent = hasOppnent or True
        else:
            hasOppnent = hasOppnent or False
    return hasOppnent

# check if it is a valid move
def isValidMove(board,row,col,color):
    if board[row][col]==0:
        if hasOppnentToken(board,neighbours(row, col),color):
            # print("neighbour")
            valid = False
            token = findAllToken(board,row,col,color)
            # print(token)
            for i in token:
                if i > 0:
                    valid = valid or True
                else:
                    valid = valid or False
            if valid == True:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def findAllToken(board,row,col,color):
    # the order in result is right left top down
    # topRight bottomRight topLeft bottomLeft
    result = []
    result.append(findTokenRight(board,row,col,color))
    result.append(findTokenLeft(board, row, col, color))
    result.append(findTokenUp(board, row, col, color))
    result.append(findTokenDown(board, row, col, color))
    result.append(findTokenTopRight(board, row, col, color))
    result.append(findTokenBottomRight(board, row, col, color))
    result.append(findTokenTopLeft(board, row, col, color))
    result.append(findTokenBottomLeft(board, row, col, color))

    return result

def findTokenRight(board,row,col,color):
    if inGrid(row,col+1):
        if board[row][col+1]!=color and board[row][col+1]!=0:
            return 1 + findTokenRight(board, row, col + 1, color)
        elif board[row][col+1] == color:
            return 0
        elif board[row][col+1] == 0:
            return -8
    else:
        return -8

def findTokenLeft(board,row,col,color):
    if inGrid(row,col-1):
        if board[row][col-1]!=color and board[row][col-1]!=0:
            return 1 + findTokenLeft(board, row, col-1, color)
        elif board[row][col-1] == color:
            return 0
        elif board[row][col-1] == 0:
            return -8
    else:
        return -8

def findTokenUp(board,row,col,color):
    if inGrid(row-1,col):
        if board[row-1][col]!=color and board[row-1][col]!=0:
            return 1+findTokenUp(board, row-1, col, color)
        elif board[row - 1][col] == color:
            return 0
        elif board[row - 1][col] == 0:
            return -8
    else:
        return -8

def findTokenDown(board,row,col,color):
    if inGrid(row+1,col):
        if board[row+1][col]!=color and board[row+1][col]!=0:
            return 1+findTokenDown(board,row+1,col,color)
        elif board[row+1][col]==color:
            return 0
        elif board[row+1][col]==0:
            return -8
    else:
        return -8

def findTokenTopRight(board,row,col,color):
    if inGrid(row - 1, col + 1):
        if board[row - 1][col+1] != color and board[row - 1][col+1] != 0:
            return 1 + findTokenTopRight(board, row - 1, col+1, color)
        elif board[row - 1][col+1] == color:
            return 0
        elif board[row - 1][col+1] == 0:
            return -8
    else:
        return -8

def findTokenBottomRight(board,row,col,color):
    if inGrid(row + 1, col + 1):
        if board[row + 1][col + 1] != color and board[row + 1][col + 1] !=0:
            return 1 + findTokenBottomRight(board, row + 1, col + 1, color)
        elif board[row + 1][col+1] == color:
            return 0
        elif board[row + 1][col+1] == 0:
            return -8
    else:
        return -8

def findTokenTopLeft(board,row,col,color):
    if inGrid(row - 1, col - 1):
        if board[row - 1][col - 1] != color and board[row - 1][col - 1] !=0:
            return 1 + findTokenTopLeft(board, row - 1, col - 1, color)
        elif board[row - 1][col-1] == color:
            return 0
        elif board[row - 1][col-1] == 0:
            return -8
    else:
        return -8

def findTokenBottomLeft(board,row,col,color):
    if inGrid(row + 1, col - 1):
        if board[row + 1][col - 1] != color and board[row + 1][col - 1] !=0:
            return 1 + findTokenBottomLeft(board, row + 1, col - 1, color)
        elif board[row + 1][col-1] == color:
            return 0
        elif board[row + 1][col-1] == 0:
            return -8
    else:
        return -8

# let the computer play
def selectNextPlay(board,color):
    # pick a random position in the valid moves list
    validMoves = []
    validMoves = getValidMoves(board,color)
    if validMoves!=[]:
        temp = random.randint(0,len(validMoves)-1)
        board = placeToken(board,color,validMoves[temp][0],validMoves[temp][1])
        board = flip(board, color, validMoves[temp][0],validMoves[temp][1])
    return board

# get the valid moves list of chosen color
def getValidMoves(board,color):
    allValidMoves = []
    for i in range(0,8):
        for j in range(0,8):
            if isValidMove(board,i,j,color):
                # append tuple into list
                allValidMoves.append((i,j))

    return allValidMoves

# get the winner and show the scores
def winner(board,quit):
    score_white = 0
    score_black = 0
    if quit==False:
        # no valid moves
        if getValidMoves(board,1) == [] or getValidMoves(board,2) == []:
            for i in board:
                for j in i:
                    if j == 1:
                        score_white = score_white + 1
                    elif j == 2:
                        score_black = score_black + 1
            turtle.goto(0, 0)
            turtle.color("red")
            if score_black > score_white:
                turtle.write("black wins. socre:" + str(score_black), font=("Arial", 15, "bold"))
            elif score_black < score_white:
                turtle.write("white wins. socre:" + str(score_white), font=("Arial", 15, "bold"))
            elif score_black == score_white:
                turtle.write("same score. socre:" + str(score_black), font=("Arial", 15, "bold"))
            return True
        else:
            return False
    else:
        for i in board:
            for j in i:
                if j == 1:
                    score_white = score_white + 1
                elif j == 2:
                    score_black = score_black + 1
        turtle.goto(0, 0)
        turtle.color("red")
        if score_black > score_white:
            turtle.write("black wins. socre:" + str(score_black), font=("Arial", 15, "bold"))
        elif score_black < score_white:
            turtle.write("white wins. socre:" + str(score_white), font=("Arial", 15, "bold"))
        elif score_black == score_white:
            turtle.write("same score. socre:" + str(score_black), font=("Arial", 15, "bold"))
        return True

# place a token on the board
def placeToken(board, color, row, col):
    # change turtle shape and color and change the board
    turtle.shape("circle")
    if color == 1:
        turtle.color("white")
        board[row][col] = 1
    elif color == 2:
        turtle.color("black")
        board[row][col] = 2
    coord = helper(row,col)
    turtle.goto(coord[0],coord[1])
    turtle.stamp()

    return board

def flip(board,color,row,col):
    validMoves = []
    validMoves = findAllToken(board,row,col,color)
    # print(validMoves)
    # right
    if validMoves[0]>0:
        r = row
        c = col
        for i in range(0,validMoves[0]):
            c = c+1
            board = placeToken(board,color,r,c)
    # left
    if validMoves[1] > 0:
        r = row
        c = col
        for i in range(0,validMoves[1]):
            c = c - 1
            board = placeToken(board, color, r, c)
    # top
    if validMoves[2] > 0:
        r = row
        c = col
        for i in range(0,validMoves[2]):
            r = r - 1
            board = placeToken(board, color, r, c)
    # down
    if validMoves[3] > 0:
        r = row
        c = col
        for i in range(0, validMoves[3]):
            r = r + 1
            board = placeToken(board, color, r, c)
    # topRight
    if validMoves[4] > 0:
        r = row
        c = col
        for i in range(0, validMoves[4]):
            r = r - 1
            c = c + 1
            board = placeToken(board, color, r, c)
    # bottomRight
    if validMoves[5] > 0:
        r = row
        c = col
        for i in range(0, validMoves[5]):
            r = r + 1
            c = c + 1
            board = placeToken(board, color, r, c)
    # topLeft
    if validMoves[6] > 0:
        r = row
        c = col
        for i in range(0, validMoves[6]):
            r = r - 1
            c = c -1
            board = placeToken(board, color, r, c)
    # bottomLeft
    if validMoves[7] > 0:
        r = row
        c = col
        for i in range(0, validMoves[7]):
            r = r + 1
            c = c - 1
            board = placeToken(board, color, r, c)

    return board

def checkValidInputs(row,col):
    if row>=0 and row <=7 and col>=0 and col<=7:
        return True
    else:
        return False

# start the game
def Othello():
    # a matrix that indicates the board
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]

    # token states
    free = 0
    white = 1
    black = 2

    win = False
    quit = False

    draw_board()
    placeToken(board, white, 3, 3)
    placeToken(board, black, 3, 4)
    placeToken(board, black, 4, 3)
    placeToken(board, white, 4, 4)

    # no one wins and the user do not enter null-string continue the game
    invalidrow = ''
    invalidcol = ''
    while((not win) and (not quit)):
        if invalidrow=='' and invalidcol=='':
            row_col = turtle.textinput("User Input","Please enter row,col in format(2,3):")
        else:
            row_col = turtle.textinput("User Input", str(invalidrow) + ',' + str(invalidcol) + "is not a valid move. reenter row,col" )
            invalidrow = ''
            invalidcol = ''
        # check if user wants to quit
        if row_col == '':
            quit = True
            winner(board, quit)
            turtle.done()
        else:
            # check if there is a winner
            if winner(board,quit):
                win = True
                turtle.done()
            # no winner continue the game
            else:
                row_col = row_col.split(",")
                row = int(row_col[0])
                col = int(row_col[1])
                if checkValidInputs(row,col)==False:
                    invalidrow = row
                    invalidcol = col
                    continue
                # check the chosen row and col is a valid move
                if isValidMove(board,row,col,black) and getValidMoves(board,black)!=[]:
                    # user's turn
                    board = placeToken(board,black,row,col)
                    board = flip(board,black,row,col)
                    # computer's turn
                    board = selectNextPlay(board,white)
                    # check if there is a winner
                    if winner(board, quit):
                        win = True
                        turtle.done()
                #if it is not a valid move
                elif isValidMove(board,row,col,black) == False:
                    invalidrow = row
                    invalidcol = col
                    continue

def main():
    Othello()

if __name__=="__main__":
    main()




