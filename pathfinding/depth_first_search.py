from math import sqrt,trunc

class node(object):
	def __init__(self, parent, coord):
		self.parent = parent
		self.coord = coord

	def __eq__(self, coord):
		return self.coord == coord

	def __add__(self, coord):
		return (self.coord[0] + coord[0], self.coord[1] + coord[1])

class pathfinder(object):
	def __init__(self, grid, start, end, walls, GUI = None):
		self.START = node(None, start)
		self.END = end
		self.WALLS = walls
		self.WIDTH = grid[0]
		self.HEIGHT = grid[1]
		self.closed = [self.START]
		self.count = 1

	def find_next(self):
		while self.count > 0:
			step = []
			attempted_coord = (0,0)
			for open_index in range(self.count):
				current = self.closed[-(open_index + 1)]
				for neighbour in [(-1,1), (0,1), (1,1), (-1,0), (1,0), (-1,-1), (0,-1), (1,-1)]:
					if current + neighbour == self.END:
						solved = self.pathtrace(current + neighbour, current)
						return solved

					attempted_coord = current + neighbour
					if attempted_coord in self.WALLS \
						or	attempted_coord in self.closed \
						or (attempted_coord)[0] < 0 \
						or (attempted_coord)[1] < 0 \
						or (attempted_coord)[0] >= self.WIDTH or (attempted_coord)[1] >= self.HEIGHT:
							continue
					else:
						newnode = node(current, current + neighbour)
						step.append(newnode)

			self.count = len(step)
			self.closed += step

	def pathtrace(self, neighbour, parent):
		step = []
		print("end\n{}".format(neighbour))
		while parent:
			for node in self.closed:
				if parent == node:
					step.insert(0, node.coord)
					parent = node.parent
					print("{}".format(node.coord))
		print("start")
		return step


a = pathfinder((20,20), (3, 3), (17, 12), 
	[(5, 2), (5, 3), (6, 3), (6, 4), (7, 4), (7, 5), (8, 5), (8, 6), (9, 6), (9, 7), 
	(10, 7), (10, 8), (11, 8), (11, 9), (12, 9), (12, 10), (13, 10), (13, 11), 
	(14, 11), (14, 12), (15, 12), (15, 13), (16, 13), (16, 14), (14, 15), (13, 15), 
	(12, 13), (11, 12), (11, 13), (10, 12), (10, 11), (9, 11), (9, 10), (8, 10), (8, 9), 
	(7, 9), (7, 8), (6, 8), (6, 7), (5, 6), (5, 7), (4, 6), (4, 5), (3, 5), (11, 15), 
	(12, 15), (10, 15), (9, 15), (9, 14), (8, 13), (8, 14), (7, 13), (7, 12), (6, 12), 
	(6, 11), (5, 11), (5, 10), (4, 10), (4, 9), (3, 9), (3, 8), (2, 8), (2, 7), (5, 0), 
	(6, 0), (4, 2), (2, 2), (3, 2), (7, 1), (7, 0), (8, 1), (8, 2), (9, 2), (9, 3), 
	(10, 3), (10, 4), (11, 4), (11, 5), (12, 5), (12, 6), (13, 6), (13, 7), (14, 7), 
	(14, 8), (15, 8), (15, 9), (16, 9), (16, 10), (17, 11), (17, 10), (16, 15), (17, 13), 
	(18, 13), (18, 12), (18, 11), (10, 0), (11, 0), (11, 1), (12, 1), (12, 2), (13, 2), 
	(13, 3), (14, 3), (14, 4), (15, 4), (15, 5), (16, 5), (16, 6), (17, 6), (17, 7), 
	(18, 7), (18, 8), (19, 8), (19, 9), (0, 9), (0, 10), (1, 10), (1, 11), (2, 11), 
	(2, 12), (3, 12), (3, 13), (4, 13), (4, 14), (5, 14), (5, 15), (6, 15), (6, 16), 
	(7, 16), (7, 17), (8, 17), (8, 18), (9, 18), (9, 19), (10, 19), (19, 15), (18, 15), 
	(18, 16), (18, 17), (17, 17), (16, 17), (15, 17), (14, 17), (13, 17), (12, 17), 
	(12, 18), (11, 18), (11, 19)]
)

a.find_next()
