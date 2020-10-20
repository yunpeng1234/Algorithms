from math import sqrt,trunc

class node(object):
	def __init__(self, position, parent, g):
		self.position = position
		self.parent = parent
		self.g = g

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

def distg(neighbour):
	if neighbour[0] == 0 or neighbour[1] == 0:
		return 1
	else:
		return 1.4

def roundoff(number):
	down = trunc(number*10)/10
	if number+0.05 > down+0.1:
		return down+0.1
	else:
		return down

def sortindex(open_list, neighbour_node):
	if len(open_list) == 0:
		return 0
	f = neighbour_node.g
	length = len(open_list)-1
	high = open_list[-1].g
	highindex = length
	low = open_list[0].g
	lowindex = 0
	print("high = {}, low = {}, f = {}".format(high,low,f))
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

	front = open_list[estimate-1].g
	back = open_list[estimate].g
	crashcounter = 0
	while front>f or back<f:
		crashcounter+=1
		if crashcounter >= 20:
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
			front = open_list[estimate-1].g
			back = open_list[estimate].g
		elif back<f:
			low = back
			lowindex = estimate
			length = highindex - estimate
			estimate = round(((f - low)/(high - low))*length+lowindex)
			#print("#[{}]={},[{}] = {}, estimate[{}] = {}".format(lowindex,low,highindex,high,estimate,f))
			front = open_list[estimate-1].g
			back = open_list[estimate].g
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
			## round down always better, explore what happens if round up? ## if dont mind pathfinding go L instead of \, can leave h,g without sqrt
			tentative_g = (current.g*10 + distg(neighbour)*10)/10##adding 2 floats messes up python for reasons
			print("g={}".format(tentative_g))
			try:
				index = open_list.index(neighbour_pos)
				neighbour_node = open_list[index]
				if neighbour_node.g > tentative_g:
					neighbour_node.g = tentative_g
					neighbour_node.parent = current.position## referral mechanism
					#sorting mechanism
					del open_list[index]##################
					open_list.insert(sortindex(open_list, neighbour_node),neighbour_node)
				elif neighbour_node.g < tentative_g:
					tentative_g = neighbour_node.g
			except(ValueError):
				neighbour_node = node(neighbour_pos, current.position, tentative_g)
				index = sortindex(open_list, neighbour_node)
				open_list.insert(index, neighbour_node)






