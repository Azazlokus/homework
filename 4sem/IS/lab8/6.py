import random


with open("lines.txt", "r") as file:
    lines = file.readlines()
    print(random.choice(lines))
