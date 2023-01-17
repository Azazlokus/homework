def linear(some_list):
    if not some_list:
        return some_list
    if type(some_list[0]) is list:
        return linear(some_list[0]) + linear(some_list[1:])
    return some_list[:1] + linear(some_list[1:])


print(*linear([[1, 2], 4, [[2, 4, -8, [-4, "er", [0], [{2: "primer"}, []]]]]]))
