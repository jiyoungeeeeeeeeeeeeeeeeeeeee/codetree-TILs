a,b,c = list(map(int,input().split()))

if a > b and a > c:
    if  b - c > 0:
        print(b)
    else : print(c)

elif b > a and b > c :
    if a - c > 0 :
        print(a)
    else : print(c)

elif c > a and c > b:
    if a - b > 0:
        print(a)
    else : print(b)