def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Это треугольник")
    else:
        print("Это не треугольник")


triangle(1, 1, 2)
triangle(7, 6, 10)
triangle(20, 13, 17)
