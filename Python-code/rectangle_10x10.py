n = int(input())

is_n_even = n%2 ==0
range_rows =0
stars = 1
dash = (n-stars)//2

if is_n_even:
    stars =2
    range_rows = n//2
else:
    range_rows = n//2 +1

for row in range(0,int(range_rows)):
    print('-'*dash + '*'*stars + '-'*dash)
    stars+=2
    dash= (n-stars)//2

rest = n - range_rows

for row in range(0,int(rest)):
    print("|"+ "*"*(0)+ '|')