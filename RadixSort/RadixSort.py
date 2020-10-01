#radix_sort has a runtime complexity of O((n+b) * logb(k)) where b is the base and k is the largest possible value
def radix_sort(xs) :
	def find_place(n, b) :
		return n // b % 10 

	def radix_place_sort(xs, base) :
		counts = {}
		#set up counts dict
		for i in range(10) :
			counts[i] = 0

		for idx in range(len(xs)) :
			counts[find_place(xs[idx], base)] += 1

		for count in range(1, 10) :
			counts[count] += counts[count - 1]
		
		ys = [None for x in xs]

		for i in range(len(xs)) :
			idx = len(xs) - i - 1
			val = find_place(xs[idx], base)
			# if val == 0 :
			# 	ys[counts[0] - 1] = xs[idx]
			# 	counts[0] -= 1
			# else :
			ys[counts[val] - 1] = xs[idx]
			counts[val] -= 1						
		return ys 

	max_val = max(xs)
	num_bases = math.ceil(math.log(max_val, 10))
	for bases in range(num_bases) :
		base = 10 ** bases
		xs = radix_place_sort(xs, base)
	return xs
