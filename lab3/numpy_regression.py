import sys
import matplotlib.pyplot as plt
from numpy import *

def main():
    inputMatrix = transpose(loadtxt(sys.argv[1]))
    x = inputMatrix[0]
    y = inputMatrix[1]

    calcExpReg(x,y,int(sys.argv[2]))

def calcExpReg(x,y,n):
    """Calculates exponential regression with values X and Y and with the n degree"""
    Xp  = powers(x,0,n)
    Yp  = powers(y,1,1)
    Xpt = Xp.transpose()
    
    #Magic
    a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    a = a[:,0]

    xStep = step(x)
    plt.plot(x,y, "ro")
    plt.plot(xStep, calcPoly(a, xStep))
    plt.show()

def step(x):
    """Returns more x values based on min and max x, with small steps"""
    return linspace(int(x[0]),int(x[-1]),int((x[-1]-x[0])/0.2))

def calcPoly(a,x):
    """Calculates polynomial sum of x with coefficient a"""
    return sum((p*x**i for i,p in enumerate(a)))

def calcLinReg(x,y):
    """Only used for testing purposes, plots a linear regression of x and y"""
    Xp = powers(x,0,1)
    Yp = powers(y,1,1)
    y2 = []

    Xpt = transpose(Xp)
    [[b],[m]] = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    
    for num in x:
        y2.append(b+m*num)
    gPlot(x,y,y2)

def gPlot(x,y,y2):
    """Plot graph and points based on x,y,y2"""
    plt.plot(x,y, "ro")
    plt.plot(x,y2)
    plt.show()


def powers(inputList, powMin, powMax):
    """Returns a matrix with each row as values from inputList rasied to the power of powMin to powMax"""
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