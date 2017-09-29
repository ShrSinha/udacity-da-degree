def bubble_sort(input_list):
    """
    Implement standard bubble sort.

    Input = 
    input_list = Non-empty, non-negative integer. Can have duplicates.
    e.g 43221

    Output =
    Sorted list in ascending order.  
    """
    length = len(input_list)
    while length != 1:
        for index in range(length-1):
            if input_list[index] >= input_list[index+1]:
                input_list[index],input_list[index+1] = input_list[index+1],input_list[index]
        length -= 1
    print(input_list)

# Output expected 12234
bubble_sort([4,3,2,2,1])

Time complexity = 

      
