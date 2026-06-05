a = list(map(int, input().split()))
b = list(map(int, input().split()))

common = list(set(a) & set(b))

print(common)