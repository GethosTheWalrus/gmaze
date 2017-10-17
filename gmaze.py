import pygame

maze = [[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,1,0,1],
		[1,1,1,1,0,1,1,1,1,1,1,0,0,0,1,1,0,1,0,1],
		[1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1],
		[1,0,0,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,1,1],
		[1,1,1,1,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,1],
		[1,1,0,1,0,1,0,1,0,1,0,0,1,1,1,1,0,1,0,1],
		[1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,1,1,0,1],
		[1,0,1,1,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,1],
		[1,0,0,1,0,0,0,0,1,0,1,1,1,1,1,1,1,0,1,1],
		[1,0,1,1,0,1,1,1,1,0,1,0,0,0,0,0,0,0,1,1],
		[1,0,0,1,0,1,0,1,0,0,1,0,1,1,1,1,0,1,0,1],
		[1,0,1,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,1],
		[1,1,1,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1],
		[1,0,0,1,0,0,0,0,1,0,1,0,1,1,1,0,1,1,1,1],
		[1,0,1,1,0,1,1,0,1,0,1,0,1,0,0,0,0,0,0,1],
		[1,0,0,1,0,0,1,0,1,0,0,1,1,0,1,1,1,1,0,1],
		[1,0,1,1,0,1,0,0,1,0,1,1,0,0,0,0,1,1,1,1],
		[1,0,0,0,0,1,0,1,1,0,0,0,1,0,1,0,0,0,0,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
		]

wM = 500
hM = 500

mH = len(maze)
mW = len(maze[0])

pygame.init()
screen = pygame.display.set_mode((wM, hM))
done = False


def solveMaze(p,  m):
	wasHere = [[False for i in range(mW)] for j in range(mH)]
	correctPath = [[False for i in range(mW)] for j in range(mH)]

	recursiveSolve(p, m, wasHere, correctPath, 0, 0)

	return correctPath

def recursiveSolve(p, m, w, c, x, y):
	p.event.get()
	drawBlock(p, y * (wM / mW) + (wM / mW) / 4, x * (hM / mH) + (hM / mH) / 4, (wM / mW) / 2, (hM / mH) / 2, 128, 128, 255, 100)

	if x == mW - 1 and y == mH - 1:
		c[x][y] = True
		drawBlock(p, y * (wM / mW) + (wM / mW) / 4, x * (hM / mH) + (hM / mH) / 4, (wM / mW) / 2, (hM / mH) / 2, 128, 255, 128, 100)
		return True

	if m[x][y] == 1 or w[x][y]:
		drawBlock(p, y * (wM / mW) + (wM / mW) / 4, x * (hM / mH) + (hM / mH) / 4, (wM / mW) / 2, (hM / mH) / 2, 255, 128, 128, 100)
		return False

	w[x][y] = True

	if x != 0:
		if recursiveSolve(p, m, w, c, x - 1, y):
			c[x][y] = True
			drawBlock(p, y * (wM / mW) + (wM / mW) / 4, x * (hM / mH) + (hM / mH) / 4, (wM / mW) / 2, (hM / mH) / 2, 128, 255, 128, 100)
			return True

	if x != mW - 1:
		if recursiveSolve(p, m, w, c, x + 1, y):
			c[x][y] = True
			drawBlock(p, y * (wM / mW) + (wM / mW) / 4, x * (hM / mH) + (hM / mH) / 4, (wM / mW) / 2, (hM / mH) / 2, 128, 255, 128, 100)
			return True

	if y != 0:
		if recursiveSolve(p, m, w, c, x, y - 1):
			c[x][y] = True
			drawBlock(p, y * (wM / mW) + (wM / mW) / 4, x * (hM / mH) + (hM / mH) / 4, (wM / mW) / 2, (hM / mH) / 2, 128, 255, 128, 100)
 			return True

	if y != mH - 1:
		if recursiveSolve(p, m, w, c, x, y + 1):
			c[x][y] = True
			drawBlock(p, y * (wM / mW) + (wM / mW) / 4, x * (hM / mH) + (hM / mH) / 4, (wM / mW) / 2, (hM / mH) / 2, 128, 255, 128, 100)
			return True

	drawBlock(p, y * (wM / mW) + (wM / mW) / 4, x * (hM / mH) + (hM / mH) / 4, (wM / mW) / 2, (hM / mH) / 2, 255, 128, 128, 100)
	return False

def drawBlock(p, x, y, w, h, r, g, b, delay):
	if delay > 0:
		p.time.wait(delay)
	p.draw.rect(screen, (r, g, b), pygame.Rect(x, y, w, h))
	p.display.flip()

def drawMaze(p, m):
	for rowNum, row in enumerate(maze):
		for colNum, val in enumerate(row):
			if val == 1:
				drawBlock(p, colNum * (wM / mW), rowNum * (hM / mH), (wM / mW), (hM / mH), 0, 128, 255, 0)

solved = False

while not done:
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
					done = True	

	if not solved:
		#draw the maze from the matrix
		drawMaze(pygame, maze)
		pygame.display.flip()
		#find the solution
		solveMaze(pygame, maze)
		solved = True