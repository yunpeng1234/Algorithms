from math import sqrt,trunc

#NOT ACTUALLY DJIKSTRAS its me best first search
from math import sqrt,trunc
import GUI_final

class node(object):
	def __init__(self, position, parent, h):
		self.position = position
		self.parent = parent
		self.h = h

	def __add__(self, diff):
		return(self.position[0] + diff[0], self.position[1] + diff[1])
		

	def __eq__(self, other):
		return self.position == other

# def truncate(number):
# 	return trunc(number*10)/10

def pathtrace(current, closed_list):
	pathlist = []
	while current.parent != None:
		pathlist.insert(0,current.position)
		for node in closed_list:
			if node == current.parent:
				current = node
	pathlist.insert(0,current.position)
	strfy = "start"
	for i in pathlist:
		strfy+="=>({},{})".format(i[0],i[1])
	strfy+="end"
	print(strfy)
	return pathlist


def disth(neighbour_pos, end):
	# end = end.position
	# return trunc((sqrt((neighbour_pos[0]-end[0])**2 + (neighbour_pos[1]-end[1])**2))*10)/10
	end = end.position
	end_x = end[0]
	end_y = end[1]
	n_x = neighbour_pos[0]
	n_y = neighbour_pos[1]

	x_diff = abs(end_x - n_x)
	y_diff = abs(end_y - n_y)

	if x_diff >= y_diff:
		dist_h = (y_diff * 14) + (x_diff - y_diff) * 10
		return dist_h/10
	elif x_diff < y_diff:
		dist_h = (x_diff * 14) + (y_diff - x_diff) * 10
		return dist_h/10


def roundoff(number):
	down = trunc(number*10)/10
	if number+0.05 > down+0.1:
		return down+0.1
	else:
		return down

def sortindex(open_list, neighbour_node):
	if len(open_list) == 0:
		return 0
	f = neighbour_node.h
	length = len(open_list)-1
	high = open_list[-1].h
	highindex = length
	low = open_list[0].h
	lowindex = 0
	if f>high:
		return highindex+1
	if f<=low:
		return 0
	estimate = round(((f - low)/(high - low))*length)
	if estimate == 0:
		estimate = 1
	if estimate >= len(open_list):
		estimate = len(open_list)-1
	print(len(open_list))
	print(estimate)

	front = open_list[estimate-1].h
	back = open_list[estimate].h
	crashcounter = 0
	while front>f or back<f:
		crashcounter+=1
		if crashcounter >= 20:
			for i in open_list:
				print(i.h)
			print(neighbour_node.h)
			raise
		#print("front = {},back = {}, f = {}".format(front,back,f))
		if estimate == lowindex:
			estimate += 1
		if front>f:
			high = front
			highindex = estimate-1
			length = estimate - lowindex -1
			estimate = round(((f - low)/(high - low))*length+lowindex)
			#print("$[{}]={},[{}] = {}, estimate[{}] = {}, length = {}".format(lowindex,low,highindex,high,estimate,f,length))
			front = open_list[estimate-1].h
			back = open_list[estimate].h
		elif back<f:
			low = back
			lowindex = estimate
			length = highindex - estimate
			estimate = round(((f - low)/(high - low))*length+lowindex)
			#print("#[{}]={},[{}] = {}, estimate[{}] = {}".format(lowindex,low,highindex,high,estimate,f))
			front = open_list[estimate-1].h
			back = open_list[estimate].h
	return estimate



def pathfinder(grid,start,end,wall,):
	open_list = []
	closed_list = []
	start = node(start,None,0)
	end = node(end,None,0)
	open_list.append(start)
	closed_list.append(end)
	while len(open_list) != 0:
		current = open_list[0]##remember to sort!
		print("current node: ({},{})".format(current.position[0],current.position[1]))
		del open_list[0]
		closed_list.append(current)
		for neighbour in [(-1,1), (0,1), (1,1), (-1,0), (1,0), (-1,-1), (0,-1), (1,-1)]:
			neighbour_pos = current + neighbour
			if neighbour_pos in wall or neighbour_pos[0]>grid[0]-1 or neighbour_pos[0]<0 or neighbour_pos[1]>grid[1]-1 or neighbour_pos[1]<0:
				continue
			if neighbour_pos in closed_list:
				if neighbour_pos == end:
					print("PATHFOUND")
					return pathtrace(current, closed_list)
				continue

			print("calculating position ({},{})".format(neighbour_pos[0],neighbour_pos[1]))
			neighbour_h = disth(neighbour_pos, end)
			if neighbour_pos not in open_list:
				h = neighbour_h
				neighbour_node = node(neighbour_pos, current.position, neighbour_h)
				index = sortindex(open_list, neighbour_node)
				open_list.insert(index, neighbour_node)

