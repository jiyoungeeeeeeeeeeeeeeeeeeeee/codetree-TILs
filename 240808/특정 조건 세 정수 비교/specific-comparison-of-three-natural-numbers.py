a,b,c = list(map(int,input().split()))


# c가 최솟값일 경우
if a > c and b > c :
    if a == c :
        print(1 , end = ' ')
    else :
        print(0, end = ' ')

# b가 최솟값일 경우
if a > b and c > b:
    if a == b:
        print(1, end = ' ')
    else:
        print(0, end = ' ')

#a가 최솟값일 경우
if c > a and b > a :

  print(1, end = ' ')


if a==b==c:
    print(1, end = ' ')
else: print(0, end = ' ')