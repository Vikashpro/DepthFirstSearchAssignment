def dfs_stack(numbers, start_index):
    """
    Perform Depth-First Search (DFS) on a list of numbers using a stack.

    :param numbers: List of numbers to traverse
    :param start_index: Starting index for DFS
    :return: List of numbers in the order they were visited
    """
    if start_index < 0 or start_index >= len(numbers):
        raise IndexError("Starting index is out of bounds")
    
    visited = set()  # Set to keep track of visited indices
    stack = [start_index]  # Initialize stack with the start index
    order_of_visit = []  # List to store the order of indices visited

    while stack:
        index = stack.pop()  # Pop an index from the stack
        if index not in visited:
            visited.add(index)  # Mark the index as visited
            order_of_visit.append(numbers[index])  # Add the number to visit order
            # Add the next index to the stack if it's within bounds
            if index + 1 < len(numbers):
                stack.append(index + 1)
    