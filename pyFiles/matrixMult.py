# Matrix Multiplication
def printMatrix(m):
	for row in m:
		print(row)
		
def matrixMult(A, B):
	C = []
	if len(A[0]) == len(B):
		for i in range(len(A)):
			array = []
			for j in range(len(B[0])):
				sum = 0
				for k in range(len(B)):
					sum += A[i][k] * B[k][j]
				array.append(sum)
			C.append(array)
	else:
		print("Matrix Multiplication Cannot Be Computed!")
	return C

A = [[2, -3, 3],
	[-2, 6, 5],
	[4, 7, 8]]

B = [[-1, 9, 1],
	[ 0, 6, 5],
	[ 3, 4, 7]]

printMatrix(matrixMult(A, B))