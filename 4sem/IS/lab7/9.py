class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):

    def __init__(self, a):
        super().__init__(a, a, a)


triangle1 = Triangle(2, 1, 1)
print(triangle1.perimetr())
t = EquilateralTriangle(5)
print(t.perimetr())
print(t.a, t.b, t.c)
