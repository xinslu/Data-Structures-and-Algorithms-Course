"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    lower_bound=0
    higher_bound=len(input_array)-1
    while lower_bound<=higher_bound:
        n=higher_bound+lower_bound
        if input_array[n//2]==value:
            return n//2
        elif input_array[n//2]>value:
            higher_bound=n//2-1
        elif input_array[n//2]<value:
            lower_bound=n//2+1
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))