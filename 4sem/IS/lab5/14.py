def recursive_len(some_list):
    tmp = 0
    if some_list:
        tmp += 1
    else:
        return 0
    some_list.pop()
    count = tmp + recursive_len(some_list)
    return count


print(recursive_len([1, 2, 3, 4, 5]))
