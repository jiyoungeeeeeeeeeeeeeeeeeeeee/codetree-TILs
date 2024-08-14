a , b = map(int,input().split())

for i in range(a,b+1):
    if i%2 == 1:
        if i * 2 <= b:
            i *= 2
    elif i%2 ==0 :
        if i + 3 <= b:
            i += 3
            
            print(i , end=' ')