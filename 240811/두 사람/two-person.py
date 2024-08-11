a , s1  = input().split()
b , s2  = input().split()

a = int(a)
b = int(b)


if a and b >= 19 and s1 and s2 == 'M':
    print(1)

elif (a or b >= 19 ) and (s1 or s2 == 'M'):
    print(1)
   

else: print(0)