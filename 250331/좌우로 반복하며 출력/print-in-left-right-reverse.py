n = int(input())

for i in range(n):
    row = list(range(1,n+1))

    if i%2 == 0:
        for j in range(n):
            print(row[j], end='')
    else:
        for j in range(n-1,-1,-1):
            print(row[j], end ='')
    
    print()