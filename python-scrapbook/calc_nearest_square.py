def nearest_square(limit):
	r"""Return the largest square number that is less than the input parameter.

	limit -- int.
	"""

	i = 0

	while (i + 1)**2 < limit: 
		i += 1
	return i**2		
   


test1 = nearest_square(0)

print("expected result: 0, actual result: {}".format(test1))


