n = int(input())

temp = n
sum = 0
digits = len(str(n))

while temp > 0:
    rem = temp % 10
    sum += rem ** digits
    temp //= 10

if sum == n:
    print("Armstrong")
else:
    print("Not Armstrong")