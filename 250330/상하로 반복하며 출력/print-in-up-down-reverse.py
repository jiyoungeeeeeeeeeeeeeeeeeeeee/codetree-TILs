n = int(input())
arr = [[0 for i in range(n)] for _ in range(n)]

for i in range(1,n+1):
    for j in range(n):
        if j%2 == 0:
            print(i , end = '')
        else:
            print(n+1-i , end = '')
    print()