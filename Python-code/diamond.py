n = int(input())

stars = 1
innerdashes = 0
dashes = (n-stars + innerdashes)//2
is_n_even = n%2 == 0
rows = 0

if n<=3:
    rows = 0
else:
    rows = (n-3)//2

if is_n_even:
    stars= 2
    innerdashes = 2
else:
    innerdashes= 1



print('-'*dashes + '*'*stars + "-"*dashes)

for row in range(0,rows):
    dashes-=1
    print('-'*dashes + '*' + '-'*innerdashes + '*'+ '-'*dashes)
    innerdashes+=2
if n>2:
    print('*'+ '-'*(n-2)+ '*')

for row in range(0,rows):
    innerdashes -= 2
    print('-' * dashes + '*' + '-' * innerdashes + '*' + '-' * dashes)
    dashes+=1
if n>=3:
    print('-'*dashes + '*'*stars + "-"*dashes)
