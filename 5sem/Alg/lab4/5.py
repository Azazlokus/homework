import secrets
from hashlib import scrypt


def auth():
	login = input("Введите логин: ")
	password = input("Введите пароль: ").encode()
	salt = None
	hash = None
	with open("bd.txt", "r") as file:
		for line in file:
			row = line.split(";")
			if row[0] == login:
				salt = row[1].encode()
				hash = row[2]
	if salt == None or hash == None:
		print("Пользователя под данным логином не существует")
		return
	hashed_pass = scrypt(password=password, salt=salt, n=8, r=512, p=4, dklen=32).hex()
	if (hash == hashed_pass):
		print("Успешно!")
	else:
		print("Неверный пароль")

def reg():
	login = input("Введите логин: ")
	password = input("Введите пароль: ").encode()
	salt = secrets.token_hex(32).encode()
	hashed_pass = scrypt(password=password, salt=salt, n=8, r=512, p=4, dklen=32).hex()
	with open("bd.txt", "a") as file:
		file.write(login + ";" + salt.decode() + ";" + hashed_pass)


while True:
	print("Выберите действие")
	print("1. Авторизация")
	print("2. Регистрация")
	n = int(input())
	if n == 1:
		auth()
	elif n == 2:
		reg()