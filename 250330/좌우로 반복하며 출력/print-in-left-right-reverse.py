n = int(input())
arr1 = [[0 for i in range(n)] for _ in range(n)]

for i in range(n):
    if i % 2 == 0:
        for j in range(1,n+1):
            print(j , end ='')
    else :
        for j in range(n,0,-1):
            print(j, end = '')

    print()