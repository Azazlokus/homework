class SparceArray:
    
    def __init__(self):
        self.arr = {}

    def __getitem__(self, key):
        return self.arr.get(key, 0)

    def __setitem__(self, key, value):
        self.arr[key] = value


sa = SparceArray()
sa[0] = 1
sa[10] = 5
for i in range(0, 11):
    print(i, ":", sa[i])
