def two_sum_two_pointers(arr, target):
    # Store value with original index
    arr_with_index = [(val, idx) for idx, val in enumerate(arr)]
    
    # Sort by value
    arr_with_index.sort(key=lambda x: x[0])
    
    left = 0
    right = len(arr_with_index) - 1

    while left < right:
        current_sum = arr_with_index[left][0] + arr_with_index[right][0]

        if current_sum == target:
            return (arr_with_index[left][1], arr_with_index[right][1])

        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None  # no pair found


# Example usage
arr = [7, 2, 11, 15, 1, 8]
target = 9

result = two_sum_two_pointers(arr, target)
print("Indices:", result)