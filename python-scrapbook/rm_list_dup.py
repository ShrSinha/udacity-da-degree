def func_rm_list_dup_values(list):
	r"""Return a new list containing unique elements of the original list. """

	unique_list = []

	for item in list:
		if item not in unique_list:
			unique_list.append(item)

	return(unique_list)



list = [1,1,2,3,4,5,5]

print(func_rm_list_dup_values(list))			
