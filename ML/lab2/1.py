import numpy as np


# 1
print("1)")
arr = np.array([1, 7, 13, 105])
print("Байты:", arr.nbytes)

np.savetxt("file.txt", arr)
txt = np.loadtxt("file.txt")
print("txt file:", txt)

arr.tofile("file.bin")
bin = np.fromfile("file.bin", dtype=int)
print("bin file", bin)

# 2
print("2)")
arr1 = np.zeros(10)
arr2 = np.ones(10)
arr3 = np.ones(10) * 5
print(arr1, arr2, arr3, sep="\n")

# 3
print("3)")
arr = np.arange(30, 71, 2)
print(arr)

# 4
print("4)")
arr = np.linspace(5, 50, 10)
print(arr)

# 5
print("5)")
arr = np.random.randint(1, 100, size=(3, 3, 3))
print(arr)

# 6
print("6)")
arr = np.arange(30, 42).reshape(3, 4)
print(arr)

# 7
print("7)")
arr = np.ones((10, 10))
arr[1:-1, 1:-1] = 0
print(arr)

# 8
print("8)")
arr = np.diag([1, 2, 3, 4, 5])
print(arr)

# 9
print("9)")
arr = np.zeros((4, 4))
arr[::2, 1::2] = 1
arr[1::2, ::2] = 1
print(arr)

# 10
print("10)")
arr = np.arange("2017-03", "2017-04", dtype="datetime64[D]")
print(arr)
