#largest prime

num = 600851475143
i = 2

#divide num by 2 
while i < num:
	while num % i == 0:
		#if num divide by factor == even, increment factor
		num /= i
		#else increment the prime number
	i += 1

print(int(num))