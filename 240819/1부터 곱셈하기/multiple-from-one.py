n = int(input())
pred = 1

for i in range(1, 11):
    pred *= i
    if pred >= n:
        break

print(i)