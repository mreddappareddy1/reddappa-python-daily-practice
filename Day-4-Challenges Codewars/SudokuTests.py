import numpy as np
def getSubMatrix(board,matrixNum):
    matrix = []
    for i in range(0,9,3):
        for j in range(0,9,3):
            submatrix = []
            for k in range(i,i+3):
                for l in range(j,j+3):
                    row = board[k]
                    cell = row[l]
                    submatrix.append(cell)
            matrix.append(submatrix)               
    return matrix[matrixNum-1]
def getBoardRow(board,rowNum):
    rows = board[rowNum-1]
    return rows
def getBoardColumn(board,columnNum):
    board_t = np.array(board).T.tolist()
    return(board_t[columnNum-1])

sudokuboard = [[1, 3, 2, 4, 6, 8, 5, 7, 9], 
[4, 9, 8, 3, 7, 5, 2, 6, 1], 
[7, 5, 6, 2, 1, 9, 3, 8, 4], 
[6, 4, 3, 7, 9, 2, 1, 5, 8], 
[5, 2, 1, 8, 4, 6, 7, 9, 3], 
[9, 8, 7, 5, 3, 1, 4, 2, 6], 
[2, 1, 4, 6, 8, 7, 9, 3, 5], 
[3, 6, 5, 9, 2, 4, 8, 1, 7], 
[8, 7, 9, 1, 5, 3, 6, 4, 2]]
# [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
#                [6, 7, 2, 1, 9, 5, 3, 4, 8],
#                [1, 9, 8, 3, 4, 2, 5, 6, 7],
#                [8, 5, 9, 7, 6, 1, 4, 2, 3],
#                [4, 2, 6, 8, 5, 3, 7, 9, 1],
#                [7, 1, 3, 9, 2, 4, 8, 5, 6],
#                [9, 6, 1, 5, 3, 7, 2, 8, 4],
#                [2, 8, 7, 4, 1, 9, 6, 3, 5],
#                [3, 4, 5, 2, 8, 6, 1, 7, 9]]

# print(getSubMatrix(sudokuboard,1))
# print(getBoardRow(sudokuboard,1))
# print(getBoardColumn(sudokuboard,1))

# matrixDList = []
# for i in range(9):
#     nMatrix = getSubMatrix(sudokuboard,i+1)
#     matrixDList.append(len([x for x in nMatrix if nMatrix.count(x) > 1 and x>=0 and x<=9]))
# isSubMatrixValid = all(i==0 for i in matrixDList)
# print("Submatrices Status ={}".format(isSubMatrixValid))
# matrixDlist = []
# for i in range(9):
#     nMatrix = getBoardRow(sudokuboard,i+1)
#     matrixDList.append(len([x for x in nMatrix if nMatrix.count(x) > 1]))
# isMatrixRowsValid = all(i==0 for i in matrixDList)
# print("Unique Rows Status ={}".format(isMatrixRowsValid))

# matrixDlist = []
# for i in range(9):
#     nMatrix = getBoardColumn(sudokuboard,i+1)
#     matrixDList.append(len([x for x in nMatrix if nMatrix.count(x) > 1]))
# isMatrixColumnsValid = all(i==0 for i in matrixDList)
# print("Unique Columns Status ={}".format(isMatrixColumnsValid))

# isSudokuValid = True if isSubMatrixValid == True and isMatrixColumnsValid == True and isMatrixColumnsValid == True else False
# print(isSudokuValid)




matrixDList = []
zCount = 0
for i in range(9):
    nMatrix = getSubMatrix(sudokuboard,i+1)
    matrixDList.append(len([x for x in nMatrix if nMatrix.count(x) > 1]))
    nMatrix = getBoardRow(sudokuboard,i+1)
    matrixDList.append(len([x for x in nMatrix if nMatrix.count(x) > 1]))
    nMatrix = getBoardColumn(sudokuboard,i+1)
    matrixDList.append(len([x for x in nMatrix if nMatrix.count(x) > 1]))
    zCount = zCount+sum(1 for x in nMatrix if x == 0)
isTotalMatrixValid = all(i==0 for i in matrixDList) and zCount < 1
print(isTotalMatrixValid)



# [[1, 3, 2, 4, 6, 8, 5, 7, 9], 
# [4, 9, 8, 3, 7, 5, 2, 6, 1], 
# [7, 5, 6, 2, 1, 9, 0, 8, 4], 
# [6, 4, 3, 7, 9, 2, 1, 5, 8], 
# [5, 2, 1, 8, 4, 6, 7, 9, 3], 
# [9, 8, 7, 5, 3, 1, 4, 2, 6], 
# [2, 1, 4, 6, 8, 7, 9, 3, 5], 
# [3, 6, 5, 9, 2, 4, 8, 1, 7], 
# [8, 7, 9, 1, 5, 3, 6, 4, 2]]



# matrixDList = []
# for i in range(9):
#     nMatrix = getSubMatrix(sudokuboard,i+1)
#     matrixDList.append(len([x for x in nMatrix if nMatrix.count(x) > 1 and x>0 and x<=9]))
# isSubMatrixValid = all(i==0 for i in matrixDList)
# zCount = sum(1 for x in sudokuboard[2] if x == 0)
# print(zCount)
#print("Submatrices Status ={}".format(isSubMatrixValid))