import numpy as np

def make_identity(matrix):
	for nrow in range(len(matrix)-1, 0, -1):
		row = matrix[nrow]
		for upper_row in matrix[:nrow]:
			factor = upper_row[nrow]
			upper_row -= factor*row
	return matrix

def gauss(matrix):
	for nrow in range(len(matrix)):
		pivot = nrow + np.argmax(abs(matrix[nrow:, nrow]))
		if pivot != nrow:
			matrix[[nrow, pivot]] = matrix[[pivot, nrow]]
		row = matrix[nrow]
		divider = row[nrow]
		if abs(divider) < 1e-10:
			return
		row /= divider
		for lower_row in matrix[nrow+1:]:
			factor = lower_row[nrow]  
			lower_row -= factor*row  
	make_identity(matrix)
	return matrix

matrix = np.array([
	[2.4, 0.2, -0.3, -1.1, 5.8, 23.84],
	[0.3, 0.1, 1.1, 10.2, 1.0, 38.85],
	[0.5, -6.2, 0.1, 1.5, -1.2, 17.23],
	[0.1, 2.1, 5.1, 0.2, -0.3, 6.56],
	[2.5, 0.1, 0.2, 0.3, 0.4, 6.63]
])

n = len(matrix)
roots = make_identity(gauss(np.copy(matrix)))[:, n]
print(roots)
print(np.matmul(matrix[:, :n], roots.T) - matrix[:, n])
