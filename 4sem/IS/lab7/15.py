class Digits:

    def __init__(self, numbers):
        self.numbers = [int(x) for x in numbers.split()]

    def make_negative(self):
        self.numbers = list(
            map(lambda x: -x if x > 0 else x, self.numbers))

    def square(self):
        self.numbers = list(map(lambda x: x ** 2, self.numbers))

    def strange_command(self):
        self.numbers = list(map(lambda x: x + 1 if not x %
                            5 else x, self.numbers))

    def check_command(self):
        for i in range(int(input("Count of commands: "))):
            command = input("Command: ")
            if command in self.funcs:
                self.funcs[command](self)

    funcs = {
        "strange_command": strange_command,
        "square": square,
        "make_negative": make_negative
    }


numbers = input("Numbers: ")
D = Digits(numbers)
D.check_command()
print(D.numbers)
