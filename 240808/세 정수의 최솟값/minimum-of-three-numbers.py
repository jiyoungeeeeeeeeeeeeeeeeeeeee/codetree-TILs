a , b, c = list(map(int, input().split()))


# a가 최솟값인 경우 
if a <= b and a <= c:
    print(a)

if b <= a and b <= c:
    print(b)

else : print(c)