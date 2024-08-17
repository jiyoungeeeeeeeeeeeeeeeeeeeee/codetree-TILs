sum_val = 0

n = int(input())

for i in range(1,n+1):
    if n%i == 0:
        sum_val += i
        if sum_val == n:
            print('P')

    elif sum_val != n:
        print('N')