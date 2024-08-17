n = int(input())
sum_val = 0
count = 0

for i in range(n):
    s = int(input())
    sum_val += s
    count += 1


print(f"{sum_val} {sum_val/count :.1f}")