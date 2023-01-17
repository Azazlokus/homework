actions = {
    'read': 'r',
    'write': 'w',
    'execute': 'x'
}

files_num = int(input())
files = {}
for i in range(files_num):
    file, *permissions = input().split()
    files[file] = set(permissions)

request_num = int(input())
for i in range(request_num):
    action, file = input().split()
    if actions[action] in files[file]:
        print("OK")
    else:
        print("Access denied")
