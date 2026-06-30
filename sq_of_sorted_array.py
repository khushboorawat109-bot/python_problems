def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1  # fill from the end

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left] * nums[left]
            left += 1
        else:
            result[pos] = nums[right] * nums[right]
            right -= 1
        pos -= 1

    return result


# Example usage
arr = [-7, -3, 2, 3, 11]
print("Squared sorted array:", sortedSquares(arr))
# Output: [4, 9, 9, 49, 121]
