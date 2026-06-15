def max_area(height):
    left = 0
    right = len(height) - 1

    max_water = 0

    while left < right:
        width = right - left
        area = min(height[left], height[right]) * width

        max_water = max(max_water, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

height = [1,8,6,2,5,4,8,3,7]
print(max_area(height))