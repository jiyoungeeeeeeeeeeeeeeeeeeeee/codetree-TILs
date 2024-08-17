n  = int(input())
sum_val = 0

for i in range(n):
    s = int(input())

    if s%2 == 1 and s%3 == 0:
        sum_val += s

print(sum_val)