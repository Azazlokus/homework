def check_password(password):
    def wrapper(func):
        def check(*args, **kwargs):
            if input("Введите пароль: ") != password:
                print("В доступе отказано")
                return None
            return func(*args, **kwargs)
        return check
    return wrapper


@check_password('1234')
def make_burger():
    print("Это функция обернутая в декоратор с параметром")


make_burger()
