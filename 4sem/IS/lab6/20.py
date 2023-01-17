def cached(func):
    cache = {}
    print("Вывод кеша:")

    def cache_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        print(cache)
        return cache[args]
    return cache_func


@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


fib(5)
