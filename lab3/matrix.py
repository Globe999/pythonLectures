def transpose(matrix):
    tranposed = []
    colIndex = 0
    rowIndex = 0
    for colIndex in range(len(matrix[0])):
        newrow = []
        for row in matrix:
            newrow.append(matrix[rowIndex][colIndex])
            rowIndex += 1
        rowIndex = 0
        tranposed.append(newrow)
    return tranposed


def powers(inputList, powMin, powMax):
    matrix = []
    for i in inputList:
        row = []
        for pow in range(powMin, powMax+1):
            row.append(i**pow)
        matrix.append(row)
    return matrix

def matmul(mat1, mat2):
    resultMatrix = []
    pass


def main():
    m = [[1,2],[3,4],[5,6],[7,8]]
    print(transpose(m))
    # print(powers([2,3,4],0,5))

main()