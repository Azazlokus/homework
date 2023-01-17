class Balance:
    left = 0
    right = 0

    def add_right(self, num):
        self.right += num

    def add_left(self, num):
        self.left += num

    def result(self):
        if self.right == self.left:
            return "="
        elif self.right > self.left:
            return "R"
        else:
            return "L"


balance = Balance()
balance.add_right(10)
balance.add_left(9)
balance.add_left(2)
print(balance.result())
