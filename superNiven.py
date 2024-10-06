# Python3 implementation to check if a 
# number is Super Niven Number or not.

# Checks if sums of all subsets of digits 
# array divides the number N
def isDivBySubsetSums(arr, num):

	# To calculate length of array arr
	n = len(arr)

	# There are total 2^n subsets
	total = 1 << n

	# Consider all numbers from 0 to 2^n - 1
	i = 0
	while i < total:
		sum = 0

		# Consider binary representation of
		# current i to decide which elements
		# to pick.
		j = 0
		while j < n:
			if (i & (1 << j)):
				sum += arr[j]
				
			j += 1

		# Check sum of picked elements.
		if (sum != 0) and (num % sum != 0):
			return False
			
		i += 1
		
	return True

# Function to check if a number is 
# a super-niven number
def isSuperNivenNum(n):

	temp = n
	
	# To store digits of N
	digits = []
	
	while (n > 1):
		digit = int(n) % 10
		digits.append(digit)
		n = n / 10

	return isDivBySubsetSums(digits, temp)

# Driver code
if __name__ == '__main__': 

	n = 500
	
	if isSuperNivenNum(n):
		print("Yes")
	else:
		print("No")

# This code is contributed by jana_sayantan
