a , b = map(int,input().split())
sum_val = 0

if a > b:
    for i in range(b, a+1):
        if i%5 == 0:
            sum_val += i
    else :print(0)

elif b > a:
    for i in range(a, b+1):
        if i%5 == 0:
            sum_val += i
    else :print(0)

elif a == b:
    print(a)