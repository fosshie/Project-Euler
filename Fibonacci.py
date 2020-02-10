#fibonacci sequence: get a specific number n
def fibseq(n): 
	if n == 1 or n == 2:
		return 1
	array = [None] * (n+1) #creating array of n elements 
	array[1] = 1 #second index = 1 
	array[2] = 2 #third index = 2
	for i in range(3, n+1): #start from with what we know to what we want (+1 because programming starts from 0)
		array[i] = array[i-1] + array[i-2] 
	return array[n]

