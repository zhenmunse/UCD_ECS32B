
"""
Node class used for Problem 2-5
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


"""
1. transform(lst)
Transform an unordered list into a Python list
Input: an (possibly empty) unordered list
Output: a Python list
"""
def transform(lst):
    result = [] # Initialize default empty list
    current = lst
    while current:  # Traverse the linked list
        result.append(current.data) # Append the data of the current node to the result list
        current = current.next
    return result

"""
2. concatenate(lst1, lst2)
Concatenate two unordered lists
Input: two (possibly empty) unordered list
Output: an unordered list
"""
def concatenate(lst1, lst2):
    if not lst1:    # If lst1 is empty, return lst2
        return lst2
    current = lst1
    while current.next: # Traverse to the end of lst1
        current = current.next
    current.next = lst2 # Link the end of lst1 to the head of lst2
    return lst1



"""
3. removeNodes(lst, i, n)
Starting from the ith node, remove the next n nodes
(not including the ith node itself).
Assume i + n <= lst.length(), i >= 0, n >= 0.
Input:
    lst -- an unrdered list
    i -- a non-negative integer
    n -- a non-negative integer
Output: an unordred list

lst = [1, 2, 3, 4, 5]
i = 2
n = 2
return [1, 2, 5]

i = 1
n = 2
return [1, 4, 5]

i = 0
n = 2
return [3, 4, 5]
"""
def removeNodes(lst, i, n):
    if not lst or not n:  # If the list is empty or n is 0, return the original list
        return lst
    
    # Case 1: Remove from head
    if not i: # If i is 0, we need to remove the first n nodes
        current = lst
        count = 0
        while current and count < n: # Move n nodes ahead
            current = current.next # Advance to the next node
            count += 1
        return current # New head of the list after removing first n nodes

    # Case 2: Otherwise
    previous = lst
    count = 0
    while previous and count < i - 1: # Move to the (i-1)th node
        previous = previous.next
        count += 1
    current = previous.next
    count = 0
    while current and count < n: # Move n nodes ahead from the ith node
        current = current.next
        count += 1
    previous.next = current # Link the (i-1)th node to the (i+n)th node
    return lst



"""
4. removeDuplicates(lst)
Remove duplicates from a sorted linked list.
Only keep one instance of each value.

Input:
    lst -- a sorted linked list (in non-decreasing order)
Output:
    the head of the updated linked list

Examples:
Input: 1 -> 1 -> 2
Output: 1 -> 2

Input: 1 -> 1 -> 2 -> 2 -> 3 -> 3 -> 4
Output: 1 -> 2 -> 3 -> 4
"""
def removeDuplicates(lst):
    current = lst
    while current and current.next: # Traverse the linked list
        if current.data == current.next.data: # If current node and next node have the same data
            current.next = current.next.next # Skip the next node
        else:
            current = current.next # Move to the next node
    return lst
