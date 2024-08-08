a , b, c = list(map(int, input().split()))


# a가 최솟값인 경우 
if a <= b and a <= c:
    print(a)

# b가 최솟값인 경우
if b <= a and b <= c:
    print(b)

# c가 최솟값인 경우
if c <= a and c <= b: 
    print(c)