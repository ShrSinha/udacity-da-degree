def is_string_unique(str):
	r"""Return False if input string has duplicate characters.
	
	str -- string. Limited to ASCII character set.
	"""

	ascii_value_set = 128

	#If len(str) > 128, then it cannot be unique.
	if len(str) > 128:
		return False

	# List of boolean values. Index i indicates if ASCII character i is present.
	list_bool = [False for int in range(ascii_value_set)]
	
	for char in str:
		int = ord(char)
		if list_bool[int]:
			return False
		else:
			list_bool[int] = True	
	return True		



print('is_string_unique: {}'.format(is_string_unique('abcabc')))


