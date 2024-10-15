a_1 , a_2 = input().split()

b_1 , b_2 = input().split()

c_1 , c_2 = input().split()

a_2, b_2 , c_2 = int(a_2) , int(b_2) , int(c_2)

if (a_1 == 'Y' and a_2 >= 37) and (b_1 == 'Y' and b_2 >= 37):
    print('E')

elif (a_1 == 'Y' and a_2 >= 37) and (c_1== 'Y' and c_2 >= 37):
    print('E')

elif (b_1 == 'Y' and b_2 >= 37) and (c_1 == 'Y' and c_2 >= 37):
    print('E')

else : print('N')