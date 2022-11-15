import numpy as np



def seidel(matrix):
	err = 1.e-5
	n = len(matrix)
	x = [-matrix[i][i] for i in range(n)]
	b = matrix[:, :n]
	c = matrix[:, n]
	for i in range(n):
		for j in range(n):
			b[i][j] /= x[i] 
		b[i][i] = 0
		c[i] /= -x[i]
		
	x = c
	max = 1
	it = 0
	if count_norm(b) < 1:
		while max > err:
			x_new = [0] * n
			for i in range(n):
				for j in range(n):
					x_new[i] += b[i][j] * x[j]
				x_new[i] += c[i]

			max = -1
			for i in range(n):
				sub = abs(x_new[i] - x[i])
				if sub > max:
					max = sub 
			x = x_new
			it += 1
	else:
		x = []
	return x, it
		

def count_norm(matrix):
	max = -1
	for row in matrix:
		sum_row = sum(abs(row))
		if sum_row > max:
			max = sum_row
	return max

matrix = np.array([
	[2.4, 0.2, -0.3, -1.1, 5.8, 23.84],
   	[0.3, 0.1, 1.1, 10.2, 1.0, 38.85],
   	[0.5, -6.2, 0.1, 1.5, -1.2, 17.23],
   	[0.1, 2.1, 5.1, 0.2, -0.3, 6.56],
   	[2.5, 0.1, 0.2, 0.3, 0.4, 6.63]
])

"""matrix = np.array([
	[4.0, -1.0, -2.0, 4.0],
	[1.0, -4.0, -1.0, -6.0],
	[2.0, -1.0, -4.0, 4.0]
])"""

result, it = seidel(matrix)
print(result, it)
