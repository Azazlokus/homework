class Summator:

    def transform(self, n):
        return n

    def sum(self, N):
        return sum(self.transform(i) for i in range(1, N + 1))


class PowerSummator(Summator):

    def __init__(self, b):
        self.b = b

    def transform(self, n):
        return n ** self.b


class SquareSummator(PowerSummator):

    def __init__(self):
        super().__init__(2)


class CubeSummator(PowerSummator):

    def __init__(self):
        super().__init__(3)


S1 = Summator()
S2 = SquareSummator()
S3 = CubeSummator()
SP = PowerSummator(2)

print(S1.sum(3))
print(S2.sum(3))
print(S3.sum(3))
print(SP.sum(3))
