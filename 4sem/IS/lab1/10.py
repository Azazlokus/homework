while True:
    fact = 1
    num1 = int(input())
    op = input()
    if op == "x":
        print(num1)
        break
    else:
        if op == "!" and num1 > 0:
            for i in range(1, num1+1):
                fact *= i
            print(fact)
            continue
        elif num1 < 0:
            continue
        num2 = int(input())
        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "*":
            print(num1 * num2)
        elif op == "/" and num2 != 0:
            print(num1 // num2)
        elif op == "%":
            print(num1 % num2)
