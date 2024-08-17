sum_val = 0
counts = 0

for i in range(10):
    s = int(input())
    if  0 <= s <=200:
        sum_val += s
        counts += 1

print(f"{sum_val} {sum_val/counts:.1f}")