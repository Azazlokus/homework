def partial_sums(*num):
    res = [0]
    for i in range(len(num)):
        res.append(res[i] + num[i])
    return res


print(partial_sums(1, 0.5, 0.25, 0.125))
