def is_string_unique(str):
	"""
	Return False if string has duplicate characters. Assume string to be ASCII.
	"""
	ascii_value_set = 128
	#If len(str) > 128, then it cannot be unique.
	if len(str) > 128:
		return False

	# List of boolean values. Index i indicates if ASCII character i is present.
	list = []
	for int in range(ascii_value_set):
		list.append(False)

	for char in str:
		int = ord(char)
		if list[int]:
			return False
		else:
			list[int] = True	
		
	
	return True		


print('is_string_unique: {}'.format(is_string_unique('abcabc')))


