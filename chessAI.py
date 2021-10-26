###################### TERM PROJECT: CHESS AI #################################

from cmu_112_graphics import *
import random, copy

###############################################################################
# MINIMAX FUNCTION
###############################################################################

#some code copied from https://www.youtube.com/watch?v=-ivz8yJ4l4E&t=320s at time 6:46
#alpha-beta pruning pseudocode from https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
def minimax(board, depth, alpha, beta, maxPlayer):
    alpha = -10000
    beta = 10000
    #base case
    if (depth == 0):
        return None, board.getBoardScore()
    if (maxPlayer):
        value = -10000
        alpha = -10000
        moves = board.allMoves('white')
        if (moves == []):
            print('error')
        bestMoves = []
        for row in range(len(moves)):
            #make move
            board.makeMove(moves[row][0], moves[row][1])
            #recursive call
            result = minimax(board, depth - 1, alpha, beta, False)[1]
            alpha = max(alpha, value)
            if (alpha >= beta):
                break
            if (result >= value):
                value = result
                bestMove = moves[row][0], moves[row][1]
                #if (result == value):
                    #bestMoves.append(bestMove)
                #else:
                    #bestMoves = []
                    #bestMoves.append(bestMove)
            #undo move, backtrack
            board.undoMove()
        #random.shuffle(bestMoves)
        #for i in range(len(bestMoves)):
            #bestMove = bestMoves[i]
        return bestMove, value  
    else:
        value = 10000
        moves = board.allMoves('black')
        if (moves == []):
            print('error')
        bestMoves = []
        for row in range(len(moves)):
            #make move
            board.makeMove(moves[row][0], moves[row][1])
            #recursive call
            result = minimax(board, depth - 1, alpha, beta, True)[1]
            beta = min(beta, value)
            if (beta <= alpha):
                break
            if (result <= value):
                value = result
                bestMove = moves[row][0], moves[row][1]
                #if (result == value):
                    #bestMoves.append(bestMove)
                #else:
                    #bestMoves = []
                    #bestMoves.append(bestMove)
            #undo move, backtrack
            board.undoMove()
        #random.shuffle(bestMoves)
        #for i in range(len(bestMoves)):
            #bestMove = bestMoves[i]
        return bestMove, value 