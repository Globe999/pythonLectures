import sys
import matplotlib.pyplot as plt
from numpy import *

def main():
    inputMatrix = transpose(loadtxt(sys.argv[1]))
    x = inputMatrix[0]
    y = inputMatrix[1]
    
    # calcLinReg(x,y)
    calcExpReg(x,y,int(sys.argv[2]))

def calcExpReg(x,y,n):
    Xp  = powers(x,0,n)
    Yp  = powers(y,1,1)
    Xpt = Xp.transpose()

    a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    a = a[:,0]
    y2 = []
    print(a)
    for num in x:
        y2.append(calcPoly(a,num))
    gPlot(x,y,y2)

def calcPoly(a,x):
    y = []
    for i in a:
        y.append(i**x)
    return y

def calcLinReg(x,y):
    Xp = powers(x,0,1)
    Yp = powers(y,1,1)
    y2 = []

    Xpt = transpose(Xp)
    [[b],[m]] = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    
    for num in x:
        y2.append(b+m*num)
    gPlot(x,y,y2)

def gPlot(x,y,y2):
    plt.plot(x,y, "ro")
    plt.plot(x,y2)
    plt.show()


def powers(inputList, powMin, powMax):
    if inputList.size == 0:
        return []
    matrix = []
    for i in inputList:
        row = []
        for pow in range(powMin, powMax+1):
            row.append(i**pow)
        matrix.append(row)
    return array(matrix)


main()