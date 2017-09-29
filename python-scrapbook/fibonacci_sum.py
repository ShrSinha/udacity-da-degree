def fibonacci_sum(index):
    """
    Return the corresponding Fibonacci sequence sum.

    Input = 
    index = Non-negative integer.

    Output =
    fibonacci_sum(3) = 2
    """
    #Indexing of Fibonacci sequence starts at 0.
    # Furthur improvement can be done by use of Hash tables.

    if index == 0 or index == 1:
        return index
    else:
        return fibonacci_sum(index-1) + fibonacci_sum(index-2)
        
