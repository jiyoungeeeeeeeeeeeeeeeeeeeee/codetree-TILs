prod = 1

a,b = map(int,input().split())

for i in range(1,b+1):
    prod *= a

print(prod)