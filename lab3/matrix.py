def transpose(matrix):
    tranposed = []
    colIndex = 0
    rowIndex = 0
    if not matrix:
        return []

    for colIndex in range(len(matrix[0])):
        newrow = []
        for row in matrix:
            newrow.append(matrix[rowIndex][colIndex])
            rowIndex += 1
        rowIndex = 0
        tranposed.append(newrow)
    return tranposed


def powers(inputList, powMin, powMax):
    if not inputList:
        return []
    matrix = []
    for i in inputList:
        row = []
        for pow in range(powMin, powMax+1):
            row.append(i**pow)
        matrix.append(row)
    return matrix

def matmul(mat1, mat2):
    if not mat1 or not mat2:
        return []
    
    resultMatrix = []
    row = []
    for _ in range(len(mat2[0])):
        row.append(0)
    for _ in range(len(mat1)):
        resultMatrix.append(row.copy())
    # iterate through rows of mat1
    for i in range(len(mat1)):
    # iterate through columns of mat2
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
            # iterate through rows of mat2
                resultMatrix[i][j] += (mat1[i][k] * mat2[k][j])
    return resultMatrix



def invert(matrix):
    #Hardcoded because it's always a 2x2 matrix
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    det = a*d-b*c
    return[[d/det,-b/det],[-c/det, a/det]]

def loadtxt(file):
    txt = open(file, encoding="utf-8")
    txtLines = txt.readlines()
    txt.close()
    matrix = []
    if not txtLines:
        return []

    for l in txtLines:
        strList = l.rstrip("\n").split("\t")
        
        strList[:] = [x for x in strList if x]
        floatList = list(map(float, strList))
        matrix.append(floatList)
    return matrix
