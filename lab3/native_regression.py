import sys
import matplotlib.pyplot as plt
from matrix import *

def main():
    inputMatrix = transpose(loadtxt(sys.argv[1]))
    Xp  = powers(inputMatrix[0],0,1)
    Yp  = powers(inputMatrix[1],1,1)
    Xpt = transpose(Xp)
    [[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    #predicted number of chirps = b + m * temperature
main()