n = int(input())

i = 1

while i <= n:
    if i % 3 == 0:
        print(0, end=' ')
    else:
        contains_369 = False
        for digit in str(i):
            if digit in '369':
                contains_369 = True
                break
        if contains_369:
            print(0, end=' ')
        else:
            print(i, end=' ')
    i += 1