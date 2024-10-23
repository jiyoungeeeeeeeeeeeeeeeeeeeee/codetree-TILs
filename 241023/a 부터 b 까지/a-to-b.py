a,b = list(map(int,input().split()))

i = a

while b >= i:
    print(i , end = ' ')
    if i % 2 == 0:
        i += 3
    elif i % 2 != 0:
        i *= 2