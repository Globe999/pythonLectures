import random

class FifteenModel:
	def __init__(self):
		self.gameMatrix = []
		n = 1
		for i in range(4):
			row = []
			for j in range(n,n+4):
				if (j == 16):
					row.append(0)
				else:
					row.append(j)
			n += 4
			self.gameMatrix.append(row)


	def getValue(self,row,col):
		return self.gameMatrix[row][col]

	def tryMove(self,row,col):
		if 0 <= row-1 and self.gameMatrix[row-1][col] == 0:
			self.__flipNum(row, col, row-1,col)
		elif row+1 < 4 and self.gameMatrix[row+1][col] == 0:
			self.__flipNum(row, col, row+1,col)
		elif 0 <= col-1 and self.gameMatrix[row][col-1] == 0:
			self.__flipNum(row, col, row,col-1)
		elif col+1 < 4 and self.gameMatrix[row][col+1] == 0:
			self.__flipNum(row, col, row,col+1)

	#Row1 = current row, row2 = other row
	def __flipNum(self, row1, col1, row2, col2):
		self.gameMatrix[row2][col2] = self.gameMatrix[row1][col1]
		self.gameMatrix[row1][col1] = 0
	def shuffle(self):
		#Create list
		numList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
		self.gameMatrix = []
		for _ in range(4):
			row = []
			for i in range(4):
				randomNum = random.choice(numList)
				if not randomNum:
					randomNum = 0
				numList.pop(numList.index(randomNum))
				row.append(randomNum)
			self.gameMatrix.append(row)