import random
from time import sleep
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
				labyrinth_map[i].append(CELL_MARK)
			else:
				labyrinth_map[i].append(WALL_MARK)

	start = start_point_generate(n, m)
	finish = finish_point_generate(start, n, m)
	list_transition = [start]
	x, y = start
	visited_cells[x][y] = CELL_MARK
	x, y, tx, ty = direction_choice(x, y, visited_cells)
	for i in range(1, m * n):
		while not (x > -1 and y > -1):
			x, y = list_transition[-1]
			list_transition.pop()
			x, y, tx, ty = direction_choice(x, y, visited_cells)
		visited_cells[x][y] = CELL_MARK
		list_transition.append((x, y))
		labyrinth_map[tx][ty] = CELL_MARK
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
				if matrix[x][y] == CELL_MARK:
					pygame.draw.line(window, COLOR_WAY, [i, j], [i, j], 1)
				else:
					pygame.draw.line(window, COLOR_WALL, [i, j], [i, j], 1)
	pygame.draw.circle(window, COLOR_START, (
		WIDTH_BORDER + start[0] * (WIDTH_CELL + WIDTH_WALL) + WIDTH_CELL // 2, WIDTH_BORDER +
		start[1] * (WIDTH_CELL + WIDTH_WALL) + WIDTH_CELL // 2), WIDTH_CELL // 4)
	pygame.draw.circle(window, COLOR_FINISH, (
		WIDTH_BORDER + finish[0] * (WIDTH_CELL + WIDTH_WALL) + WIDTH_CELL // 2, WIDTH_BORDER +
		finish[1] * (WIDTH_CELL + WIDTH_WALL) + WIDTH_CELL // 2), WIDTH_CELL // 4)

	path = findPath(labyrinth, start, finish)
	for step in path:
		pygame.draw.circle(window, (0, 0, 255), (
			WIDTH_BORDER + step[0] * (WIDTH_CELL + WIDTH_WALL) + WIDTH_CELL // 2, WIDTH_BORDER +
			step[1] * (WIDTH_CELL + WIDTH_WALL) + WIDTH_CELL // 2), WIDTH_CELL // 6)
	pygame.display.update()
	check_events()
		


def convertPos(point):
	x, y = point
	x, y = x * 2 + 1, y * 2 + 1
	if (x % 2 == 1):
		x -= 1
	if (y % 2 == 1):
		y -= 1
	return x, y


def getPath(x, y, lm):
	path = []
	step = 2
	k = lm[x][y]
	while k > START_MARK:
		if x > 1 and lm[x-step][y] == k - 1:
			x, y = x - step, y
			k -= 1
			path.append((x // step, y // step))
		elif y > 1 and lm[x][y-step] == k - 1:
			x, y = x, y - step
			k -= 1
			path.append((x // step, y // step))
		elif x < len(lm)-step and lm[x+step][y] == k - 1:
			x, y = x + step, y
			k -= 1
			path.append((x // step, y // step))
		elif y < len(lm[0]) - step and lm[x][y + step] == k - 1:
			x, y = x, y + step
			k -= 1
			path.append((x // step, y // step))
	path = path[:-1]
	return path


def findPath(matrix, start, finish):
	lm = [row[:] for row in matrix]
	x_start, y_start = convertPos(start)
	lm[x_start][y_start] = START_MARK
	x_finish, y_finish = convertPos(finish)

	k = 1
	while (lm[x_finish][y_finish] == CELL_MARK):
		k += 1
		make_step(k, lm)
	path = getPath(x_finish, y_finish, lm)
	return path


def make_step(k, matrix):
	step = 2
	steps = []
	for i in range(0, len(matrix), step):
		for j in range(len(matrix[0])):
			if matrix[i][j] == k:
				if i > step-1 and matrix[i-step][j] == CELL_MARK and matrix[i-step+1][j] != WALL_MARK:
					matrix[i-step][j] = k + 1
					steps.append((i-step, j))
				if j > step-1 and matrix[i][j-step] == CELL_MARK and matrix[i][j-step+1] != WALL_MARK:
					matrix[i][j-step] = k + 1
					steps.append((i, j-step))
				if i < len(matrix)-step and matrix[i+step][j] == CELL_MARK and matrix[i+step-1][j] != WALL_MARK:
					matrix[i+step][j] = k + 1
					steps.append((i+step, j))
				if j < len(matrix[0])-step and matrix[i][j+step] == CELL_MARK and matrix[i][j+step-1] != WALL_MARK:
					matrix[i][j+step] = k + 1
					steps.append((i, j+step))
	for step in steps:
		pygame.draw.circle(window, (255, 0, 0), (
			WIDTH_BORDER + step[0] // 2 * (WIDTH_CELL + WIDTH_WALL) + WIDTH_CELL // 2, WIDTH_BORDER +
			step[1] // 2 * (WIDTH_CELL + WIDTH_WALL) + WIDTH_CELL // 2), WIDTH_CELL // 8)
	pygame.display.update()
	check_events()
	sleep(0.2)

def check_events():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()


COLOR_WAY = (255, 255, 255)
COLOR_WALL = (0, 0, 0)
COLOR_START = (0, 255, 0)
COLOR_FINISH = (255, 0, 0)
COLOR_BORDER = (192, 192, 192)
WIDTH_WALL = 5
WIDTH_CELL = 20
WIDTH_BORDER = 5
CELL_MARK = 1
WALL_MARK = 0
START_MARK = 2
IS_DRAW = True

n, m = input("Введите размеры лабиринта: ").split()
n = int(n)
m = int(m)
size_x = ((n * 2 - 1) // 2 + 1) * WIDTH_CELL + \
	((n * 2 - 1) // 2) * WIDTH_WALL + 2 * WIDTH_BORDER
size_y = ((m * 2 - 1) // 2 + 1) * WIDTH_CELL + \
	((m * 2 - 1) // 2) * WIDTH_WALL + 2 * WIDTH_BORDER

pygame.init()
window = pygame.display.set_mode((size_x, size_y))
labyrinth, start, finish = create_labyrinth(n, m)

draw_labyrinth(labyrinth, start, finish)
while True:
	check_events()
	sleep(0.1)

	
