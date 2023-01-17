def arithmetic_operation(operation):
    def math(a, b):
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            return a / b
    return math


operation = arithmetic_operation('*')
print(operation(3, 6))
