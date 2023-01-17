from Stack import Stack

s = Stack()

while True:
	expr = input()
	if expr:
		expr = expr.split()
		for sumb in expr:		
			if sumb in ("+", "-", "/", "*") and  s.size() > 1:
				num1 = int(s.pop())
				num2 = int(s.pop())
				print("Result: ", end="")
				if sumb == "+":
					num = num1 + num2
				elif sumb == "-":
					num = num1 - num2
				elif sumb == "*":
					num = num1 * num2
				elif sumb == "/":
					num = num1 / num2
				s.push(num)
				print(num)
			elif sumb.isdigit():
				s.push(sumb)
			else:
				print("Invalid operation")
	else:
		break