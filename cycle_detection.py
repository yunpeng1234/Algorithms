# Given a function f and a starting value i,
# Write a function determineF(i, n, k) that returns true if a value k can 
# be found with n successive applications of f to i, and false otherwise.

# Constraints
# i < 1000000007
# k < 1000000007

# Example:

def f(i):
	return i * 4 % 5

i = 1
k = 3
n = 5

# returns False

#print(determineF(f, i, n, k))


#implementing tortoise and hare algo. k is target value, n is max iterations, i is initial value, f is function
def determineF(f, i, n, k) :
	#Finds the start of the loop using the value at which loop is detected
	def find_loop_start(end) :
		p = end
		q = i
		start_count = 1
		while q != p :
			q = f(q)
			p = f(p)
			start_count += 1
		return start_count

	#Need separate values to check for loop, p would be the tortoise, q would be the hare
	p, q =i, i
	#Tracking number of function applications
	count = 1
	#q checks 2 function applications ahead so we can stop searching at n - 2
	while count <= n - 2 :
		p = f(p)
		q = f(f(q))
		#print(p," : ",q)
		if p != k :
			if p == q :
				print('loop detected')
				print('loop started at : ',find_loop_start(p))
				return False
			else :
				count += 1
		else :
			print('target reached at ', count)
			return True
	else :
		print('no loop and k not found')
		return False
