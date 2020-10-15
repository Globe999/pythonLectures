import os

def gcd(m, n):
	if not m or not n:
		return n+m
	while n:
		m,n = n,m%n	
	return m

def binarySearch(values, i, j, key):
	if i > j:
		return None
	k = (i+j)//2
	print("MinVal: {}, MaxVal {}, i: {} j: {} key: {} k: {}".format(values[0], values[-1], i,j,key,k))
	if values[k] == key:
		return k
	elif values[k] < key:
		return binarySearch(values.copy(), i, k-1, key)
	elif values[k] > key:
		return binarySearch(values.copy(), k+1, j, key)

def totalFileSize(path):




val = []
for i in list(reversed(range(1000))):
    val.append(i)

print(binarySearch(val, 0, len(val)-1, 2))