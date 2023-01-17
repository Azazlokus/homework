def square_fibonacci(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1 * fib1


for fib in square_fibonacci(7):
    print(fib, end=" ")
