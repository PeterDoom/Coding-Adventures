n = int(input())
space = " "
star = '*'
second_part = n-1
for row in range(1,2*n):
    if row<= n:
        space = n-row
        star = row
        print(' '*space + '* '*star)
    else:
        space = row- n

        print(' '*space + '* '*second_part)
        second_part-=1