a , s1  = input().split()
b , s2  = input().split()

a = int(a)
b = int(b)


if (a >= 19 and s1 == "M" ) and ( b >= 19 and s2 == 'M'):
    print(1)

elif (a >= 19 and s1 == "M" ) or ( b >= 19 and s2 == 'M'):
    print(1)
   

else: print(0)