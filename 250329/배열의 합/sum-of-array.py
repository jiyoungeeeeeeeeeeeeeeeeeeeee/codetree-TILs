arr1 = [list(map(int,input().split())) for _ in range(4)]

for i in range(4):
    row_sum = 0
    for j in range(4):
        row_sum += arr1[i][j]
    print(row_sum)