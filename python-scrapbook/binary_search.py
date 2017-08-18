def binary_search(input_list, int_value):
    """Binary search function.
	
	Input:
	input_list = Distinct non-negative integer sorted in asc list. It cannot be empty.
	int_value = non-negative integer.

	Output:
    Return the index of value, or -1 if the value doesn't exist in the list.
	"""
    low_index = 0
    high_index = len(input_list)-1
    
    if int_value < input_list[low_index] or int_value > input_list[high_index]:
        return -1
    else:
        while low_index <= high_index:
            mid_index = (low_index + high_index) / 2
            if int_value == input_list[mid_index]:
                return mid_index
            elif int_value < input_list[mid_index]:
                high_index = mid_index - 1
            else:#int_value > input_list[mid_index]
                low_index = mid_index + 1
        return -1	    


test_list = [1,3,9,11,15,19,29]
#test_val1 = 25
#test_val2 = 15
test_val1 = 29
print(binary_search(test_list, test_val1))
#print binary_search(test_list, test_val2)