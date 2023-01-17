def check_password(func):
    def check(*args, **kwargs):
        if input("Введите пароль: ") != '1234':
            print("В доступе отказано")
            return None
        return func(*args, **kwargs)
    return check


@check_password
def fibonacci(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
    return fib1


print(fibonacci(5))
