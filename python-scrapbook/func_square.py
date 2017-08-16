def func_square(limit):
	"""
	Populate set with all non-negtive square integers less than given number.
	"""
	square = set()
	i = 0

	while i**2 < limit:
		square.add(i**2)
		i += 1
	
	return(square)	

# Note 0 is an integer and a square.
print(func_square(10))        
