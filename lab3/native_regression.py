import sys
import matplotlib.pyplot as plt
from matrix import *

def main():
    inputMatrix = transpose(loadtxt("lab3/chirps.txt"))
    x = inputMatrix[0]
    y = inputMatrix[1]
    Xp  = powers(x,0,1)
    Yp  = powers(y,1,1)

    Xpt = transpose(Xp)
    [[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    y2 = []
    for num in x:
        y2.append(b+m*num)

    #for each point, 
    plt.plot(x,y, "ro")
    plt.plot(x,y2)
    plt.show()
    #predicted number of chirps = b + m * temperature
    #y = kx+m: 

def calc(b, m, temp):
    return b + (m * temp)

def gPlot(x,y,y2):
    plt.plot(x,y, "ro")
    plt.plot(x,y2)
    plt.show()


main()