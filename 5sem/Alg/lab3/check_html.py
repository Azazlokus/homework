from Stack import Stack


def check_html(path):
	s = Stack()
	with open(path) as file:
		for line in file:
			line = line.strip()
			while line != "":
				start1 = line.find("</")
				end = line.find(">", start1)
				if start1 > -1 and end > -1:
					s.pop()
					line = line.replace(line[start1:end+1], "")
				start2 = line.find("<")
				end = line.find(">", start2)
				if start2 > -1 and end > -1:
					s.push(line[start2+1:end])
					line = line.replace(line[start2:end+1], "")
				if start1 < 0 and start2 < 0:
					break	
	if s.isEmpty():
		return True
	else:
		return False

print(check_html("index.html"))