login = input("Логин: ")
back_addr = input("Резервный адрес: ")
if '@' in login or '@' not in back_addr:
    print("Неверный логин или резервный адрес")
