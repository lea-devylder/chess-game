##################### TERM PROJECT: CHESS GAME ################################

from cmu_112_graphics import *
from chessAI import *


###############################################################################
# CLASSES
###############################################################################

#each class takes input of name and color
#self.moves is a list of tuples with directions
#getMoves function for all pieces, returns legal moves of that piece based on position

# PIECES CLASSES
class Pawn(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.moves = []
        self.captures = []

    def __repr__(self):
        return self.name

    def getName(self):
        return self.name
    
    def getColor(self):
        return self.color

    def getMoves(self, board, row, col):
        legalMoves = []
        if (self.color == 'white'):
            if (row == 6):
                self.moves = [(-1,0), (-2, 0)]
            else:
                self.moves = [(-1,0)]
            self.captures = [(-1,-1), (-1,1)]
        else:
            if (row == 1):
                self.moves = [(1,0), (2,0)]
            else:
                self.moves = [(1,0)]
            self.captures = [(1,1), (1,-1)]
        for x, y in self.moves:
            if (board[row + x][col + y] == 0):
                legalMoves.append((row + x, col + y))
        for x, y in self.captures:
            if (0 <= row + x < 8 and 0 <= col + y < 8):
                if (board[row+x][col+y] != 0 and board[row+x][col+y].getColor() != self.color):
                    legalMoves.append((row + x, col + y))
        return legalMoves

class Knight(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.moves = [(1,2),(2,1),(-1,-2),(-2,-1),(-1,2),(2,-1),(1,-2),(-2,1)]

    def __repr__(self):
        return self.name
    
    def getName(self):
        return self.name
    
    def getColor(self):
        return self.color

    def getMoves(self, board, row, col):
        legalMoves = []
        for x, y in self.moves:
            if (0 <= row + x < 8 and 0 <= col + y < 8):
                if (board[row + x][col + y] == 0):
                    legalMoves.append((row + x, col + y))
                elif (board[row + x][col + y] != self.color):
                    legalMoves.append((row + x, col + y))
        return legalMoves

class Bishop(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def __repr__(self):
        return self.name
    
    def getName(self):
        return self.name
    
    def getColor(self):
        return self.color

    def getMoves(self, board, row, col):
        legalMoves = []
        directions = [(1,1),(1,-1), (-1,1),(-1,-1)]
        
        for dRow, dCol in directions:
            newRow = row + dRow
            newCol = col + dCol
            openSquares = True
            while openSquares:
                if (0 <= newRow < 8 and 0 <= newCol < 8):
                    if (board[newRow][newCol] == 0):
                        legalMoves.append((newRow, newCol))
                        newRow += dRow
                        newCol += dCol
                    elif (board[newRow][newCol].getColor() != self.color):
                        legalMoves.append((newRow, newCol))
                        openSquares = False
                    else:
                        openSquares = False
                else:
                    openSquares = False 
        return legalMoves     

class Rook(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def __repr__(self):
        return self.name
    
    def getName(self):
        return self.name
    
    def getColor(self):
        return self.color
    
    def getMoves(self, board, row, col):
        legalMoves = []
        directions = [(1,0),(-1,0), (0,1),(0,-1)]

        for dRow, dCol in directions:
            newRow = row + dRow
            newCol = col + dCol
            openSquares = True
            while (openSquares == True):
                if (0 <= newRow < 8 and 0 <= newCol < 8):
                    if (board[newRow][newCol] == 0):
                        legalMoves.append((newRow, newCol))
                        newRow += dRow
                        newCol += dCol
                    elif (board[newRow][newCol].getColor() != self.color):
                        legalMoves.append((newRow, newCol))
                        openSquares = False
                    else:
                        openSquares = False
                else:
                    openSquares = False
        return legalMoves     
        

class Queen(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def __repr__(self):
        return self.name
    
    def getName(self):
        return self.name
    
    def getColor(self):
        return self.color
    
    def getMoves(self, board, row, col):
        legalMoves = []
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

        for dRow, dCol in directions:
            newRow = row + dRow
            newCol = col + dCol
            openSquares = True
            while (openSquares == True):
                if (0 <= newRow < 8 and 0 <= newCol < 8):
                    if (board[newRow][newCol] == 0):
                        legalMoves.append((newRow, newCol))
                        newRow += dRow
                        newCol += dCol
                    elif (board[newRow][newCol].getColor() != self.color):
                        legalMoves.append((newRow, newCol))
                        openSquares = False
                    else:
                        openSquares = False
                else:
                    openSquares = False
        return legalMoves     

class King(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.moves = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

    def __repr__(self):
        return self.name
    
    def getColor(self):
        return self.color
    
    def getName(self):
        return self.name
    
    def getMoves(self, board, row, col):
        legalMoves = []
        for x, y in self.moves:
            if (0 <= row + x < 8 and 0 <= col + y < 8):
                if (board[row + x][col + y] == 0):
                    legalMoves.append((row + x, col + y))
                elif (board[row + x][col + y].getColor() != self.color):
                    legalMoves.append((row + x, col + y))
        return legalMoves

# BOARD CLASS
class Board(object):
    def __init__(self):
        self.rows = 8
        self.cols = 8
        self.squares = [[0]*self.cols for i in range(self.rows)]
        self.pastMoves = []
        self.pastPieces = []
    
    def startBoard(self, app):
        #add black pieces to top of the board
        col = 0
        for i in range(len(app.blackPieces)):
            if (i < 8):
                self.squares[0][i] = app.blackPieces[i]
            else:
                self.squares[1][col] = app.blackPieces[i]
                col += 1
        #add white pieces to bottom of the board
        col = 0
        for i in range(len(app.whitePieces)):
            if (i < 8):
                self.squares[7][i] = app.whitePieces[i]
            else:
                self.squares[6][col] = app.whitePieces[i]
                col += 1
        return self.squares
    
    def getRowsAndCols(self):
        return self.rows, self.cols

    #called in the AI function, makes move and evaluates
    def makeMove(self, move1, move2):
        x1, y1 = move1
        x2, y2 = move2
        self.pastPieces.append(self.squares[x2][y2])
        self.squares[x2][y2] = self.squares[x1][y1]
        self.squares[x1][y1] = 0
        self.pastMoves.append(move1)
        self.pastMoves.append(move2)

    #also called in AI function after recursive call, undoes move
    def undoMove(self):
        x2, y2 = self.pastMoves.pop()
        x1, y1 = self.pastMoves.pop()
        self.squares[x1][y1] = self.squares[x2][y2]
        self.squares[x2][y2] = self.pastPieces.pop()
    
    #returns legal moves of all the pieces of specified color
    def allMoves(self, color):
        allMoves = []
        pieceMoves = []
        for row in range(8):
            for col in range(8):
                if (self.squares[row][col] != 0):
                    if (self.squares[row][col].getColor() == color):
                        if (len(self.squares[row][col].getMoves(self.squares, row, col)) != 0):
                            for x, y in self.squares[row][col].getMoves(self.squares, row, col):
                                if (self.squares[x][y] == 0 or self.squares[x][y].getColor() != color):
                                    pieceMoves.append((row, col))
                                    pieceMoves.append((x, y))
                                    allMoves.append(pieceMoves)
                                    pieceMoves = []
        return allMoves
    
    #evaluation function for AI, returns score of current board
    def getBoardScore(self):
        score = 0
        for row in range(len(self.squares)):
            for col in range(len(self.squares[0])):
                if (self.squares[row][col] != 0):
                    if (isinstance(self.squares[row][col], Pawn)):
                        if (self.squares[row][col].getColor() == 'white'):
                            score += 1
                        else: 
                            score -= 1
                    if (isinstance(self.squares[row][col], Knight)):
                        if (self.squares[row][col].getColor() == 'white'):
                            score += 3
                        else: 
                            score -= 3
                    if (isinstance(self.squares[row][col], Bishop)):
                        if (self.squares[row][col].getColor() == 'white'):
                            score += 3
                        else: 
                            score -= 3
                    if (isinstance(self.squares[row][col], Rook)):
                        if (self.squares[row][col].getColor() == 'white'):
                            score += 5
                        else: 
                            score -= 5
                    if (isinstance(self.squares[row][col], Queen)):
                        if (self.squares[row][col].getColor() == 'white'):
                            score += 9
                        else: 
                            score -= 9
                    if (isinstance(self.squares[row][col], King)):
                        if (self.squares[row][col].getColor() == 'white'):
                            score += 100
                        else: 
                            score -= 100
        return score

################################################################################       
# MAIN APP
################################################################################ 

def appStarted(app):
    app.margin = 50
    app.board = Board()
    app.rows, app.cols = app.board.getRowsAndCols()

    #code for images from https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html
    app.br = app.loadImage('bRook.png')
    app.bn = app.loadImage('bKnight.png')
    app.bb = app.loadImage('bBishop.png')
    app.bq = app.loadImage('bQueen.png')
    app.bk = app.loadImage('bKing.png')
    app.bp = app.loadImage('bPawn.png')

    app.wr = app.loadImage('wRook.png')
    app.wn = app.loadImage('wKnight.png')
    app.wb = app.loadImage('wBishop.png')
    app.wq = app.loadImage('wQueen.png')
    app.wk = app.loadImage('wKing.png')
    app.wp = app.loadImage('wPawn.png')

    app.blackPieces = []
    app.whitePieces = []
    #black pieces, first half of back row
    app.blackPieces.extend([Rook('br1','black'),Knight('bn1','black'),Bishop('bb1','black'),Queen('bq','black')])
    #black pieces, second half of back row
    app.blackPieces.extend([King('bk','black'),Bishop('bb2','black'),Knight('bn2','black'),Rook('br2','black')])
    #white pieces, first half of back row
    app.whitePieces.extend([Rook('wr1','white'),Knight('wn1','white'),Bishop('wb1','white'),Queen('wq','white')])
    #white pieces, second half of back row
    app.whitePieces.extend([King('wk','white'),Bishop('wb2','white'),Knight('wn2','white'),Rook('wr2','white')])
    #black pawns
    app.blackPieces.extend([Pawn('bp1','black'),Pawn('bp2','black'),Pawn('bp3','black'),Pawn('bp4','black')])
    app.blackPieces.extend([Pawn('bp5','black'),Pawn('bp6','black'),Pawn('bp7','black'),Pawn('bp8','black')])
    #white pawns
    app.whitePieces.extend([Pawn('wp1','white'),Pawn('wp2','white'),Pawn('wp3','white'),Pawn('wp4','white')])
    app.whitePieces.extend([Pawn('wp5','white'),Pawn('wp6','white'),Pawn('wp7','white'),Pawn('wp8','white')])

    app.boardObject = Board()
    app.board = app.boardObject.startBoard(app)

    app.clickedSquareRow = None
    app.clickedSquareCol = None
    app.moveToSquareRow = None
    app.moveToSquareCol = None
    app.firstSquareClicked = False

    app.legalMoves = []
    app.turn = 0

    #check for castling
    app.castleBKingSide = True
    app.castleBQueenSide = True
    app.castleWKingSide = True
    app.castleWQueenSide = True

    #check for check
    app.blackInCheck = False
    app.whiteInCheck = False
    app.checkPath = []

    app.gameMode = 'home'
    app.gameOver = False
  
#function from https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
def getCellBounds(app, row, col):
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    x0 = app.margin + col * cellWidth
    x1 = app.margin + (col+1) * cellWidth
    y0 = app.margin + row * cellHeight
    y1 = app.margin + (row+1) * cellHeight
    return (x0, y0, x1, y1)

#function from https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
def getCell(app, x, y):
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth  = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    row = int((y - app.margin) / cellHeight)
    col = int((x - app.margin) / cellWidth)
    return (row, col)

def movePiece(app, x, y):
    #finds where user clicked
    row, col = getCell(app, x, y)
    #checks if user clicked piece to move
    if (app.firstSquareClicked == False):
        app.clickedSquareRow = row
        app.clickedSquareCol = col
        #if user clicked empty square, return None
        if (app.board[row][col] == 0):
            return None
        #if user did not click empty square
        else:
            #check if white's turn and if the clicked piece is white
            if (app.turn % 2 == 0 and app.board[row][col].getColor() == 'white'):
                app.legalMoves = app.board[row][col].getMoves(app.board, row, col)
                app.firstSquareClicked = True
            #check if black's turn and if the clicked piece is black
            elif (app.turn % 2 != 0 and app.board[row][col].getColor() == 'black'):
                app.legalMoves = app.board[row][col].getMoves(app.board, row, col)
                app.firstSquareClicked = True
            #if king is in check and if there is a path to king
            if (app.checkPath != [] and app.whiteInCheck or app.blackInCheck):
                app.legalMoves = []
                moves = app.board[row][col].getMoves(app.board, row, col)
                #update legal moves of pieces
                for i in range(len(moves)):
                    if (isinstance(app.board[row][col], King)):
                        if (moves[i] not in app.checkPath):
                            app.legalMoves.append(moves[i])
                    elif (moves[i] in app.checkPath):
                        app.legalMoves.append(moves[i])
            updateCastleMoves(app)
        #check if there are no legal moves
        if (len(app.legalMoves) == 0):
            app.firstSquareClicked = False
    #if piece is clicked
    else: 
        #set user's second click as row and col of placement of the piece
        if (row, col) in app.legalMoves:
            app.moveToSquareRow = row
            app.moveToSquareCol = col
        else:
            #check if placement is a capture
            if (app.board[row][col] != 0):
                app.clickedSquareRow = row
                app.clickedSquareCol = col
                app.legalMoves = app.board[row][col].getMoves(app.board, row, col)
            #check path to king again
            if (app.checkPath != []):
                app.legalMoves = []
                moves = app.board[row][col].getMoves(app.board, row, col)
                for i in range(len(moves)):
                    if (moves[i] in app.checkPath):
                        app.legalMoves.append(moves[i])
    #if two squares are clicked, move the piece to the second clicked square
    if (app.clickedSquareRow != None and app.moveToSquareRow != None):
        checkCastling(app)
        app.board[app.moveToSquareRow][app.moveToSquareCol] = app.board[app.clickedSquareRow][app.clickedSquareCol]
        checkCheck(app)
        app.board[app.clickedSquareRow][app.clickedSquareCol] = 0
        app.clickedCell = 0
        app.clickedSquareRow = None
        app.clickedSquareCol = None
        app.moveToSquareRow = None
        app.moveToSquareCol = None
        app.firstSquareClicked = False
        app.turn += 1
        if (app.gameMode == 'one-player'):
            AImove(app)
            app.turn += 1

def AImove(app):
    piece, bestMove = minimax(app.boardObject, 3, -10000, 10000, False)[0]
    app.boardObject.makeMove(piece, bestMove)

def updateCastleMoves(app):
    #update king's legal moves to allow for castling
    if (app.board[app.clickedSquareRow][app.clickedSquareCol].getName() == 'wk'):
        if (app.castleWQueenSide):
            app.legalMoves.append((7,6))
        if (app.castleWKingSide):
            app.legalMoves.append((7,2))
    elif (app.board[app.clickedSquareRow][app.clickedSquareCol].getName() == 'bk'):
        if (app.castleBQueenSide):
            app.legalMoves.append((0,6))
        if (app.castleBKingSide):
            app.legalMoves.append((0,2))

def checkCastling(app):
    if (app.board[app.clickedSquareRow][app.clickedSquareCol] != 0):
        #check if rook moved, then set castle boolean to false
        if (app.board[app.clickedSquareRow][app.clickedSquareCol].getName() == 'wr1'):
            app.castleWQueenSide = False
        if (app.board[app.clickedSquareRow][app.clickedSquareCol].getName() == 'wr2'):
            app.castleWKingSide = False
        if (app.board[app.clickedSquareRow][app.clickedSquareCol].getName() == 'br1'):
            app.castleBQueenSide = False
        if (app.board[app.clickedSquareRow][app.clickedSquareCol].getName() == 'br2'):
            app.castleBKingSide = False
        #if castle booelan is true, castle
        if (app.board[app.clickedSquareRow][app.clickedSquareCol].getName() == 'wk'):
            if (app.castleWKingSide):
                if (app.moveToSquareCol == 6):
                    app.board[7][5] = app.board[7][7]
                    app.board[7][7] = 0
            if (app.castleWQueenSide):
                if (app.moveToSquareCol == 2):
                    app.board[7][3] = app.board[7][0]
                    app.board[7][0] = 0
            app.castleWQueenSide = False
            app.castleWKingSide = False
        if (app.board[app.clickedSquareRow][app.clickedSquareCol].getName() == 'bk'):
            if (app.castleBKingSide):
                if (app.moveToSquareCol == 6):
                    app.board[0][5] = app.board[0][7]
                    app.board[0][7] = 0
            if (app.castleBQueenSide):
                if (app.moveToSquareCol == 2):
                    app.board[0][3] = app.board[0][0]
                    app.board[0][0] = 0
            app.castleBQueenSide = False
            app.castleBKingSide = False

def checkCheck(app):
    row = app.moveToSquareRow
    col = app.moveToSquareCol
    legalMoves = app.board[row][col].getMoves(app.board, row, col)
    #check if the king's position is in a piece's legal moves
    for x,y in legalMoves:
        if (app.board[x][y] != 0):
            if (app.board[row][col].getColor() == 'black' and app.board[x][y].getName() == 'wk'):
                app.whiteInCheck = True
                findPath(app, x, y, row, col)
            elif (app.board[row][col].getColor() == 'white' and app.board[x][y].getName() == 'bk'):
                app.blackInCheck = True
                findPath(app, x, y, row, col)   
            else:
                app.whiteInCheck = False
                app.blackInCheck = False

def findPath(app, x, y, row, col):
    if (isinstance(app.board[row][col], Knight) 
        or isinstance(app.board[row][col], Pawn)):
        app.checkPath.append((row, col))
    else: 
        #check if the king is in piece's path
        if (isinstance(app.board[row][col], Rook)):
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
        if (isinstance(app.board[row][col], Bishop)):
            directions = [(1,1),(1,-1),(-1,1),(-1,-1)]
        if (isinstance(app.board[row][col], Queen)):
            directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

        foundPath = False
        for drow, dcol in directions:
            newRow = drow + row
            newCol = dcol + col
            path = False
            if (foundPath): break
            while (path == False):
                if (0 <= newRow < 8 and 0 <= newCol < 8):
                    if (app.board[newRow][newCol] == 0):
                        app.checkPath.append((newRow, newCol))
                        newRow += drow 
                        newCol += dcol
                    elif (newRow == x and newCol == y):
                        foundPath = True
                        break
                    else:
                        app.checkPath = []
                        path = True
                else:
                    app.checkPath = []
                    path = True

def switchScreen(app, x, y):
    if (app.gameMode == 'home' and 
    app.width*5//16 < x < app.width*11//16 
    and app.height*11//16 < y < app.height*13//16):
        app.gameMode = 'modes'
    elif (app.gameMode == 'modes'):
        if (app.width*2//6 < x < app.width*4//6 and app.height*3//8 < y < app.height*4//8):
            app.gameMode = 'one-player'
        elif (app.width*2//6 < x < app.width*4//6 and app.height*10//16 < y < app.height*13//16):
            app.gameMode = 'two-player' 
    else:
        pass
                
def keyPressed(app, event):
    #restart game
    if (event.key == 'r'):
        appStarted(app)

def mousePressed(app, event):
    #get x and y coordinates
    x, y = event.x, event.y
    if (app.gameMode == 'home' or app.gameMode == 'modes'):
        switchScreen(app, x, y)
    else:
        movePiece(app, x, y)

################################################################################
# DRAW FUNCTIONS
################################################################################

def redrawAll(app, canvas):
    if (app.gameMode == 'home'):
        drawHome(app, canvas)
    elif (app.gameMode == 'modes'):
        drawModes(app, canvas)
    elif (app.gameMode == 'two-player' or app.gameMode == 'one-player'):
        drawBackground(app, canvas)
        drawBoard(app, canvas)
        drawMoves(app, canvas)
        drawPieces(app, canvas)
        drawCheck(app, canvas)

#function from https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
def getCellBounds2(app, row, col):
    margin = 0
    gridWidth  = app.width - 2*margin
    gridHeight = app.height - 2*margin
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    x0 = margin + col * cellWidth
    x1 = margin + (col+1) * cellWidth
    y0 = margin + row * cellHeight
    y1 = margin + (row+1) * cellHeight
    return (x0, y0, x1, y1)

def drawHome(app, canvas):
    rows = 10
    cols = 10
    nextColor = None
    for row in range(rows):
        for col in range(cols):
            if (nextColor):
                color = 'dark slate gray'
                nextColor = False
            else: 
                color = 'sea green'
                nextColor = True
            x0, y0, x1, y1 = getCellBounds2(app, row, col)
            canvas.create_rectangle(x0, y0, x1, y1, fill = color, width = 0)
        if (nextColor): nextColor = False
        else: nextColor = True
    canvas.create_rectangle(app.width//4, app.height*3//8, app.width*3//4, 
        app.height*5//8, fill = 'dark slate gray', outline = 'AntiqueWhite1', width = 5)
    canvas.create_text(app.width//2, app.height//2, text = "CHESS.py", fill = 'AntiqueWhite1',
                        font = 'Times 40 bold')
    canvas.create_rectangle(app.width*5//16, app.height*11//16, 
       app.width*11//16, app.height*13//16, fill = 'sea green', 
       outline = 'AntiqueWhite1', width = 4, activefill = 'LightGoldenRod3')
    canvas.create_text(app.width*8//16, app.height*12//16, 
        text = "Play!", fill = 'AntiqueWhite1', font = 'Arial 20 bold')

def drawModes(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'dark slate gray')
    canvas.create_rectangle(20, 20, app.width-20, app.height-20, fill = 'dark slate gray',
        outline = 'sea green', width = 5)
    canvas.create_text(app.width//2, app.height//6, text = 'Pick a mode:',
        font = 'Times 40 bold', fill = 'AntiqueWhite1')
    canvas.create_rectangle(app.width*2//6, app.height*3//8, app.width*4//6, 
        app.height*4//8, fill = 'AntiqueWhite1', outline = 'sea green', 
        width = 4, activefill = 'LightGoldenRod3')
    canvas.create_text(app.width//2, app.height*7//16, text = '1 - Player', 
        fill = 'dark slate gray', font = 'Arial 15 bold')
    canvas.create_rectangle(app.width*2//6, app.height*10//16, app.width*4//6, 
        app.height*12//16, fill = 'AntiqueWhite1', outline = 'sea green', 
        width = 4, activefill = 'LightGoldenRod3')
    canvas.create_text(app.width//2, app.height*11//16, text = '2 - Player', 
        fill = 'dark slate gray', font = 'Arial 15 bold')

def drawMoves(app, canvas):
    if (app.firstSquareClicked):
        for x, y in app.legalMoves:
            x0, y0, x1, y1 = getCellBounds(app, x, y)
            r, cx, cy = (x1-x0)//6, (x1+x0)//2, (y1+y0)//2
            if (app.board[x][y] == 0):
                canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = 'dark slate gray', width = 0)

def drawCheck(app, canvas):
    if (app.whiteInCheck):
        canvas.create_text(app.width//2, app.height - (app.margin//2), 
        text = "White in check.", fill = 'white', font = 'Arial 15 bold')
    elif (app.blackInCheck):
        canvas.create_text(app.width//2, app.height - (app.margin//2), 
        text = "Black in check.", fill = 'white', font = 'Arial 15 bold')

def drawBackground(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'dark slate gray')

def drawBoard(app, canvas):
    #create outline of the board
    canvas.create_rectangle(app.margin, app.margin, 
    app.width-app.margin, app.height-app.margin, width = 0)
    #draw board and alternate between two colors, except when starting new row
    nextColor = False
    for row in range(len(app.board)):
        for col in range(len(app.board[0])):
            if (row == app.clickedSquareRow and col == app.clickedSquareCol):
                color = 'khaki'
                if (nextColor): nextColor = False
                else: nextColor = True
            elif (nextColor):
                color = 'PaleGreen4'
                nextColor = False
            else: 
                color = 'cornsilk2'
                nextColor = True
            x0, y0, x1, y1 = getCellBounds(app, row, col)
            canvas.create_rectangle(x0, y0, x1, y1, fill = color, width = 0)
        #keep same color when starting new row
        if (nextColor): nextColor = False
        else: nextColor = True

#images from https://commons.wikimedia.org/wiki/Category:PNG_chess_pieces/Standard_transparent
def drawPieces(app, canvas):
    for row in range(len(app.board)):
        for col in range(len(app.board[0])):
            x0, y0, x1, y1 = getCellBounds(app, row, col)
            if (isinstance(app.board[row][col], Pawn)):
                if (app.board[row][col].getColor() == 'white'):
                    canvas.create_image((x1+x0)//2, (y1+y0)//2, image=ImageTk.PhotoImage(app.wp))
                else: 
                    canvas.create_image((x1+x0)//2, (y1+y0)//2, image=ImageTk.PhotoImage(app.bp))
            if (isinstance(app.board[row][col], Knight)):
                if (app.board[row][col].getColor() == 'white'):
                    canvas.create_image((x1+x0)//2, (y1+y0)//2, image=ImageTk.PhotoImage(app.wn))
                else: 
                    canvas.create_image((x1+x0)//2, (y1+y0)//2, image=ImageTk.PhotoImage(app.bn))
            if (isinstance(app.board[row][col], Bishop)):
                if (app.board[row][col].getColor() == 'white'):
                    canvas.create_image((x1+x0)//2, (y1+y0)//2, image=ImageTk.PhotoImage(app.wb))
                else: 
                    canvas.create_image((x1+x0)//2, (y1+y0)//2, image=ImageTk.PhotoImage(app.bb))
            if (isinstance(app.board[row][col], Rook)):
                if (app.board[row][col].getColor() == 'white'):
                    canvas.create_image((x1+x0)//2, (y1+y0)//2, image=ImageTk.PhotoImage(app.wr))
                else: 
                    canvas.create_image((x1+x0)//2, (y1+y0)//2, image=ImageTk.PhotoImage(app.br))
            if (isinstance(app.board[row][col], Queen)):
                if (app.board[row][col].getColor() == 'white'):
                    canvas.create_image((x1+x0)//2, (y1+y0)//2, image=ImageTk.PhotoImage(app.wq))
                else: 
                    canvas.create_image((x1+x0)//2, (y1+y0)//2, image=ImageTk.PhotoImage(app.bq))
            if (isinstance(app.board[row][col], King)):
                if (app.board[row][col].getColor() == 'white'):
                    canvas.create_image((x1+x0)//2, (y1+y0)//2, image=ImageTk.PhotoImage(app.wk))
                else: 
                    canvas.create_image((x1+x0)//2, (y1+y0)//2, image=ImageTk.PhotoImage(app.bk))

runApp(width=600, height=600)
