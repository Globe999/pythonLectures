
import sys, numpy

import matplotlib.pyplot as plt

def logmap(r, x):
	return r*x*(1-x)


def experiment(r, x, n):
	for _ in range(1,n):
		print (x)
		x = logmap(r, x)
	print(x)


def table(r, x1, x2, n):
	for _ in range(n):
		print (x1, x2)
		x1 = logmap(r, x1)
		x2 = logmap(r, x2)

def attractors(r,x,n,epsilon):
	output = []

	found = False

	a = 0

	for _ in range(n+1):
		x = logmap(r, x)

		clear = False
		for old_x in output:
			if abs(x - old_x) < epsilon:
				clear = True
				a += 1
				found = True
				break
		if clear:
			output = []
			x = old_x

		output.append(x)

	if not found:
		return []

	return output


#print(attractors(3.5,0.2,100,1e-5))

def bifurcationDiagram():
	x = []
	y = []

	xval = 0

	while xval <= 3.9:
		list = attractors(xval, 0.2, 250, 1e-5)

		if list:
			for l in list:
				x.append(xval)
				y.append(l)

		xval += 0.003


	plt.scatter(x, y, color="red", s=0.5, label="dot")

	plt.xlabel("ages")
	plt.ylabel("sal")
	plt.title("ages and sals")

	plt.legend()
	plt.show()

bifurcationDiagram()


#table(2.5, 0.20, 0.21, 20)
