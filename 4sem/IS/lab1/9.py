def check_pass(password, repass):
    if len(password) < 8:
        print("Короткий!")
        return False
    if "123" in password:
        print("Простой!")
        return False
    if password != repass:
        print("Различаются.")
        return False
    print("OK")
    return True


password = input("Введите пароль: ")
repass = input("Подтвердите пароль: ")

while(not check_pass(password, repass)):
    password = input("Введите пароль: ")
    repass = input("Подтвердите пароль: ")
