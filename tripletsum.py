def find_triplet(arr, target):
    arr.sort()  # Sort the array first
    n = len(arr)

    for i in range(n - 2):  # Fix the first element
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:
                return (arr[i], arr[left], arr[right])  # Found the triplet
            elif current_sum < target:
                left += 1  # Move left pointer to increase sum
            else:
                right -= 1  # Move right pointer to decrease sum

    return None  # No triplet found


# Example usage
arr = [1, 4, 6, 8, 10, 45]
target = 22
result = find_triplet(arr, target)

if result:
    print("Triplet found:", result)
else:
    print("No triplet found")
