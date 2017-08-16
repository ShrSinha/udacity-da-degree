def func_square(limit):
	r"""Return set of all non-negtive, square integers, less than the input integer."""

	square = set()
	i = 0

	while i**2 < limit:
		square.add(i**2)
		i += 1
	
	return(square)	



# Note 0 is an integer as well as a square.
print(func_square(10))        
