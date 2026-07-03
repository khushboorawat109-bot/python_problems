def three_sum_closest(nums, target):
    nums.sort()  # Sort the array
    n = len(nums)
    closest_sum = float('inf')

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            # Update closest sum if this one is closer
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum

            # Move pointers based on comparison
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                # Exact match found
                return current_sum

    return closest_sum


# Example usage
arr = [-1, 2, 1, -4]
target = 1
result = three_sum_closest(arr, target)
print("Closest sum:", result)
