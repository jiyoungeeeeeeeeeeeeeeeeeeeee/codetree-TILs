A_m, A_e = map(int, input().split())
B_m, B_e = map(int, input().split())

if A_m > B_m:
    print("A")
else:
    print("B")

if A_m == B_m:
    if A_e > B_e:
        print("A")
    else:
        print("B")