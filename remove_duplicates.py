def remove_duplicates(items):
    """Return a new list with duplicates removed, preserving order."""
    unique_list = []
    for item in items:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example usage
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
result = remove_duplicates(numbers)
print("Original list:", numbers)
print("Without duplicates:", result)
