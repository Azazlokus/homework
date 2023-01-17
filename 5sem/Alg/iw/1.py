import random
import pygame


def start_point_generate(n, m):
	pos_choice = [True, False]
	x_choice = [0, n - 1]
	y_choice = [0, m - 1]
	if random.choice(pos_choice):
		if random.choice(pos_choice):
			start = (0, random.choice(y_choice))
		else:
			start = (n - 1, random.choice(y_choice))
	else:
		if random.choice(pos_choice):
			start = (random.choice(x_choice), 0)
		else:
			start = (random.choice(x_choice), m - 1)
	return start


def finish_point_generate(start, n, m):
	return n - 1 - start[0], m - 1 - start[1]


def direction_choice(x, y, matrix):
	choice_list = []
	if x > 0:
		if not matrix[x - 1][y]:
			choice_list.append((x - 1, y))
	if x < len(matrix) - 1:
		if not matrix[x + 1][y]:
			choice_list.append((x + 1, y))
	if y > 0:
		if not matrix[x][y - 1]:
			choice_list.append((x, y - 1))
	if y < len(matrix[0]) - 1:
		if not matrix[x][y + 1]:
			choice_list.append((x, y + 1))

	if choice_list:
		nx, ny = random.choice(choice_list)
		if x == nx:
			if ny > y:
				tx, ty = x * 2, ny * 2 - 1
			else:
				tx, ty = x * 2, ny * 2 + 1
		else:
			if nx > x:
				tx, ty = nx * 2 - 1, y * 2
			else:
				tx, ty = nx * 2 + 1, y * 2
		return nx, ny, tx, ty
	else:
		return -1, -1, -1, -1


def create_labyrinth(n, m):
	visited_cells = []
	for i in range(n):
		visited_cells.append([])
		for j in range(m):
			visited_cells[i].append(0)

	labyrinth_map = []
	for i in range(n * 2 - 1):
		labyrinth_map.append([])
		for j in range(m * 2 - 1):
			if i % 2 == 0 and j % 2 == 0:
				labyrinth_map[i].append(1)
			else:
				labyrinth_map[i].append(0)

	start = start_point_generate(n, m)
	finish = finish_point_generate(start, n, m)
	list_transition = [start]
	x, y = start
	visited_cells[x][y] = 1
	x, y, tx, ty = direction_choice(x, y, visited_cells)
	for i in range(1, m * n):
		while not (x > -1 and y > -1):
			x, y = list_transition[-1]
			list_transition.pop()
			x, y, tx, ty = direction_choice(x, y, visited_cells)
		visited_cells[x][y] = 1
		list_transition.append((x, y))
		labyrinth_map[tx][ty] = 1
		x, y, tx, ty = direction_choice(x, y, visited_cells)
	return labyrinth_map, start, finish


def draw_labyrinth(matrix, start, finish):
	width = (len(matrix) // 2 + 1) * WIDTH_CELL + \
			(len(matrix) // 2) * WIDTH_WALL + WIDTH_BORDER * 2
	height = (len(matrix[0]) // 2 + 1) * WIDTH_CELL + \
		(len(matrix[0]) // 2) * WIDTH_WALL + WIDTH_BORDER * 2
	for i in range(width):
		for j in range(height):
			if i < WIDTH_BORDER or width - i <= WIDTH_BORDER or j < WIDTH_BORDER or height - j <= WIDTH_BORDER:
				pygame.draw.line(window, COLOR_BORDER, [i, j], [i, j], 1)
			else:
				x = (i - WIDTH_BORDER) // (WIDTH_CELL + WIDTH_WALL) * 2 + 1
				y = (j - WIDTH_BORDER) // (WIDTH_CELL + WIDTH_WALL) * 2 + 1
				if (i - WIDTH_BORDER) % (WIDTH_CELL + WIDTH_WALL) <= WIDTH_CELL:
					x -= 1
				if (j - WIDTH_BORDER) % (WIDTH_CELL + WIDTH_WALL) <= WIDTH_CELL:
					y -= 1
				if matrix[x][y] == 1:
					pygame.draw.line(window, COLOR_WAY, [i, j], [i, j], 1)
				else:
					pygame.draw.line(window, COLOR_WALL, [i, j], [i, j], 1)
	pygame.draw.circle(window, COLOR_START, (
		WIDTH_BORDER + start[0] * (WIDTH_CELL + WIDTH_WALL) + WIDTH_CELL // 2, WIDTH_BORDER +
		start[1] * (WIDTH_CELL + WIDTH_WALL) + WIDTH_CELL // 2), WIDTH_CELL // 4)
	pygame.draw.circle(window, COLOR_FINISH, (
		WIDTH_BORDER + finish[0] * (WIDTH_CELL + WIDTH_WALL) + WIDTH_CELL // 2, WIDTH_BORDER +
		finish[1] * (WIDTH_CELL + WIDTH_WALL) + WIDTH_CELL // 2), WIDTH_CELL // 4)


COLOR_WAY = (255, 255, 255)
COLOR_WALL = (0, 0, 0)
COLOR_START = (0, 255, 0)
COLOR_FINISH = (255, 0, 0)
COLOR_BORDER = (192, 192, 192)
WIDTH_WALL = 5
WIDTH_CELL = 20
WIDTH_BORDER = 5

n, m = input("Введите размеры лабиринта: ").split()
n = int(n)
m = int(m)
size_x = ((n * 2 - 1) // 2 + 1) * WIDTH_CELL + ((n * 2 - 1) // 2) * WIDTH_WALL + 2 * WIDTH_BORDER
size_y = ((m * 2 - 1) // 2 + 1) * WIDTH_CELL + ((m * 2 - 1) // 2) * WIDTH_WALL + 2 * WIDTH_BORDER

pygame.init()
window = pygame.display.set_mode((size_x, size_y))
labyrinth, start, finish = create_labyrinth(n, m)
draw_labyrinth(labyrinth, start, finish)
pygame.display.update()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
