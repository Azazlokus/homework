def from_string_to_list(string, container):
    string = string.split()
    for num in string:
        container.append(int(num))


a = [1, 2, 3]
from_string_to_list("1 3 99 52", a)
print(*a)
