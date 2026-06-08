arr = list(map(int, input().split()))

if arr == sorted(arr):
    print("Sorted")
else:
    print("Not Sorted")