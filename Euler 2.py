#the sum of all even numbers in fibonacci
def evensum(n):
	initial, previous = 1, 1
	while initial <= n:
		yield initial #return generator 
		initial, previous = initial + previous, initial 

num = 4000000
print(sum(i for i in evensum(num) if i % 2 == 0))