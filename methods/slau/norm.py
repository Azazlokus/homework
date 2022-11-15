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


def inverse_matrix(matrix_origin):
   
    n = matrix_origin.shape[0]
    m = np.hstack((matrix_origin, np.eye(n)))

    for nrow, row in enumerate(m):
        divider = row[nrow]  
        
        row /= divider
        for lower_row in m[nrow+1:]:
            factor = lower_row[nrow]  
            lower_row -= factor*row  
    for k in range(n - 1, 0, -1):
        for row_ in range(k - 1, -1, -1):
            if m[row_, k]:
                m[row_, :] -= m[k, :] * m[row_, k]
    return m[:, n:]

def count_norm(matrix):
	max = -1
	for row in matrix:
		sum_row = sum(abs(row))
		if sum_row > max:
			max = sum_row
	return max

matrix = np.array([
    [1.0, 1.0, -2.0, 6.0],
    [2.0, 3.0, -7.0, 16.0],
    [5.0, 2.0, 1.0, 16.0],
])

n = len(matrix)

n_matrix = matrix[:, :n]
inverted_matrix = inverse_matrix(matrix[:, :n])

a1 = count_norm(n_matrix)
a2 = count_norm(inverted_matrix)
print(a1, a2)
print(a1 * a2)

