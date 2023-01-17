def same_by(characteristic, objects):
    res = []
    for obj in objects:
        if characteristic(obj) == 0:
            res.append(obj)
    if res == objects:
        return True
    else:
        return False


values = [1, 2, 4, 4]
if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")
