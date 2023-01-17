class Summator:

    def transform(self, n):
        return n

    def sum(self, N):
        return sum(self.transform(i) for i in range(1, N + 1))


class SquareSummator(Summator):

    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):

    def transform(self, n):
        return n ** 3


S1 = Summator()
S2 = SquareSummator()
S3 = CubeSummator()

print(S1.sum(3))
print(S2.sum(3))
print(S3.sum(3))
