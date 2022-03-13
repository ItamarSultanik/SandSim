def generate_grid():
	"""
	Function will generate an L.O.L that
	will represent the grid.
	:return: The grid list
	:rtype: list
	"""
	r_list = []
	for i in range(WIDTH // GRAIN_SIZE):
		r_list.append([0] * (WIDTH // GRAIN_SIZE))

	return r_list

def draw_grid(g):
	"""
	Function draws a representation of the grid with lines
	on the app window. Meant for development stages.
	:param g: The grid
	:type g: list
	"""
	for row in range(len(g)):
		pygame.draw.line(screen, WHITE, (row*GRAIN_SIZE, 0), (row*GRAIN_SIZE, WIDTH), 1)
		pygame.draw.line(screen, WHITE, (0, row*GRAIN_SIZE), (WIDTH, row*GRAIN_SIZE), 1)

def draw_grains(g):
	"""
	Function responsable for displaying the sand grain's location.
	:param g: The grid
	:type g: list
	"""
	for row in range(len(g)):
		for col in range(len(g)):
			if g[row][col] == 1:
				pygame.draw.rect(screen, WHITE, (col*GRAIN_SIZE, row*GRAIN_SIZE, GRAIN_SIZE, GRAIN_SIZE))

def update_grid(g, gr):
	"""
	Function does all of the checks and updates the grid.
	:param g: The grid
	:param gr: The list of all grain's locations
	:type g: list
	:type gr: list
	:return: The updated grid and list
	:rtype: tuple(g: list, gr: list)
	"""
	for i in gr: # Checking each grain of sand
		row, col = i # A grain is represented by a tuple marking it's location
		if row+1 < len(g):
			if g[row+1][col] == 0:
				# Removing the grain
				g[row][col] = 0
				gr.remove(i)

				# Adding it after movement
				g[row+1][col] = 1
				gr.append((row+1, col))
			else:
				if g[row+1][col-1] == 0:
					# Removing the grain
					g[row][col] = 0
					gr.remove(i)

					# Adding it after movement
					g[row+1][col-1] = 1
					gr.append((row+1, col-1))
				elif col+1 < len(g) and g[row+1][col+1] == 0:
					# Removing the grain
					g[row][col] = 0
					gr.remove(i)

					# Adding it after movement
					g[row+1][col+1] = 1
					gr.append((row+1, col+1))
	return g, gr

def mainloop():
	"""
	Main loop of the simulation.
	No input or output.
	"""
	from sys import exit
	grid = generate_grid()
	grains = []
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		# Spanning new sand
		pos = pygame.mouse.get_pos()
		r = pos[1] // GRAIN_SIZE
		c = pos[0] // GRAIN_SIZE
		grid[r][c] = 1
		grains.append((r, c))

		# Simulating sand physics
		grid, grains = update_grid(grid, grains)

		# graphics
		"draw_grid(grid)"
		screen.fill(BLACK)
		draw_grains(grid)

		pygame.display.update()
		clock.tick(FPS)

if __name__ == '__main__':
	import pygame

	# Initializing pygame
	pygame.init()
	clock = pygame.time.Clock()
	FPS = 120

	# Constants
	GRAIN_SIZE = 5 # px
	WIDTH = 750 # px
	
	# Screen instant
	screen = pygame.display.set_mode((WIDTH, WIDTH))
	pygame.display.set_caption('sand simulation')

	# Colors
	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)

	# Starting the sim
	mainloop()
