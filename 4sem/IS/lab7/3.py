class Selector:
    
    def __init__(self, values):
        self.values = values

    def get_odds(self):
        return list(filter(lambda x: x % 2, self.values))

    def get_evens(self):
        return list(filter(lambda x: not x % 2, self.values))


values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
selector = Selector(values)
print(*selector.get_odds())
print(*selector.get_evens())
